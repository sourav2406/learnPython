class _DoublyLinkedBase:
	class _Node:
		__slots__ = '_element','_prev','_next'

		def __init__(self,element,prev,nxt):
			self._element = element
			self._prev = prev
			self._next = nxt

	def __init__(self):
		self._header = self._Node(None,None,None)
		self._trailer = self._Node(None,None,None)
		self._header._next = self._trailer
		self._trailer._prev = self._header
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def _insertBetween(self,e,predecessor,successor):
		newElement = self._Node(e,predecessor,successor)
		predecessor._next = newElement
		successor._prev = newElement
		self._size += 1
		return newElement

	def _deleteNode(self,node):
		predecessor = node._prev
		successor = node._next
		predecessor._next = successor
		successor._prev = predecessor
		self._size -= 1
		element = node._element
		node._prev=node._next=node._element = None
		return element