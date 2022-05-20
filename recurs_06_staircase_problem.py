# staircase problem
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def get_number_of_ways2(N,steps=[1,2]):

	res = []
	for step in steps:
		if step==N:
			res.append([step])

		if N-step>=0:
			res_temp = get_number_of_ways2(N - step, steps)
			for each in res_temp:
				res.append([step] + each)

	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


	res = get_number_of_ways2(5)
	for each in res:
		print(each)

	print()
	n_ways = count_number_of_ways2(5)
	print(n_ways)
