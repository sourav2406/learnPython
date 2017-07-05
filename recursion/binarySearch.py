import sys

def binarySearch(data, target,low, high):
	# print(low)
	# print(high)
	if(low > high):
		return False
	else:
		mid = (low+high)//2
		#print(mid)
		if target == data[mid]:
			return True
		elif target<data[mid]:
			return binarySearch(data,target,low,mid-1)
		else:
			return binarySearch(data,target,mid+1,high)

if __name__ == '__main__':
	data = [1,2,3,5,6,7,8,9,10]
	print(data)
	search=int(input("Enter the number to be searched: "))
	if binarySearch(data,search,0,8):
		print("true")
	else:
		print("false")

	print("recursion limit:",sys.getrecursionlimit())
