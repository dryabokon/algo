import numpy
# ----------------------------------------------------------------------------------------------------------------------
def generate(N):

	if N == 1:
		return [[1]]
	elif N == 2:
		return [[1], [1, 1]]

	temp = generate(N - 1)
	last = temp[len(temp)-1]
	newline = [1]

	for i in range(len(last) - 1):newline.append(last[i] + last[i + 1])
	newline.append(1)
	temp.append(newline)
	return temp
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


	res = generate(5)
	print(res)

	A = [2,3,4]
	A.sort()