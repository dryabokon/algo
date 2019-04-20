# staircase problem
def count_number_of_ways(N,steps):

	for each in steps:
		if each ==N:
			return 1,[[N]]

	n_ways=0
	ways = []
	for each in steps:
		option=N-each
		if option>0:
			s, options = count_number_of_ways(option,steps)
			n_ways+=s
			for option in options:
				ways.append([each] + option)

	return n_ways, ways
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


	n_ways,ways =count_number_of_ways(10,steps=[1,2,3])
	print(n_ways)
	for each in ways:
		print(each)

