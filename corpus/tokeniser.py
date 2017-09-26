import sys

lines = sys.stdin.readlines()

s=1

for line in lines:
	print(s, line)
	s = s + 1
	line=line.split(" ")
	index = 1
	for word in line:
		word = word.replace(" ", "").replace(".","").replace(":","").replace(")","").replace("?","").replace(",","").replace("(","")
		print(index, '\t', word, '\t','_', '\t','_','\t','_','\t','_')	
		index = index + 1
	



