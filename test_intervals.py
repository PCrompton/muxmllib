from muxmllib import *

perfects = [1,4,5]
for i in range (-7, 8):
	if i == 0:
		continue	
	qualities = ['dim', 'min', 'maj', 'aug']
	direction = Interval(i, 'dim').direction
	if abs(i) in perfects:
		qualities.remove('maj')
		qualities[1] = 'per'	
	for quality in qualities:
		interval = Interval(i, quality)
		interval._print()
		interval.invert()
		interval._print()
		print