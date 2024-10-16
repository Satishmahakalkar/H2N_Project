## H2N-DEV-interview


# XML Processing, JSON Conversion, and Data Handling in Python

## Scenario
You are working on a project that involves **processing XML order files**. Your job is to **read these files, convert them into JSON format**, and handle any **errors gracefully** during processing. This task will test your **Python skills, error handling abilities**, and how well you **log events** for traceability. 

Some XML files may contain **missing elements, malformed structures, or unexpected fields**. Your solution should ensure that the system continues processing even when some files encounter issues.

---

## Instructions

### 1. Set Up the Environment
- Create a **GitHub repository** where all your code, logs, and outputs will be stored.
- Document your entire process in the **`README.md`** of the repository, including:
  - How you approached the task.
  - Challenges you faced and how you solved them.
  - Any tools and resources (e.g., ChatGPT, forums) that you used.

---

### 2. Task Steps

1. **Reading XML Files:**
   - Download the XML files from this [ZIP file](Find in same repository).
   - Extract them into a folder named **`/xml-files/`**.

2. **Parsing XML to JSON:**
   - Write a **Python script** that:
     - Iterates through each XML file in the `/xml-files/` folder.
     - Extracts key fields (like `OrderID`, `Customer`, and `Products`).
     - **Converts the extracted data to JSON format**.

3. **Handling Errors and Logging:**
   - Some files contain **missing elements**, **malformed XML**, or **unexpected fields**.
   - Your script should:
     - **Skip invalid files** and **log appropriate error messages** in a `process.log` file. 
     - For example:
       ```
       2024-10-16 10:05: Skipped order_008.xml - Missing <Customer> element.
       2024-10-16 10:10: Parsing error in order_009.xml - Unclosed tag.
       2024-10-16 10:15: Warning in order_010.xml - Unexpected field 'Discount'.
       ```
     - Ensure the **remaining files** continue processing without interruption.

---

### 3. Bonus Task (Optional)

1. **Storing Data in SQLite (Bonus):**
   - Create a **SQLite database** with two tables:
     - **`raw_data`**: Store the original XML content.
     - **`processed_data`**: Store the JSON output.
   - Insert data into the appropriate table during the processing.

2. **Retry Mechanism for Errors (Bonus):**
   - Implement a **retry mechanism** (up to 3 attempts) for parsing files with issues.

3. **Write Unit Tests (Bonus):**
   - Use **`pytest` or `unittest`** to write unit tests for:
     - XML parsing logic.
     - Logging functionality.

---

### 4. Time Limit
- **48 hours** (2 days) to complete the task and submit your work.  
- This deadline ensures you have **enough time** to plan, code, debug, and document your solution.

---

### 5. Submission Requirements

- **GitHub Repository:**  
  - Upload your **code, logs, and README.md** to the repository.
  - Ensure your **commits** have meaningful messages.

- **README Documentation:**  
  - Describe the **steps to set up and run** your script.
  - Explain how you handled **errors and challenges**.
  - Document how you used **any online resources** (e.g., ChatGPT or forums).

---

### Evaluation Criteria

1. **Correctness:**
   - Does the code correctly **convert XML to JSON**?

2. **Error Handling:**
   - Are **errors logged** appropriately?
   - Can the script **continue processing** despite errors?

3. **Code Quality:**
   - Is the code **modular, readable, and well-organized**?

4. **Use of GitHub:**
   - Are **commits meaningful**?
   - Is the **README.md** comprehensive and clear?

5. **Bonus Points:**
   - Is the data stored in **SQLite**?
   - Is a **retry mechanism** implemented?
   - Are there **unit tests** with `pytest` or `unittest`?

---

### Expected Output Example

- **Logs (process.log):**
  ```
  2024-10-16 10:00: Processed order_001.xml successfully.
  2024-10-16 10:05: Skipped order_008.xml - Missing <Customer> element.
  2024-10-16 10:10: Warning in order_010.xml - Unexpected field 'Discount'.
  ```

- **SQLite Database (Bonus):**
  - **`raw_data` table:** Stores original XML content.
  - **`processed_data` table:** Stores JSON output.

---

This task will test your ability to **parse, convert, and log data efficiently** while handling errors gracefully. Good luck! 🎯
