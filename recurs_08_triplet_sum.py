# ----------------------------------------------------------------------------------------------------------------------
def triplet_S(A, S=0, elements=3):

	if elements==2:
		res = []
		dct = {}
		for a in A:
			if a * 2 == S:
				dct[a] = (a in dct)
			else:
				dct[S - a] = 1

		for a in A:
			if a in dct and dct[a] > 0 and a*2>=S:
				res.append([a, S - a])
				dct[a]=0

		return res

	elif elements==3:
		A.sort()
		res = []
		for i in range(len(A)):
			a = A[i]
			if i>0 and A[i-1]==A[i]:continue

			res_temp = triplet_S(A[i+1:], S=S-a, elements=2)
			for r in  res_temp:
				res.append([a]+r)

		dct = {}
		res2 = []
		for r in res:
			# hash1 = (r[0],r[1])
			# hash2 = (r[1],r[0])
			# hash3 = (r[0],r[2])
			# hash4 = (r[2],r[0])
			#
			# if hash1 in dct or hash2 in dct:continue
			# if hash3 in dct or hash4 in dct: continue
			# dct[hash1] = 1
			# dct[hash2] = 1
			# dct[hash3] = 1
			# dct[hash4] = 1
			res2.append(r)


		return res2

# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	#A = numpy.array(list('476123'),dtype=numpy.int)
	#A = [-1, 0, 1, 2, -1, -4]

	A = [3, 0, -2, -1, 1, 2]
	res = triplet_S(A)
	print(res)