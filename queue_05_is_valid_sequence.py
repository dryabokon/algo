#
# ----------------------------------------------------------------------------------------------------------------------
def is_valid_substring(A):

	q=[]
	for element in A:
		if len(q)==0:
			q.append(element)
		else:
			candidate = q[-1]
			if (candidate=='{' and element=='}') or (candidate=='(' and element==')') or (candidate=='[' and element==']'):
				q.pop()
			else:
				q.append(element)


	return len(q)==0
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('()')

	res = is_valid_substring(A)
	print(res)

