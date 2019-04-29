# Given a string S consisting of opening and closing parenthesis '(' and ')'.
# Find length of the longest valid parenthesis substring.
# ----------------------------------------------------------------------------------------------------------------------
def find_valid_substring(A):

	stack =[-1]
	longest=0

	for i,each in enumerate(A):
		if each=='(':
			stack.append(i)
		else:
			stack.pop()
			if len(stack)==0:
				stack.append(i)
			else:
				longest = max(longest,i-stack[-1])

	return longest
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('(((())(((()')


	len = find_valid_substring(A)
	print(len)


