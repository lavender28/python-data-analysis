import time
import numpy as np

def python_sum(n):
	a = [i**2 for i in range(n)]
	b = [i**3 for i in range(n)]
	list_sum = []
	for i in range(n):
		list_sum.append(a[i] + b[i])
	return list_sum

def numpy_sum(n):
	a = np.arange(n)**2
	b = np.arange(n)**3
	return a + b
	
time1 = time.time()
python_sum(1000000)
time2 = time.time()
print(f"python_sum 耗时: {time2 - time1:.4f} 秒")

time3 = time.time()
numpy_sum(1000000)
time4 = time.time()
print(f"numpy_sum 耗时: {time4 - time3:.4f} 秒")