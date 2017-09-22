import sys

lines = 0
tokens = 0
characters = 0
for c in sys.stdin.read():
	if c ==' ':
		tokens = tokens + 1
	if c=='\n':
		lines = lines + 1
	characters = characters + 1

# Now add  the code to count the vowels and calculate the average syllable count
# for your language. Tip: Use the string to store the possible vowels and then an
# if statement.

print(lines, tokens, characters)