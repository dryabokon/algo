# Given a string S consisting of opening and closing parenthesis '(' and ')'.
# Find length of the longest valid parenthesis substring.
# ----------------------------------------------------------------------------------------------------------------------
def find_valid_substring(A):

	stack = []
	S = ['0']*len(A)
	for i in range (0,len(A)):
		if A[i]=='(': #try to push
			S[i]='1'
			stack.append('x')
		else:#try to pop
			if len(stack)>0:
				stack.pop(0)
				S[i]='1'

	seq, longest=0,0
	for i in range(0, len(A)):
		if S[i]=='1':
			seq+=1
			if seq>longest:
				longest = seq
		else:
			seq=0

	return S, longest
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = list('((()))))()()()()')

	print(''.join(A))
	res,len = find_valid_substring(A)
	print(''.join(res))
	print(len)

