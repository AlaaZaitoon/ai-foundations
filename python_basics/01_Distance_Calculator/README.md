# 📏 2D Space Distance Calculator

A Python script designed to calculate the direct Euclidean distance between two entities (e.g., a Player and an Enemy) in a 2D game environment.

## 📝 Description
This project simulates a basic game mechanic where the distance between two points is required. It takes the (x, y) coordinates for a player and an enemy, processes them using the Pythagorean theorem, and generates a formatted report.

## 🛠️ Concepts & Features
- **User Input Handling:** capturing floating-point coordinates.
- **Mathematical Logic:** Using `math.sqrt()` and `math.pow()` for accurate calculation.
- **Formatted Output:** Using **f-strings** to create a clean, readable "Calculation Report".
- **Code Structure:** The script is divided into clear steps (Input -> Processing -> Output).

## 💻 How to Run
1. Navigate to the project directory:
   ```bash
   cd python_basics/01_Distance_Calculator
   ```
2. Run the script:
   ```bash
   python distance_calculator.py
   ```

## 📊 Example Usage
When you run the script, the output will look like this:

```text
---------------------------------------
--- 2D Space Distance Calculator ---
---------------------------------------
Enter Player X position (x1): 0
Enter Player Y position (y1): 0

Enter Enemy X position (x2): 3
Enter Enemy Y position (y2): 4

--- Calculation Report ---
Player Location: (0.0, 0.0)
Enemy Location:  (3.0, 4.0)
-------------------------
Calculated Distance: 5.0 meters
---------------------------------------
```
---
*Created by Alaa Zaitoon*