from string import ascii_uppercase as u
from string import digits as d

instructions = input()
output = ""
last_digit = False
for c in instructions:
	if c in u and not last_digit:
		output += c
		last_digit = False
	elif c in u and last_digit:
		output += "\n" + c
		last_digit = False
	elif c == "+":
		output += " tighten "
		last_digit = False
	elif c == "-":
		output += " loosen "
		last_digit = False
	elif c in d:
		last_digit = True
		output += c
print(output)
