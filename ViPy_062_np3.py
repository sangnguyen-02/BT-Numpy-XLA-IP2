import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cot = ['cot1', 'cot2', 'cot3', 'cot4', 'cot5']
df = pd.read_csv(url, header=None, names=cot)

n = np.random.rand(*df.shape) < 0.5
df = df.mask(n)
df.fillna(0, inplace=True)
print(df)
