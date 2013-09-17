# given a time, calculate the angle between the minute and hour handler
def angle( hour, minute):
	if hour == 12:
		hour = 0

	deg_per_min = 6
	min_angle = 6 * minute
	# 360/12 = 30
	hour_angle = 30 * hour + 0.5 * minute
	return abs(min_angle - hour_angle)


if __name__ == "__main__":
	print str(angle(1, 23))
	print str(angle(12, 1))
	print str(angle(1,15))
