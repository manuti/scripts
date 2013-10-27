string = "We tried list and we tried dicts also we tried Zen"
diff_words = {}

for word in string.split(' '):
	if word not in diff_words:
		#print 'New word: ' + word
		diff_words[word] = 1
	else:
		#print 'Word "' + word + '" already included'
		diff_words[word] = diff_words[word] + 1

for key, value in diff_words.items():
	print key, value
