import xml.dom.minidom

PITCHES = "CDEFGAB"
CHROMATIC_SCALE = "C^D^EF^G^A^B"

class Pitch():
	def __init__(self, step, alter, octave):
		self.step = step
		self.alter = int(alter)
		self.octave = int(octave)
	
	def transpose(self, direction, interval, quality=0, octave=0):
		
		interval -= 1 #adjust the interval number to a more programming friendly value
		if direction == "down":
			interval = -interval
		old_step = self.step
		self.step = PITCHES[(PITCHES.find(self.step)+interval)%len(PITCHES)]
		
		if direction == "up":
			if PITCHES.find(old_step) > PITCHES.find(self.step):
				self.octave += 1
		elif direction == "down":
			if PITCHES.find(old_step) < PITCHES.find(self.step):
				self.octave -= 1
		
		

def create_pitch(pitch):
	step = pitch.getElementsByTagName("step")[0].firstChild.data
	try:
		alter = pitch.getElementsByTagName("alter")[0].firstChild.data
	except:
		alter = 0
	octave = pitch.getElementsByTagName("octave")[0].firstChild.data
	return Pitch(step, alter, octave)
		
def write_xml(dom_obj, filename):
	xml_str = dom_obj.toxml().encode('utf-8')
	file = open(filename, 'w')
	file.write(xml_str)
	file.close()
	
def transpose_doc(filename, direction, interval, quality=0, octaves=0):
	musicxml = xml.dom.minidom.parse(filename)
	for note_node in musicxml.getElementsByTagName("note"):
		for pitch_node in note_node.getElementsByTagName("pitch"):
			pitch = create_pitch(pitch_node)
			
			#print pitch.step, pitch.alter, pitch.octave
			pitch.transpose(direction, interval)
			#print pitch.step, pitch.alter, pitch.octave
			
			pitch_node.getElementsByTagName("step")[0].firstChild.data = pitch.step
			try:
				pitch_node.getElementsByTagName("alter")[0].firstChild.data = pitch.alter
			except:
				pass
			pitch_node.getElementsByTagName("octave")[0].firstChild.data = pitch.octave
			
			write_xml(musicxml, filename.split('.')[0]+direction+str(interval)+str(quality)+str(octaves)+".xml")
			


