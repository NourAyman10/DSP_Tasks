import numpy as np
import matplotlib.pyplot as plt

# Define the file path
file_path = "C:/Users/future/Downloads/signal1.txt"


with open(file_path, "r") as file:
    # Skip the first three lines of metadata
    for _ in range(3):
        next(file)

    
    indices = []
    values = []
    for line in file:
        n, value = line.split()
        indices.append(int(n))
        values.append(float(value))


indices = np.array(indices)
values = np.array(values)

# Display the signal in continuous representation
#plt.figure(figsize=(12, 4))
#plt.subplot(121)
#plt.plot(indices, values, marker='o', linestyle='-')
#plt.title("Continuous Representation")
#plt.xlabel("Sample Index (n)")
#plt.ylabel("Value")

# Display the signal in discrete representation
#plt.subplot(122)
#plt.stem(indices, values, basefmt=" ", use_line_collection=True)
#plt.title("Discrete Representation")
#plt.xlabel("Sample Index (n)")
#plt.ylabel("Value")

#plt.tight_layout()
#plt.show()

plt.figure(figsize=(10, 6))

# Plot the continuous representation
plt.plot(indices, values, marker='o', linestyle='-', label="Continuous")

# Overlay the discrete representation using stem
plt.stem(indices, values, basefmt=" ", use_line_collection=True, label="Discrete")

plt.title("Combined Continuous and Discrete Representation")
plt.xlabel("Sample Index (n)")
plt.ylabel("Value")
plt.legend()

plt.show()