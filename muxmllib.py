import xml.dom.minidom

PITCHES = "CDEFGAB"
CHROMATIC_SCALE = "C^D^EF^G^A^B"

# maps the number of half steps for each interval
INTERVALS ={
	'1':{'dim': -1,'per': 0,'aug': 1},
	'2':{'dim': 0,'min': 1,'maj': 2,'aug': 3},
	'3': {'dim': 2,'min': 3,'maj': 4,'aug': 5},
	'4':{'dim': 4,'per': 5,'aug': 6},
	'5':{'dim': 6,'per': 7,'aug': 8},
	'6':{'dim': 7,'min': 8,'maj': 9,'aug': 10},
	'7':{'dim': 9,'min': 10,'maj': 11,'aug': 12}
}

# maps all possible spellings for each pitch class
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

# maps the accidental symbol with the "alter" value
ACCIDENTALS = {
	'-2':'bb',
	'-1':'b',
	'0':'',
	'1':'#',
	'2':'x',
}

"""Takes a music xml filename."""
class Muxml():
	def __init__(self, filename):
		self.dom = xml.dom.minidom.parse(filename)
		self.notes = None
		self.pitches = None

	def get_note_nodes(self):
		note_nodes = []
		for note_node in self.dom.getElementsByTagName("note"):
			note_nodes.append(note_node)
		self.notes = note_nodes
	
	"""Parses object and returns all pitches found as Pitch objects."""		
	def get_pitches(self):
		if not self.notes:
			self.get_note_nodes()
		pitches = []
		for note_node in self.notes:
			for pitch_node in note_node.getElementsByTagName("pitch"):
				pitch = Pitch(pitch_node)
				pitches.append(pitch)
		self.pitches = pitches
		return pitches

	"""Transposes entire document given Interval object."""
	def transpose(self, interval):
		if not self.pitches:
			self.get_pitches()
		for pitch in self.pitches:
			pitch.transpose(interval)
	
	"""Writes object as MusicXML to filename."""			
	def write(self, filename):
		xml_str = self.dom.toxml().encode('utf-8')
		file = open(filename, 'w')
		file.write(xml_str)
		file.close()

"""Represents musical interval where -7 <= i <= 7, q is the string 'dim', 'min', 'maj', 'per', or 'aug', and 0 <= o <= 9."""
class Interval():
	def __init__(self, i, q, o=0):
		self.interval = i
		self.quality = q
		self.octave = o
		self.semitones = INTERVALS[str(abs(i))][q]*(abs(i)/i)
		self.direction = [None, 'up', 'down'][abs(i)/i]

"""Represents musical pitch given."""
class Pitch():
	def __init__(self, pitch_node):
		self.node = pitch_node
		self.step = pitch_node.getElementsByTagName("step")[0].firstChild.data
		try:
			self.alter = int(pitch_node.getElementsByTagName("alter")[0].firstChild.data)
		except:
			self.alter = 0
		self.octave = int(pitch_node.getElementsByTagName("octave")[0].firstChild.data)
		self.update()
	
	"""Returns string spelling pitch object conventionally."""
	def spell(self):
		return self.step+ACCIDENTALS[str(self.alter)]+str(self.octave)
	
	def update(self):
		self.pitch_class = (int(CHROMATIC_SCALE.find(self.step)) + self.alter) % len(CHROMATIC_SCALE)
		self.semitone = 12*self.octave + self.pitch_class
		self.update_node()
	
	def update_node(self):
		self.node.getElementsByTagName("step")[0].firstChild.data = self.step
		try:
			self.node.getElementsByTagName("alter")[0].firstChild.data = self.alter
		except:
			alter_node = self.node.ownerDocument.createElement("alter")
			text_node = self.node.ownerDocument.createTextNode(str(self.alter))
			alter_node.appendChild(text_node)
			self.node.insertBefore(alter_node, self.node.getElementsByTagName("octave")[0])
		self.node.getElementsByTagName("octave")[0].firstChild.data = self.octave
	
	"""Transposes whole document given interval object representing desired interval of transposition."""
	def transpose(self, interval):
		delta_semitone = interval.semitones
		new_semitone = self.semitone + delta_semitone
		new_pitch_class = new_semitone % 12
		delta_steps = interval.interval + -abs(interval.interval)/interval.interval #adjust the interval number to a more programming friendly value
		new_step = PITCHES[(PITCHES.find(self.step)+delta_steps)%len(PITCHES)]
		new_alter = PITCH_CLASSES[str(new_pitch_class)][new_step]
		new_octave = self.octave
		if interval.direction == 'up':
			if PITCHES.find(self.step) > PITCHES.find(new_step):
				new_octave += 1
		elif interval.direction == 'down':
			if PITCHES.find(self.step) < PITCHES.find(new_step):
				new_octave -= 1
		new_octave += interval.octave
		self.step = new_step
		self.alter = new_alter
		self.octave = new_octave
		self.pitch_class = new_pitch_class
		self.semitone = new_semitone
		self.update()
