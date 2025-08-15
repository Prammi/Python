import pandas as pd
import numpy as np
df = pd.DataFrame({"Player" : ["Sach","KingK","Zak"], "Role" : ["Master Batter","Run Machine","Speed Machine"]})
print(df)

df = pd.DataFrame([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],columns=["A","B","C","D","E"])
print(df)
print(df.values)

print("***************")
print(df.head())
print("***************")
print(df.head(2))
print("***************")
print(df.tail())
print("***************")
print(df.tail(2))

print(df.index)
print(df.columns)
print(df.index.tolist())

df = pd.DataFrame(np.arange(25, dtype=np.uint8).reshape(5,5),columns=["A","B","C","D","E"],dtype=np.uint8)
print(df)
print(df.info())
print(df.shape)
print(df.size)

print( df.describe().astype(np.uint8))
print(df["A"].mean().astype(np.uint8))
print(df["A"].unique())


