import xml.dom.minidom

PITCHES = "CDEFGAB"
CHROMATIC_SCALE = "C^D^EF^G^A^B"

INTERVALS ={
	'1':{'dim': -1,'per': 0,'aug': 1},
	'2':{'dim': 0,'min': 1,'maj': 2,'aug': 3},
	'3': {'dim': 2,'min': 3,'maj': 4,'aug': 5},
	'4':{'dim': 4,'per': 5,'aug': 6},
	'5':{'dim': 6,'per': 7,'aug': 8},
	'6':{'dim': 7,'min': 8,'maj': 9,'aug': 10},
	'7':{'dim': 9,'min': 10,'maj': 11,'aug': 12}
}

PITCH_CLASSES = {
	'0':{'B': 1, 'C': 0, 'D':-2},
	'1':{'B': 2,'C': 1,'D': -1},
	'2':{'C': 2,'D': 0,'E': -2},
	'3':{'D': 1,'E': -1,'F':-2},
	'4':{'D': 2,'E': 0,'F': -1},
	'5':{'E': 1,'F': 0,'G': -2},
	'6':{'E': 2,'F': 1,'G': -1},
	'7':{'F': 2,'G': 0,'A': -2},
	'8':{'G': 1,'A': -1},
	'9':{'G': 2,'A': 0,'B': -2},
	'10':{'A': 1,'B': -1,'C': -2},
	'11':{'A': 2,'B': 0,'C': -1}	
}

ACCIDENTALS = {
	'-2':'bb',
	'-1':'b',
	'0':'',
	'1':'#',
	'2':'x',
}

class Muxml():
	def __init__(self, filename):
		self.dom = xml.dom.minidom.parse(filename)
	
	def transpose(self, interval, quality, octaves=0):
		for note_node in self.dom.getElementsByTagName("note"):
			for pitch_node in note_node.getElementsByTagName("pitch"):
				pitch = create_pitch(pitch_node)
				
				print pitch.step + ACCIDENTALS[str(pitch.alter)] + str(pitch.octave)
				
				pitch.transpose(interval, quality)
				
				print pitch.step + ACCIDENTALS[str(pitch.alter)] + str(pitch.octave)
				print
				
				pitch_node.getElementsByTagName("step")[0].firstChild.data = pitch.step
				try:
					pitch_node.getElementsByTagName("alter")[0].firstChild.data = pitch.alter
				except:
					pass
				pitch_node.getElementsByTagName("octave")[0].firstChild.data = pitch.octave
				
				if interval < 0:
					direction = 'down'
				else:
					direction = 'up'
				
				#self.write(self.dom, 'output/'+filename.split('.')[0]+'_'+direction+str(quality)+str(abs(interval))+str(octaves)+".xml")
		
	def write(self, filename):
		xml_str = self.dom.toxml().encode('utf-8')
		file = open(filename, 'w')
		file.write(xml_str)
		file.close()

class Pitch():
	def __init__(self, step, alter, octave):
		self.step = step
		self.alter = int(alter)
		self.octave = int(octave)
		self.pitch_class = int(PITCHES.find(step)) + self.alter
		self.semitone = 12*self.octave + self.pitch_class
	
	def transpose(self, interval, quality, octave=0):
		
		delta_semitone = INTERVALS[str(abs(interval))][quality]*(abs(interval)/interval)
		new_semitone = self.semitone + delta_semitone
		new_pitch_class = new_semitone % 12
		delta_steps = interval + -abs(interval)/interval #adjust the interval number to a more programming friendly value
		new_step = PITCHES[(PITCHES.find(self.step)+delta_steps)%len(PITCHES)]
		new_alter = PITCH_CLASSES[str(new_pitch_class)][new_step]
		new_octave = self.octave
		if interval > 0:
			if PITCHES.find(self.step) > PITCHES.find(new_step):
				new_octave += 1
		elif interval < 0:
			if PITCHES.find(self.step) < PITCHES.find(new_step):
				new_octave -= 1
		new_octave += octave
		
		self.step = new_step
		self.alter = new_alter
		self.octave = new_octave
		self.pitch_class = new_pitch_class
		self.semitone = new_semitone


def create_pitch(pitch):
	step = pitch.getElementsByTagName("step")[0].firstChild.data
	try:
		alter = pitch.getElementsByTagName("alter")[0].firstChild.data
	except:
		alter = 0
	octave = pitch.getElementsByTagName("octave")[0].firstChild.data
	return Pitch(step, alter, octave)
		

	
			


