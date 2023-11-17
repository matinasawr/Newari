import sys, re

line = sys.stdin.readline() # Read in a line
inside = False # We are not in the Newari part of the page
ipa = '_' # A variable to hold the current IPA 
newari_form = '_'
devanagari_form = '_'
transcription = '_'
pos = '_'
translation = '_'
finished = False

while line:
	line = line.strip('\n')
	if line.count('Newar') > 0 and line.count('[edit]') > 0: 
		# We saw the Newari heading
		inside = True
	if line.count('Retrieved from') > 0:
		# We are now outside Newari part
		inside = False
		finished = True
	if re.findall('(Rajasthani|Sanskrit)', line):
		inside = False
		finished = True

	if line.count('IPA(key)') > 0:
		# We found a line with IPA, so split
		# it by : and take the second half
		ipa = '_'
		if line.count(':') == 0:
			ipa = line.split(':')[1].strip()
		else:	
			#     * IPA(key): [muɡə:]
			ipa = line.split('[')[1].split(']')[0].strip()
		ipa = ipa.replace(':', 'ː')

	for pos_ in ['Noun', 'Verb', 'Adjective', 'Adverb', 'Pronoun']: 
		if pos_ + '[edit]' in line:
			pos = pos_

	if line.count('•') > 0:
		# 𑐎𑐮 • (kala) ? (Deva spelling कल)		
		transcription = re.findall('\([^)]+\)', line)[0]
		if line.lower().count('deva spelling') > 0:
			newari_form = line.split('•')[0].strip()
			devanagari_form = line.lower().split('deva spelling')[1].strip('() ')
		elif line.lower().count('newa spelling') > 0:
			devanagari_form = line.split('•')[0].strip()
			newari_form = line.lower().split('newa spelling')[1].strip('() ')
		# else:
		# 	print('!', line)

	if re.findall('[0-9]+\.', line):
		translation = line.strip()
	
	# Print out the line, IPA and the state (inside or outside)

	if finished:
		if newari_form != '_' and devanagari_form != '_' :
			print(f'{newari_form} | {devanagari_form} | {ipa} | {transcription} | {pos} | {translation}')
		break

	line = sys.stdin.readline() # Read in next line

