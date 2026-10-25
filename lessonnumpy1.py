import numpy as np
height = [1.80, 1.60, 1.75, 1.90, 1.50]
weight = [81, 51.2, 70, 72.2, 54]
np_height = np.array(height)
np_weight = np.array(weight)
bmi = np.round(np_weight / np_height ** 2, 2)
print(bmi)

np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
[65.4, 59.2, 63.6, 88.4, 68.7]])
print(np_2d.shape) 
print(np_2d.ndim)
print(np_2d.size) 
print(np_2d.dtype) 
print(np_2d[0][2])
print(np_2d[0, 2]) 
print(np_2d[:, 1:3])

print(np.arange(0, 10, 2)) 
print(np.linspace(0, 1, 5)) 
print(np.zeros((2, 3))) 
print(np.ones(3))
x = np.array([1, 2, 3, 4, 5, 6])
print(x.reshape(2,3))


data = np.array([1, 2, 3, 4, 100])
print(np.mean(data))
print(np.median(data))
print(np.std(np.array([2, 4, 4, 4, 5, 5, 7, 9]))) 

#axis
m = np.array([[1, 2, 3],
[4, 5, 6]])
print(m.sum())
print(m.sum(axis=0))
print(m.sum(axis=1))

a = np.array([3, 1, 2])
print(np.sort(a))
print(np.argmax(np.array([3, 9, 2]))) 
x = np.array([1, 2, 3, 4, 5, 6])
print(np.where(x > 3, "big", "small"))


np.random.seed(42)
heights = np.random.normal(170, 9, 5)