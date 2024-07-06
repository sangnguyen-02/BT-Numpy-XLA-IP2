import numpy as np

arr = np.arange(9).reshape(3, 3)
print("Mảng lúc đầu:")
print(arr)

arr[:, [0, 1]] = arr[:, [1, 0]]
print("Mảng sau khi hoán đổi cột 0 và 1:")
print(arr)
