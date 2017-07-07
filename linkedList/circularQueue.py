class CircularQueue:
	class _Node:
		__slots__ = '_element','_next'

		def __init__(self,e,nxt):
			self._element = e
			self._next = nxt

	def __init__(self):
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def front(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		head = self._tail._next
		return head._element

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		oldHead = self._tail._next
		if self._size == 1:
			self._tail = None
		else:
			self._tail._next = oldHead._next
		self._size -= 1
		return oldHead._element

	def enqueue(self,e):
		newNode = self._Node(e,None)
		if self.is_empty():
			newNode._next = newNode
		else:
			newNode._next = self._tail._next
			self._tail._next = newNode
		self._tail = newNode
		self._size += 1

	def rotate(self):
		if self._size > 0:
			self._tail = self._tail._next

	def printList(self):
		head = self._tail._next
		for i in range(self._size):
			print(head._element,end=' ')
			head = head._next
		print('\n')

if __name__ == '__main__':
	Q1 = CircularQueue()
	Q1.enqueue(1)
	Q1.enqueue(2)
	Q1.printList()
	# print(Q1.front())
	Q1.rotate()
	# print(Q1.front())
	Q1.printList()