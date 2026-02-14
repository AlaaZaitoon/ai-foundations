# 🎓 Student Grading System

A clean, class-based Python project that analyzes student scores and prints a professional performance report with **letter grades**, **class summary**, and **Top 3 ranking**.

## 📝 Description
This project simulates a mini “grading analytics” tool.  
It takes a classroom dataset in the form of a Python **Dictionary** (`{student_name: [scores]}`), processes each student’s scores, and generates:

- Per-student performance stats (Average, Best, Worst)
- Pass/Fail result based on a configurable threshold
- Letter grade (A, B, C, D, F)
- A class-level summary (class average, pass rate, top/bottom student)
- Top 3 leaderboard ranked by average score

## 🛠️ Concepts Applied
- **OOP (Classes):** Organized logic using a `StudentGradingSystem` class.
- **Data Structures:**
  - `Dictionary`: store student name → list of scores
  - `List`: iterate, compute statistics, sorting for ranking
- **Loops & Control Flow:** `for`, `if/else`, filtering valid records
- **Statistics:** Average calculation using `statistics.mean()`
- **Clean Output Formatting:** Fixed-width, table-like report using f-strings

## 📁 Project Structure (suggested)
```text
03_Student_Grading_System/
├── analysis.py
└── README.md
```

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd python_basics/03_Student_Grading_System
   ```
2. Run the script:
   ```bash
   python analysis.py
   ```

## ⚙️ Input Format
Inside the file, you’ll define a dataset like this:

```python
classroom_data = {
    "Alaa":  [98, 92, 95, 97],
    "Ahmed": [45, 50, 48, 55],
    "Sara":  [95, 88, 92, 97],
    "Omar":  [60, 65, 58, 62],
    "NoScores": []
}
```

## 📊 Output Example
**Console Output (example):**
```text
========================================================================
STUDENT GRADING SYSTEM - PERFORMANCE REPORT
========================================================================
Name           |    Avg |   Best |  Worst | Grade | Status     | #Scores
------------------------------------------------------------------------
Alaa           |  95.50 |     98 |     92 |   A   | PASSED     |       4
Ahmed          |  49.50 |     55 |     45 |   F   | FAILED     |       4
Sara           |  93.00 |     97 |     88 |   A   | PASSED     |       4
Omar           |  61.25 |     65 |     58 |   D   | PASSED     |       4
NoScores       |      - |      - |      - |   -   | NO DATA    |       0
========================================================================
CLASS SUMMARY
------------------------------------------------------------------------
Students (total) : 5
Students (valid) : 4
Class Average    : 74.81
Pass Rate        : 75.00%
Top Student      : Alaa
Bottom Student   : Ahmed
========================================================================
TOP 3 RANKING
------------------------------------------------------------------------
1) Alaa  - Avg: 95.50 | Grade: A | PASSED
2) Sara  - Avg: 93.00 | Grade: A | PASSED
3) Omar  - Avg: 61.25 | Grade: D | PASSED
========================================================================
```

## 🧩 Customization Ideas
- Change passing mark:
  - `StudentGradingSystem(classroom_data, pass_mark=60)`
- Change allowed score range:
  - `min_score=0`, `max_score=100`
- Add exporting results to CSV for a more “data engineering” feel

---
*Created by Alaa Zaitoon*