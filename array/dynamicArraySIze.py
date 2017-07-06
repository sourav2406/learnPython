import sys
from time import time

data = []
for k in range(25):
	a = len(data)
	b = sys.getsizeof(data)
	# print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))
	# print(data)
	start = time()
	data.append(None)
	end = time()
	print(end-start) 