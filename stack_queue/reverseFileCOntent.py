from stackArray import StackArray

def reverse_file(fileName):
	S = StackArray()
	original = open(fileName)
	for line in original:
		print(line)
		S.push(line.rstrip('\n'))
	original.close()
	# print(S.is_empty())
	output = open(fileName,'w')
	while not S.is_empty():
		out = S.pop()
		# print(out)
		output.write(out+'\n')
	output.close()

if __name__ == '__main__':
	reverse_file('test.txt')