A = list('()((())))()(')
# ----------------------------------------------------------------------------------------------------------------------
def is_valid_substring2(A):
	def is_pair(a,b):return (a=='(' and b==')')or(a=='[' and b==']')or(a=='{' and b=='}')
	queue = [A[0]]
	for a in A[1:]:
		if len(queue)==0:
			queue.append(a)
			continue

		if is_pair(queue[-1],a):
			queue.pop()
		else:
			queue.append(a)

	return len(queue)==0
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('()((())())()')

	res = is_valid_substring2(A)
	print(res)

