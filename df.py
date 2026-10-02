import pandas as pd
import numpy as np

data = {
    "name":["Alice","Bob"],
    "age" : [45,78],
    "Salary": [6789,89443]
}

df = pd.DataFrame(data)
print(df)
print(df["age"])   # Col position
print(df.iloc[0])  # Row position
print(df[df["age"] > 50])

data = {
    "product" : ["Pen","Notebook","Eraser","Marker"],
    "price": [10,40,5,25],
    "stock" : [100,30,200,0]
}

df = pd.DataFrame(data)
print(df)
print(f"Price Column only : {df["price"]}")
print(f"ROw only {df.iloc[2]}")
print(f"Boolean masked {df[df["stock"] > 0]}")


print("=============")

df["tot"] = df["price"] * df["stock"]
print(df)
print(df[df["tot"] == df["tot"].max()])
print(df.loc[df["tot"].idxmax()])
print(df["price"].mean())

print(" =======================")


data = {
    "employee": ["A", "B", "C", "D"],
    "dept": ["Eng", "Sales", "Eng", "Sales"],
    "salary": [70000, 50000, 90000, 55000]
}
df = pd.DataFrame(data)
print("Only Eng")
print(df[df["dept"] == "Eng"])
df["bonus"] = df["salary"] * 0.1
print("Along with Bonus value")
print(df)
print("using idxmin : ")
print(df.loc[df["salary"].idxmin()])



print(type(df[df["dept"] == "Eng"]))
print(df[df["dept"] == "Eng"])



print(type(df["dept"] == "Eng"))
print(df["dept"] == "Eng")

print("=================")


data = {
    "product": ["Pen", "Notebook", "Eraser", "Marker"],
    "price": [10, 40, 5, 25],
    "stock": [100, 30, 200, 0]
}
df = pd.DataFrame(data)

print(df[(df["price"] < 30) & (df["stock"] > 50)])

print(df[(df["price"] < 10) | (df["stock"] ==0)])


def stuff_logic(s):
    return "In stock" if s > 0 else "Out of Stock"

df["stock_status"] = df["stock"].apply(stuff_logic)

print(df)


print("========================")

print(df[(df["price"] >= 25) & (df["stock"] < 100)])



def tier(s):
    return "premium" if s > 20 else "Budget"

df["price_tier"] = df["price"].apply(tier)

print(df)

print(df[~(df["stock"]>50)])

print("========Final=============")


sales_data = {
    "store": ["A", "B", "C", "D", "E"],
    "revenue": np.array([12000, 8500, 15000, 9500, 21000]),
    "expenses": np.array([9000, 7000, 10000, 8000, 15000]),
    "region": ["North", "South", "North", "South", "North"]
}
df = pd.DataFrame(sales_data)

df["profit"] = df["revenue"] - df["expenses"]

print(df)

print(df[(df["region"] == 'North') & (df["profit"] > 3000)])

def per(p):
    return "Strong" if p > 5000 else "weak"

df["performance"] = df["profit"].apply(per)

print(df)

print(df.loc[df["profit"].idxmax(),"store"])

print(df.loc[df["profit"].idxmax(),["store", "region"]])

