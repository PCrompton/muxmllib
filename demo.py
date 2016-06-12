from muxmllib import *

filename = "hello_world.xml"

#print musicxml
perfects = [1,4,5]
for i in range (-7, 8):
	if i == 0:
		continue
	elif i < 0:
		direction = 'down'
	else:
		direction = 'up'
	qualities = ['dim', 'min', 'maj', 'aug']
	if abs(i) in perfects:
		qualities.remove('maj')
		qualities[1] = 'per'
	for quality in qualities:	
		musicxml = Muxml(filename)
		print "testing:", direction, quality+str(abs(i))
		musicxml.transpose(i, quality)
		musicxml.write(filename.split('.')[0]+direction+quality+str(abs(i)))