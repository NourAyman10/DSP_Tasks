import numpy as np
import matplotlib.pyplot as plt


class FirstPoint:
    def __init__(self):
        self.file_path = "Files/signal1.txt"

        with open(self.file_path, "r") as file:
            for _ in range(3):
                next(file)
            self.indices = []
            self.values = []
            for line in file:
                self.n, self.value = line.split()
                self.indices.append(int(self.n))
                self.values.append(float(self.value))

        self.indices = np.array(self.indices)
        self.values = np.array(self.values)

        plt.figure(figsize=(10, 6))
        plt.plot(self.indices, self.values, marker='o', linestyle='-', label="Continuous")
        plt.stem(self.indices, self.values, basefmt=" ", use_line_collection=True, label="Discrete")
        plt.title("Combined Continuous and Discrete Representation")
        plt.xlabel("Sample Index (n)")
        plt.ylabel("Value")
        plt.legend()
        plt.show()

