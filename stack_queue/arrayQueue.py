class ArrayQueue:
	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
		self._size = 0
		self._front = 0

	def __len__(self):
		return self._size

	def __str__(self):
		return str(self._data)

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._data[self._front]

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front+1)%len(self._data)
		self._size -= 1
		if 0 < self._size < len(self._data) // 4:
			self._resize(len(self._data)//2)
		return answer

	def enqueue(self,e):
		if self._size == len(self._data):
			self._resize(2*len(self._data))
		avail = (self._front+self._size)%len(self._data)
		self._data[avail] = e
		self._size +=1

	def _resize(self,cap):
		old = self._data
		self._data = [None] * cap
		walk = self._front
		for k in range(self._size):
			self._data[k] = old[walk]
			walk = (walk+1)%len(old)
		self._front = 0

if __name__ == '__main__':
	Q1 = ArrayQueue()

	Q1.enqueue(1)
	Q1.enqueue(2)
	Q1.enqueue(3)
	print(Q1)
	Q1.dequeue()
	Q1.dequeue()
	print(Q1)
	Q1.enqueue(4)
	Q1.enqueue(5)
	print(Q1)
	Q1.dequeue()
	print(Q1)
	Q1.enqueue(6)
	Q1.enqueue(7)
	Q1.enqueue(8)
	print(Q1)
	Q1.enqueue(9)
	print(Q1)