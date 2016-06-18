import os
import shutil
import xml.dom.minidom
from muxmllib import *

def compare_pitches(interval, pitch_node, params):
	pitch = Pitch(pitch_node)
	tests = [
		(pitch.step, params['step'], 'step'),
		(pitch.alter, params['alter'], 'alter'),
		(pitch.octave, params['octave'], 'octave'),
		(pitch.pitch_class, params['pitch_class'], 'pitch_class'),
		(pitch.semitone, params['semitone'], 'semitone')
	]	
	results = {}
	for t in tests:
		results[t[2]] = (t[0] == t[1], t[0], t[1])
	return results

def test_tranpose():
	pass
	dir = 'tests'
	try:
	    os.stat(dir)
	except:
	    os.mkdir(dir) 
	filename = 'hello_world.xml'
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
			musicxml = Muxml(filename)
			musicxml.get_pitches()
			musicxml.transpose(Interval(i, quality))
			musicxml.write(dir+'/'+filename.split('.')[0]+direction+quality+str(abs(i))+'.xml')
	original = Muxml(filename)
	up = 'up'
	down = 'down'
	dim = 'dim'
	min = 'min'
	per = 'per'
	maj = 'maj'
	aug = 'aug'
	upDim1 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(1)+'.xml')
	downDim1 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(1)+'.xml') 
	upPer1 = Muxml(dir+'/'+filename.split('.')[0]+up+per+str(1)+'.xml')
	downPer1 = Muxml(dir+'/'+filename.split('.')[0]+down+per+str(1)+'.xml')
	upAug1 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(1)+'.xml')
	downAug1 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(1)+'.xml')
	upDim2 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(2)+'.xml')
	downDim2 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(2)+'.xml')
	upMin2 = Muxml(dir+'/'+filename.split('.')[0]+up+min+str(2)+'.xml')
	downMin2 = Muxml(dir+'/'+filename.split('.')[0]+down+min+str(2)+'.xml')
	upMaj2 = Muxml(dir+'/'+filename.split('.')[0]+up+maj+str(2)+'.xml')
	downMaj2 = Muxml(dir+'/'+filename.split('.')[0]+down+maj+str(2)+'.xml')
	upAug2 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(2)+'.xml')
	downAug2 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(2)+'.xml')
	upDim3 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(3)+'.xml')
	downDim3 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(3)+'.xml')
	upMin3 = Muxml(dir+'/'+filename.split('.')[0]+up+min+str(3)+'.xml')
	downMin3 = Muxml(dir+'/'+filename.split('.')[0]+down+min+str(3)+'.xml')
	upMaj3 = Muxml(dir+'/'+filename.split('.')[0]+up+maj+str(3)+'.xml')
	downMaj3 = Muxml(dir+'/'+filename.split('.')[0]+down+maj+str(3)+'.xml')
	upAug3 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(3)+'.xml')
	downAug3 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(3)+'.xml')
	upDim4 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(4)+'.xml')
	downDim4 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(4)+'.xml')
	upPer4 = Muxml(dir+'/'+filename.split('.')[0]+up+per+str(4)+'.xml')
	downPer4 = Muxml(dir+'/'+filename.split('.')[0]+down+per+str(4)+'.xml')
	upAug4 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(4)+'.xml')
	downAug4 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(4)+'.xml')
	upDim5 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(5)+'.xml')
	downDim5 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(5)+'.xml')
	upPer5 = Muxml(dir+'/'+filename.split('.')[0]+up+per+str(5)+'.xml')
	downPer5 = Muxml(dir+'/'+filename.split('.')[0]+down+per+str(5)+'.xml')
	upAug5 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(5)+'.xml')
	downAug5 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(5)+'.xml')
	upDim6 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(6)+'.xml')
	downDim6 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(6)+'.xml')
	upMin6 = Muxml(dir+'/'+filename.split('.')[0]+up+min+str(6)+'.xml')
	downMin6 = Muxml(dir+'/'+filename.split('.')[0]+down+min+str(6)+'.xml')
	upMaj6 = Muxml(dir+'/'+filename.split('.')[0]+up+maj+str(6)+'.xml')
	downMaj6 = Muxml(dir+'/'+filename.split('.')[0]+down+maj+str(6)+'.xml')
	upAug6 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(6)+'.xml')
	downAug6 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(6)+'.xml')
	upDim7 = Muxml(dir+'/'+filename.split('.')[0]+up+dim+str(7)+'.xml')
	downDim7 = Muxml(dir+'/'+filename.split('.')[0]+down+dim+str(7)+'.xml')
	upMin7 = Muxml(dir+'/'+filename.split('.')[0]+up+min+str(7)+'.xml')
	downMin7 = Muxml(dir+'/'+filename.split('.')[0]+down+min+str(7)+'.xml')
	upMaj7 = Muxml(dir+'/'+filename.split('.')[0]+up+maj+str(7)+'.xml')
	downMaj7 = Muxml(dir+'/'+filename.split('.')[0]+down+maj+str(7)+'.xml')
	upAug7 = Muxml(dir+'/'+filename.split('.')[0]+up+aug+str(7)+'.xml')
	downAug7 = Muxml(dir+'/'+filename.split('.')[0]+down+aug+str(7)+'.xml')
	test_cases = [
		('upDim1', upDim1.get_pitches()[0].node, {'step': 'C', 'alter': -1, 'octave': 4, 'pitch_class': 11}),
		('downDim1', downDim1.get_pitches()[0].node, {'step': 'C', 'alter': 1, 'octave': 4, 'pitch_class': 1}),
		('upPer1', upPer1.get_pitches()[0].node, {'step': 'C', 'alter': 0, 'octave': 4, 'pitch_class': 0}),
		('downPer1', downPer1.get_pitches()[0].node, {'step': 'C', 'alter': 0, 'octave': 4, 'pitch_class': 0}),
		('upAug1', upAug1.get_pitches()[0].node, {'step': 'C', 'alter': 1, 'octave': 4, 'pitch_class': 1}),
		('downAug1', downAug1.get_pitches()[0].node, {'step': 'C', 'alter': -1, 'octave': 4, 'pitch_class': 11}),
		('upDim2', upDim2.get_pitches()[0].node, {'step': 'D', 'alter': -2, 'octave': 4, 'pitch_class': 0}),
		('downDim2', downDim2.get_pitches()[0].node, {'step': 'B', 'alter': 1, 'octave': 3, 'pitch_class': 0}),
		('upMin2', upMin2.get_pitches()[0].node, {'step': 'D', 'alter': -1, 'octave': 4, 'pitch_class': 1}),
		('downMin2', downMin2.get_pitches()[0].node, {'step': 'B', 'alter': 0, 'octave': 3, 'pitch_class': 11}),
		('upMaj2', upMaj2.get_pitches()[0].node, {'step': 'D', 'alter': 0, 'octave': 4, 'pitch_class': 2}),
		('downMaj2', downMaj2.get_pitches()[0].node, {'step': 'B', 'alter': -1, 'octave': 3, 'pitch_class': 10}),
		('upAug2', upAug2.get_pitches()[0].node, {'step': 'D', 'alter': 1, 'octave': 4, 'pitch_class': 3}),
		('downAug2', downAug2.get_pitches()[0].node, {'step': 'B', 'alter': -2, 'octave': 3, 'pitch_class': 9}),
		('upDim3', upDim3.get_pitches()[0].node, {'step': 'E', 'alter': -2, 'octave': 4, 'pitch_class': 2,}),
		('downDim3', downDim3.get_pitches()[0].node, {'step': 'A', 'alter': 1, 'octave': 3, 'pitch_class': 10}),
		('upMin3', upMin3.get_pitches()[0].node, {'step': 'E', 'alter': -1, 'octave': 4, 'pitch_class': 3}),
		('downMin3', downMin3.get_pitches()[0].node, {'step': 'A', 'alter': 0, 'octave': 3, 'pitch_class': 9}),
		('upMaj3', upMaj3.get_pitches()[0].node, {'step': 'E', 'alter': 0, 'octave': 4, 'pitch_class': 4}),
		('downMaj3', downMaj3.get_pitches()[0].node, {'step': 'A', 'alter': -1, 'octave': 3, 'pitch_class': 8}),
		('upAug3', upAug3.get_pitches()[0].node, {'step': 'E', 'alter': 1, 'octave': 4, 'pitch_class': 5}),
		('downAug3', downAug3.get_pitches()[0].node, {'step': 'A', 'alter': -2, 'octave': 3, 'pitch_class': 7}),
		('upDim4', upDim4.get_pitches()[0].node, {'step': 'F', 'alter': -1, 'octave': 4, 'pitch_class': 4}),
		('downDim4', downDim4.get_pitches()[0].node, {'step': 'G', 'alter': 1, 'octave': 3, 'pitch_class': 8}),
		('upPer4', upPer4.get_pitches()[0].node, {'step': 'F', 'alter': 0, 'octave': 4, 'pitch_class': 5}),
		('downPer4', downPer4.get_pitches()[0].node, {'step': 'G', 'alter': 0, 'octave': 3, 'pitch_class': 7}),
		('upAug4', upAug4.get_pitches()[0].node, {'step': 'F', 'alter': 1, 'octave': 4, 'pitch_class': 6}),
		('downAug4', downAug4.get_pitches()[0].node, {'step': 'G', 'alter': -1, 'octave': 3, 'pitch_class': 6}),
		('upDim5', upDim5.get_pitches()[0].node, {'step': 'G', 'alter': -1, 'octave': 4, 'pitch_class': 6}),
		('downDim5', downDim5.get_pitches()[0].node, {'step': 'F', 'alter': 1, 'octave': 3, 'pitch_class': 6}),
		('upPer5', upPer5.get_pitches()[0].node, {'step': 'G', 'alter': 0, 'octave': 4, 'pitch_class': 7}),
		('downPer5', downPer5.get_pitches()[0].node, {'step': 'F', 'alter': 0, 'octave': 3, 'pitch_class': 5}),
		('upAug5', upAug5.get_pitches()[0].node, {'step': 'G', 'alter': 1, 'octave': 4, 'pitch_class': 8}),
		('downAug5', downAug5.get_pitches()[0].node, {'step': 'F', 'alter': -1, 'octave': 3, 'pitch_class': 4}),
		('upDim6', upDim6.get_pitches()[0].node, {'step': 'A', 'alter': -2, 'octave': 4, 'pitch_class': 7}),
		('downDim6', downDim6.get_pitches()[0].node, {'step': 'E', 'alter': 1, 'octave': 3, 'pitch_class': 5}),
		('upMin6', upMin6.get_pitches()[0].node, {'step': 'A', 'alter': -1, 'octave': 4, 'pitch_class': 8}),
		('downMin6', downMin6.get_pitches()[0].node, {'step': 'E', 'alter': 0, 'octave': 3, 'pitch_class': 4}),
		('upMaj6', upMaj6.get_pitches()[0].node, {'step': 'A', 'alter': 0, 'octave': 4, 'pitch_class': 9}),
		('downMaj6', downMaj6.get_pitches()[0].node, {'step': 'E', 'alter': -1, 'octave': 3, 'pitch_class': 3}),
		('upAug6', upAug6.get_pitches()[0].node, {'step': 'A', 'alter': 1, 'octave': 4, 'pitch_class': 10}),
		('downAug6', downAug6.get_pitches()[0].node, {'step': 'E', 'alter': -2, 'octave': 3, 'pitch_class': 2}),
		('upDim7', upDim7.get_pitches()[0].node, {'step': 'B', 'alter': -2, 'octave': 4, 'pitch_class': 9}),
		('downDim7', downDim7.get_pitches()[0].node, {'step': 'D', 'alter': 1, 'octave': 3, 'pitch_class': 3}),
		('upMin7', upMin7.get_pitches()[0].node, {'step': 'B', 'alter': -1, 'octave': 4, 'pitch_class': 10}),
		('downMin7', downMin7.get_pitches()[0].node, {'step': 'D', 'alter': 0, 'octave': 3, 'pitch_class': 2}),
		('upMaj7', upMaj7.get_pitches()[0].node, {'step': 'B', 'alter': 0, 'octave': 4, 'pitch_class': 11}),
		('downMaj7', downMaj7.get_pitches()[0].node, {'step': 'D', 'alter': -1, 'octave': 3, 'pitch_class': 1}),
		('upAug7', upAug7.get_pitches()[0].node, {'step': 'B', 'alter': 1, 'octave': 4, 'pitch_class': 0}),
		('downAug7', downAug7.get_pitches()[0].node, {'step': 'D', 'alter': -2, 'octave': 3, 'pitch_class': 0})
	]
	print 'Testing:'
	results = {}
	for case in test_cases:
		case[-1]['semitone'] = 12*case[-1]['octave'] + case[-1]['pitch_class']
		result = compare_pitches(*case)
		results[case[0]] = result
	errors = []
	for key in results.keys():
		for key2 in results[key].keys():
			if not results[key][key2][0]:
				e = key+' '+key2 +': '+'result '+str(results[key][key2][1])+' should be '+str(results[key][key2][2])
				errors.append(e)
	if errors:
		for e in errors:
			print e
	else:
		print "All Test Cases Passed!"			
	shutil.rmtree(dir)

test_tranpose()	
