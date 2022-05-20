# Find jumping numbers <= X.  Example: 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.
# A number is called as a Jumping Number if all adjacent digits in it differ by 1
# ----------------------------------------------------------------------------------------------------------------------
def find_jumping_num2(x):

	res = []
	queue = list('123456789')

	while len(queue)>0:
		value = int(queue.pop())
		if value>x:continue
		res.append(value)
		last_digit = value%10
		if last_digit >= 1:
			queue.append(value*10+last_digit-1)

		if last_digit <= 8:
			queue.append(value*10+last_digit+1)

	res.sort()

	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	res = find_jumping_num2(234)
	for each in res:
		print(each)

