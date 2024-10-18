GitHub Repository Structure and this process in Ubuntu OS system
================================================================
/H2N-DEV-interview
├── README.md
├── process.log
├── data.db
├── xml-files/
│   ├── order_001.xml
│   ├── order_002.xml
│   └── ... (other XML files)
├── xml_to_json.py
└── test_xml_to_json.py


Sample README.md
Create or edit your README.md file to include the following information:

# XML to JSON Converter

This project parses XML order files, extracts key fields, converts them to JSON format, and logs the process. It also handles errors and stores data in an SQLite database.

## Features
- Converts XML order files to JSON.
- Handles missing elements and malformed XML.
- Logs all processes and errors to `process.log`.
- Stores raw and processed data in an SQLite database.
- Implements a retry mechanism for parsing errors.
- Includes unit tests using `unittest`.

 Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/username/H2N_Project.git
   cd  H2N_Project

Install dependencies:

pip install -r requirements.txt
python3 xml_to_json.py
---------------------------------------
Usage
Place your XML files in the xml-files/ directory.
The script will create a process.log file for logging.
Processed data will be stored in data.db.
Error Handling
The script logs errors such as:

Missing elements (e.g., <Customer>).
Malformed XML.
Unexpected fields in XML.

