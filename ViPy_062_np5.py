import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cot = ['cot1', 'cot2', 'cot3', 'cot4', 'cot5']
df = pd.read_csv(url, header=None, names=cot)

n = df['cot3'].value_counts().idxmax()
count = df['cot3'].value_counts().max()

print(f"{count}, {n:.2f}")
