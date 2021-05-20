"""message - a string to encode/decode
key - a key consists of only lower case letters
initShift - a non-negative integer representing the initial shift"""


message = "There is no spoon"

init_key = "Bluepill"

init_shift = 4

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Create a key
key = ""

# Remove duplicates
for i in init_key:
	if i not in key:
		key += i

# Add any letters not in initial key
for j in alphabet:
	if j not in init_key.lower():
		key += j

# Create a key alphabet
enum = enumerate(key)
key_alphabet = dict((k+1, l) for k,l in enum)


# Find first letter using init_shift
shift = 0  # 25 (Y)

for m, n in key_alphabet.items():
	if n == message[0].lower():
		shift = m + init_shift

# Find remaining letters using new shift
positions = []

positions.append(shift)


counter = 1

while counter < len(message):
    for o, p in key_alphabet.items():
	    if p == message[counter].lower():
	    	if (o + shift) > 26:
	    		positions.append(o+(shift-26))
	    		shift = o
	    	else:
	    		positions.append(o+shift)
	    		shift = o
    counter += 1

result = ""

print("Message: ", message)
print("key_alphabet: ", key_alphabet)
print("Positions: ", positions)


# Find the gaps
gaps = []

counterb = 0

for q in message:
	if q == " ":
		gaps.append(counterb)
	counterb += 1

print("gaps:", gaps)

# Convert
for r in positions: 
	for s, t in key_alphabet.items():
		if r == s:
			result += t
print("Result: ", result)
