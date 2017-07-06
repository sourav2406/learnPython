def insertionSort(A):
	for k in range(1,len(A)):
		cur = A[k]
		j = k

		while j>0 and A[j-1]>cur:
			A[j] = A[j-1]
			j-=1

		A[j] = cur

if __name__ == '__main__':
	A = [9,8,7,6,5,4,3,2,1]
	print(A)
	insertionSort(A)
	print(A)