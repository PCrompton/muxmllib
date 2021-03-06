from muxmllib import *

filename = "hello_world.xml"

perfects = [1,4,5]
for i in range (-7, 8):
	if i == 0:
		continue
	qualities = ['dim', 'min', 'maj', 'aug']
	direction = Interval.create(i, 'dim').direction
	if abs(i) in perfects:
		qualities.remove('maj')
		qualities[1] = 'per'
	for quality in qualities:	
		musicxml = Muxml(filename)
		print "testing:", direction, quality+str(abs(i))
		musicxml.get_pitches()
		for j in range(0, len(musicxml.pitches)):
			print musicxml.pitches[j].step + ACCIDENTALS[str(musicxml.pitches[j].alter)] + str(musicxml.pitches[j].octave)
		musicxml.transpose(Interval.create(i, quality))
		for j in range(0, len(musicxml.pitches)):
			print musicxml.pitches[j].step + ACCIDENTALS[str(musicxml.pitches[j].alter)] + str(musicxml.pitches[j].octave)
		
		#musicxml.write(filename.split('.')[0]+direction+quality+str(abs(i)))