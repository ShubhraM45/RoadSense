import numpy as np

# --------------------------
# 1. Creating arrays
# --------------------------

numbers = np.array([1, 2, 3, 4, 5])

print("1D array:")
print(numbers)
print()

# --------------------------
# 2. Multi-dimensional arrays
# --------------------------

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("2D array:")
print(matrix)
print()

print("Shape of the 2D array:", matrix.shape)
print()

# --------------------------
# 3. Slicing
# --------------------------

print("First row:")
print(matrix[0])

print("Second column:")
print(matrix[:, 1])

print("Bottom-right element:")
print(matrix[2, 2])

print()

# --------------------------
# 4. Reshaping
# --------------------------

values = np.arange(12)  # Create an array with values from 0 to 11

print("Original array:")
print(values)

reshaped = values.reshape((3, 4))  # Reshape to 3 rows and 4 columns

print("\nReshaped array (3x4):")
print(reshaped)

print()

# --------------------------
# 5. Mean and Sum
# --------------------------

print("Mean:", reshaped.mean())
print("Sum:", reshaped.sum())