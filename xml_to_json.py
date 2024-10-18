import os
import json
import logging
import xml.etree.ElementTree as ET
import sqlite3
from datetime import datetime

# Set up logging
logging.basicConfig(filename='process.log', level=logging.INFO)

# Create SQLite database
conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS raw_data (id INTEGER PRIMARY KEY, content TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS processed_data (id INTEGER PRIMARY KEY, json_content TEXT)''')

def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    logging.info(f"{timestamp} - {message}")

def process_xml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            xml_content = file.read()
            # Store raw XML content in the database
            c.execute("INSERT INTO raw_data (content) VALUES (?)", (xml_content,))
            conn.commit()

            root = ET.fromstring(xml_content)
            order_id = root.find('OrderID').text
            customer = root.find('Customer').text
            products = [prod.text for prod in root.findall('Products/Product')]
            json_data = {
                'OrderID': order_id,
                'Customer': customer,
                'Products': products
            }
            # Store processed JSON in the database
            c.execute("INSERT INTO processed_data (json_content) VALUES (?)", (json.dumps(json_data),))
            conn.commit()

            log_message(f"Processed {os.path.basename(file_path)} successfully.")
            return json_data
    except ET.ParseError:
        log_message(f"Parsing error in {os.path.basename(file_path)} - Unclosed tag.")
    except Exception as e:
        log_message(f"Skipped {os.path.basename(file_path)} - {str(e)}")

def main():
    for filename in os.listdir('xml-files'):
        if filename.endswith('.xml'):
            process_xml_file(os.path.join('xml-files', filename))
    
    conn.close()

if __name__ == '__main__':
    main()

