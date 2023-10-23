import numpy as np
import matplotlib.pyplot as plt

# Define the file path
file_path = "input signals/Signal3.txt"

with open(file_path, "r") as file:
    # Skip the first three lines of metadata
    for _ in range(3):
        next(file)

    values = []
    for line in file:
        _, value = line.split()
        values.append(float(value))

# Plot the signal
plt.figure(figsize=(10, 6))
plt.plot(values, marker='o', linestyle='-', label="Continuous")
plt.title("Continuous Representation")
plt.xlabel("Sample Index (n)")  # Update the label to whatever you prefer
plt.ylabel("Value")
plt.legend()
plt.show()
