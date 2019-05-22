# https://leetcode.com/problems/trapping-rain-water/
import math
# ----------------------------------------------------------------------------------------------------------------------
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# ----------------------------------------------------------------------------------------------------------------------
def from_roman(A):
	value={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	res =0
	i=0
	while i<len(A):
		current = 0
		if i+1<len(A):
			if value[A[i]]<value[A[i+1]]:
				current = value[A[i+1]]-value[A[i]]
				i+=2
			else:
				current=value[A[i]]
				i+=1
		else:
			current = value[A[i]]
			i+=1

		res+=current

	return res

# ----------------------------------------------------------------------------------------------------------------------
def to_roman(A):


	roman_value 		= {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}

	div = 1
	while A >= div:div *= 10
	div /= 10
	res = ''

	while A>0:

		base = int(A / div)

		if base in [0,1,2,3]:
			res += roman_value[div] * base
		elif base == 4:
			res += (roman_value[div] + roman_value[div * 5])
		elif base in [5,6,7,8]:
			res += (roman_value[div * 5] + (roman_value[div] * (base - 5)))
		elif base == 9:
			res += (roman_value[div] + roman_value[div * 10])

		A = A % div
		div /= 10


	return res
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	#A='XXX'
	#num = from_roman(A)

	xx = to_roman(1979)
	print(xx)

