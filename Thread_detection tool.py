import os
import re

def scan_file(file_path, threat_data):
    with open(file_path, 'rb') as file:
        content = file.read()
    
    for threat in threat_data:
        if re.search(threat, content):
            return True
    return False

def scan_directory(directory_path, threat_data):
    threats_detected = []
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file(file_path, threat_data):
                threats_detected.append(file_path)
    
    return threats_detected

# Sample usage
threat_data = [b'malicious_pattern_1', b'malicious_pattern_2']
directory_path = 'C:/Users/your_username/Documents'

threats = scan_directory(directory_path, threat_data)
if threats:
    for threat in threats:
        print(f"Threat detected: {threat}")
else:
    print("No threats detected.")
