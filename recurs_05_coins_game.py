import numpy
# ----------------------------------------------------------------------------------------------------------------------
# You and your partner can pick only first or last coin from the row. What is the min guaranteed sum of your coins
# ----------------------------------------------------------------------------------------------------------------------
def game(coins,turn=0):

	if coins.shape[0]==2:
		return max(coins),[max(coins)]

	if turn==0:

		res1,sub_collection1 =  game(numpy.delete(coins,  0), 1)
		res2,sub_collection2 =  game(numpy.delete(coins, -1), 1)
		res1+= coins[0 ]
		res2+= coins[-1]
		if res1>res2:
			return res1, [coins[0 ]] + sub_collection1
		else:
			return res2, [coins[-1]] + sub_collection2
	else:
		res1,sub_collection1 = game(numpy.delete(coins,  0), 0)
		res2,sub_collection2 = game(numpy.delete(coins, -1), 0)
		if res1<res2:
			return res1, sub_collection1
		else:
			return res2, sub_collection2

# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	A = numpy.array([10,8,5,9,1,4])

	res,collection =game(A)
	print(res)
	print(collection)
