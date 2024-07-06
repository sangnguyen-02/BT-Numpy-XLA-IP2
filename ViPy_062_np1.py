import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cot = ['cot1', 'cot2', 'cot3', 'cot4', 'cot5']
df = pd.read_csv(url, header=None, names=cot)

data = df['cot1']
mincot1 = data.min()
maxcot1 = data.max()

result = (data - mincot1) / (maxcot1 - mincot1)
print(result)
