from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("create_data.csv",encoding="utf-8")

train_data = (df["年"] <= 2021)
test_data = (df["年"] >= 2022)
interval = 1

def make_data(data):
    x = []
    y = []
    rate = list(data["終値"])
    for i in range(len(rate)):
        if i < interval : continue
        y.append(rate[i])
        xa = []
        for p in range(interval):
            d = i + p - interval
            xa.append(rate[d])
        x.append(xa)
    return (x,y)
train_x,train_y = make_data(df[train_data])
test_x,test_y = make_data(df[test_data])

lr = LinearRegression(normalize=True)
lr.fit(train_x,train_y)
pre_y = lr.predict(test_x)

plt.figure(figsize=(30,10),dpi = 100)
plt.plot(test_y,c="r")
plt.plot(pre_y,c="b")
plt.show()