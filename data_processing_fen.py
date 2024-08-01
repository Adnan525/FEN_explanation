import pandas as pd
df = pd.read_csv("train_houdini_normal_977000.csv", header=None)
# print(df.shape)
df.columns = ["FEN", "eval"]

df = df.sample(100, ignore_index=True)
df.to_csv("train_fen.csv", index=False)
