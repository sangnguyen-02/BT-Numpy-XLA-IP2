import numpy as np

np.random.seed(101)
arr = np.random.randint(1, 4, size=6)
print("array lúc đầu:")
print(arr)

one_hot = np.eye(3)[arr - 1]

print("One-hot vector:")
print(one_hot)
