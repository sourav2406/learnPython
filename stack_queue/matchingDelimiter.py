from stackArray import StackArray

def is_matched(expr):
	lefty = '({['
	righty = ')}]'
	S1 = StackArray()
	for c in expr:
		if c in lefty:
			S1.push(c)
		elif c in righty:
			if S1.is_empty():
				return False
			if righty.index(c) != lefty.index(S1.pop()):
				return False
	return S1.is_empty()

if __name__ == '__main__':
	expr = input("Enter the expr: ")
	print(is_matched(expr))