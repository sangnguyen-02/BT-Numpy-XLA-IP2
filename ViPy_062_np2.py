import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cot = ['cot1', 'cot2', 'cot3', 'cot4', 'cot5']
df = pd.read_csv(url, header=None, names=cot)

result = df[(df['cot1'] > 1.5) & (df['cot3'] < 5.0)]
print(result)
