class LinkedQueue:
	class _Node:
		__slots__ = '_element','_next'

		def __init__(self,element,nxt):
			self._element = element
			self._next = nxt

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		return self._head._element

	def dequeue(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		answer = self._head._element
		self._head = self._head._next
		self._size -= 1
		if self.is_empty():
			self._tail = None
		return answer

	def enqueue(self, e):
		new = self._Node(e,None)
		if self.is_empty():
			self._head = new
		else:
			self._tail._next = new
		self._tail = new
		self._size += 1

	def printQueue(self):
		node = self._head
		while node != None:
			print(node._element,end=' ')
			node = node._next
		print('\n')

if __name__ == '__main__':
	Q1 = LinkedQueue()
	Q1.enqueue(1)
	Q1.enqueue(2)
	Q1.printQueue()
	Q1.enqueue(3)
	Q1.enqueue(4)
	Q1.printQueue()
	Q1.dequeue()
	Q1.printQueue()
	Q1.dequeue()
	Q1.printQueue()