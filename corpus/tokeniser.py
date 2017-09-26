import sys

lines = sys.stdin.readlines()

e = 1

for line in lines:
	print("# sent_id =",e)
	print("# text =", line.strip())
	line=line.strip().split(" ")
	index = 1
	for word in line:
		word = word.replace(" ", "").replace(".","").replace(":","").replace(")","").replace("?","").replace(",","").replace("(","")
		print(index, '\t', word, '\t','_', '\t','_','\t','_','\t','_')	
		index = index + 1
	e = e+1
	print()
	



