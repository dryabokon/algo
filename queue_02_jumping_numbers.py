#  Find jumping numbers <= X.  Example: 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
# ----------------------------------------------------------------------------------------------------------------------
def find_jumping_num(x):

	queue=[0,1,2,3,4,5,6,7,8,9]
	res=[]

	while (len(queue)>0):
		num = queue.pop(0)

		if num <= x and num>0:
			res.append(str(num))

			last_dig = num % 10

			if last_dig == 0:
				queue.append((num * 10) + 1)

			elif last_dig == 9:
				queue.append((num * 10) + 8)

			else:
				queue.append((num * 10) + (last_dig - 1))
				queue.append((num * 10) + (last_dig + 1))

	return res

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	res = find_jumping_num(34)
	for each in res:
		print(each)

