#are rectangles overlap
# ----------------------------------------------------------------------------------------------------------------------
import numpy
# ----------------------------------------------------------------------------------------------------------------------
def are_overlap(top1,left1,bottom1,right1,top2,left2,bottom2,right2):
	check1 = (top1  < top2 and top2  < bottom1) or (top1 < bottom2 and bottom2 < bottom1)
	check2 = (left1 < left2 and left2< right1  ) or (left1 < right2 and right2 < right1)

	return check1 and check2
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
	top1, left1, bottom1, right1 = 88,	28,	66,	34
	top2, left2, bottom2, right2 = 88,	26,	94,	53

	res1 = are_overlap(top1, left1, bottom1, right1, top2, left2, bottom2, right2)

