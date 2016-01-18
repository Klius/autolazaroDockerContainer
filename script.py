from subprocess import Popen,PIPE
import re

def findWholeWord(w):
	return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search


command = ['docker','ps','-a']
p = Popen(command,stdout=PIPE)
text = p.stdout.read()
retcode = p.wait()

for line in text.split("\n"):
	words = line.split()
	if findWholeWord('Exited')(line):
		image = words[len(words)-1]
		command = ['docker','start',image]
		p = Popen(command)
		retcode = p.wait
