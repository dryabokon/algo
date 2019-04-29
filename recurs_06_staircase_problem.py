# staircase problem
def count_number_of_ways(N,steps=[1,2]):

	C = 0

	for each in steps:
		if each ==N:
			C+=1

	for each in steps:
		option=N-each
		if option>0:
			s = count_number_of_ways(option,steps)
			C+=s

	return C
# ----------------------------------------------------------------------------------------------------------------------
def list_number_of_ways(N,steps=[1,2]):
	C = 0
	ways = []

	for each in steps:
		if each ==N:
			C+=1
			ways.append([N])


	for each in steps:
		option=N-each
		if option>0:
			s, options = list_number_of_ways(option,steps)
			C+=s
			for option in options:
				ways.append([each] + option)

	return C, ways
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':


	n_ways =count_number_of_ways(4)
	print(n_ways)

	n_ways,ways = list_number_of_ways(4)
	print(n_ways)

