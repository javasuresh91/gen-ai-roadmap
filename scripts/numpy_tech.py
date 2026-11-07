import numpy as np

price = np.array([100,200,300])
print(price)
print(type(price))

tax_in = price * 1.1
print(tax_in)

print(price.shape) # 1-D , 3 elements

grid = np.array([[1,3,5],[9,0,3]])
print(grid.shape) # 2-D 2rows , 2column (2,3)

temps = np.array([30,32,35,28,40])
print(temps.shape)
cel_fra = temps * 9/5 + 32
print(cel_fra)
twod_arr = np.array([[1,3],[4,5],[8,5]])
print(twod_arr.shape)

print('========= End 1 ===============')


temps = np.array([30,32,35,28,40])
print(temps > 33)
print(temps[temps > 33])
print(f"Mean {temps.mean()}")
grid = np.array([[1,3],[4,5],[8,5]])
print(f"Get Column 1 : {grid[:,1]}")
print(f"Row 2 : {grid[2,:]}")

arr = np.array([5,10,15,20,25])
print(arr[arr<=15])

m = np.array([[2,4,6],[8,10,12]])
print(f"Shape {m.shape}")
print(f"Only last column {m[:,2]}")

print(arr[1:3])

print(m[m>3])
print(m.mean())