file = open('5Dataset.txt')
words = file.read().splitlines()
file.close()

for x in range(0, len(words)):
	if (x % 2 == 1):
		print words[x]
