import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
cot = ['cot1', 'cot2', 'cot3', 'cot4', 'cot5']
df = pd.read_csv(url, header=None, names=cot)
def ham(l):
    if l < 3:
        return 'small'
    elif 3 <= l < 5:
        return 'medium'
    else:
        return 'large'

result = df['cot3'].apply(ham).tolist()
print(result[0:4])
