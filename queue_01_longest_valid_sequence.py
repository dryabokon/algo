# Given a string S consisting of opening and closing parenthesis '(' and ')' f
# find length of the longest valid parenthesis substring.
# ----------------------------------------------------------------------------------------------------------------------
def find_valid_substring(A):

	stack =[-1]
	longest_length,res=0,None

	for i,a in enumerate(A):
		print(stack)
		if a=='(':
			stack.append(i)
		else:
			stack.pop()
			if len(stack)>0:
				valid_length = i - stack[-1]
				if valid_length>longest_length:
					longest_length = valid_length
					res = A[i - valid_length + 1:i + 1]
			else:
				stack.append(i)

	return longest_length,res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list(')))((((((())()()')


	len,res = find_valid_substring(A)
	print(len)
	print(''.join(res))


