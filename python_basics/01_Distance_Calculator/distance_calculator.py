"""
Project Name: Euclidean Distance Calculator
File Name: distance_calculator.py
Author: Alaa Zaitoon
Description: 
    This script calculates the direct distance (Euclidean distance) 
    between two points (Player and Enemy) in a 2D plane.
    It applies the Pythagorean theorem: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
"""

import math

print("---------------------------------------")
print("--- 2D Space Distance Calculator ---")
print("---------------------------------------")

# ---------------------------------------------------------
# Step 1: Input Collection
# We gather coordinates for both points (Player and Enemy).
# ---------------------------------------------------------

# Player Coordinates (Point A)
x1 = float(input("Enter Player X position (x1): "))
y1 = float(input("Enter Player Y position (y1): "))

print("\n")  # Just for better spacing in terminal

# Enemy Coordinates (Point B)
x2 = float(input("Enter Enemy X position (x2): "))
y2 = float(input("Enter Enemy Y position (y2): "))

# ---------------------------------------------------------
# Step 2: Processing (The Logic)
# Calculate the differences in coordinates (deltas)
# ---------------------------------------------------------

delta_x = x2 - x1
delta_y = y2 - y1

# Apply Euclidean distance formula
# Using math.pow for squaring and math.sqrt for the root
distance = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))

# ---------------------------------------------------------
# Step 3: Output Visualization
# Display the result formatted to 2 decimal places
# ---------------------------------------------------------

print("\n--- Calculation Report ---")
print(f"Player Location: ({x1}, {y1})")
print(f"Enemy Location:  ({x2}, {y2})")
print("-" * 25)
print(f"Calculated Distance: {round(distance, 2)} meters")
print("---------------------------------------")