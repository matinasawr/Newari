import sys, re

def replace_keep_case(word, replacement, text): 
	def func(match):
		g = match.group ()
		#print ('!', match, "|", g, file=sys.stderr)
		if g.islower(): return replacement.lower() 
		if g.istitle(): return replacement.title() 
		if g.isupper(): return replacement.upper()
		return replacement
	#return re.sub(word, func, text)#, flags=re.I)
	return re.sub(word, replacement, text)#, flags=re.I)

if len(sys.argv) != 2:
	print('convertor.py [TSV FILE]', file=sys.stderr)
	sys.exit(-1)


table = {}
for line in open(sys.argv[1]).readlines():
	row = line.split(',')
	nw = row[0].strip().upper()
	IPA = row[1].strip()
	table[nw]=IPA 
	
line = sys.stdin.readline().strip()
while line:

	tokens = re.sub('([:,.!?]+)', ' \g<1> ', line.upper()).split (' ')
	normalized_tokens = []
	
	for token in tokens:
		for nw,IPA in table.items():
			token = replace_keep_case(nw,IPA,token)
		normalized_tokens.append(token.strip())

	newline = ' '.join(normalized_tokens)
	print(re.sub('  *', ' ', newline))

	line = sys.stdin.readline().strip()

	# kala_sentence = 'kala is the IPA for machine'
	# re.sub('kala', 'kələ', kala_sentence)
	# print(kala_sentence)

