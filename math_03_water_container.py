# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which
# together with x-axis forms a container, such that the container contains the most water.
# ----------------------------------------------------------------------------------------------------------------------
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def maxArea(H):

	left, right = 0, len(H) - 1
	area = 0
	while left != right:

		if H[left] < H[right]:
			area = max((right-left)*H[left], area)
			left += 1
		else:
			area = max((right-left)*H[right], area)
			right -= 1
	return area
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	h,m = 13,30

	res = maxArea([1,8,6,2,5,4,8,3,7])
	print(res)

	