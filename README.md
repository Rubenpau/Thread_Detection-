# Simple Thread_Detection Tool

This Python tool is a basic example of a Thread detection utility. It scans files in a specified directory for predefined malicious patterns. Please note that this is a simplified example and not suitable for actual security use.

## Usage

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/Rubenpau/Thread-Detection-tool.git
   cd Thread-Detection-tool
   ```

2. **Install Dependencies (if required):**

   There are no external dependencies for this tool.

3. **Run the Tool:**

   To scan a directory for potential threats, execute the following command:

   ```sh
   python Thread_detector.py
   ```

4. **Configure Threat Data:**

   Open the `malware_detector.py` file and modify the `threat_data` list to include the patterns you want to detect. Add your own malicious patterns or use existing ones.

   ```python
   threat_data = [b'malicious_pattern_1', b'malicious_pattern_2']
   ```

5. **Specify the Directory to Scan:**

   Edit the `directory_path` variable to specify the directory you want to scan for threats.

   ```python
   directory_path = 'C:/Users/your_username/Documents'
   ```

6. **Run the Tool:**

   Run the tool again to scan the updated directory with the new threat data:

   ```sh
   python Thread_detector.py
   ```

7. **View the Results:**

   The tool will display the files in the specified directory that match the threat data.

## Important Notes

- Be cautious when using this tool, and do not use it on sensitive or critical systems.
- Always handle potentially malicious files with care. Quarantine or remove them if necessary.
- This tool is a basic example for educational purposes and is not a substitute for a professional antivirus solution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

