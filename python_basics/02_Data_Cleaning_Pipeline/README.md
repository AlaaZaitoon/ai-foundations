# 🧹 Data Cleaning Pipeline

An automated Python script that simulates a real-world data engineering task. It extracts unstructured data, cleans it, and exports structured results.

## 📝 Description
This project demonstrates how to build a simple ETL (Extract, Transform, Load) pipeline. It generates a messy text file containing hidden emails, uses **Regular Expressions** to find them, removes duplicates using **Sets**, and saves the clean list to a CSV file.

## 🛠️ Concepts Applied
- **RegEx (Regular Expressions):** Advanced pattern matching `([\w\.]+)@(\w+)\.([a-z]{3})`.
- **Data Structures:** - `Set`: To automatically remove duplicate entries.
  - `Dictionary`: To calculate domain statistics (e.g., count of Gmail vs Yahoo).
- **File Handling:** Reading `.txt` and writing `.csv` files safely using `with open()`.
- **Functions:** Organizing code into reusable blocks (`create_dummy_data`, `process_data`).

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd python_basics/02_Data_Cleaning_Pipeline
   ```
2. Run the pipeline:
   ```bash
   python main.py
   ```

## 📊 Output Example
The script will generate a `raw_data.txt` file and a `cleaned_emails.csv` file.

**Console Output:**
```text
[Success] Dummy data file 'raw_data.txt' created.

--- Processing 'raw_data.txt' ---
Raw matches found: 6
Unique emails saved: 5
Domain Stats: {'google': 1, 'python': 1, 'virus': 1, 'horus': 1, 'yahoo': 2}
[Success] Clean data saved to 'cleaned_emails.csv'
```
---
*Created by Alaa Zaitoon*