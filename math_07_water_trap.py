# https://leetcode.com/problems/trapping-rain-water/
# ----------------------------------------------------------------------------------------------------------------------
def maxArea(H):
	left, right = 0, len(H) - 1
	area = 0
	left_max,right_max = 0,0
	while left < right:

		if H[left] < H[right]:
			if H[left] >= left_max:
				left_max = H[left]
			else:
				area += left_max - H[left]
			left += 1
		else:
			if H[right] >= right_max:
				right_max = H[right]
			else:
				area += (right_max - H[right])
			right-=1
	return area


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

	res = maxArea([0,1,0,2,1,0,1,3,2,1,2,1])
	print(res)

