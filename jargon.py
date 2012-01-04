#!/usr/bin/python

from random import choice

f = open("words.txt")
text = f.read()
words = text.split()
f.close()

wordChoice = choice(words)
print wordChoice

choice = 0

while True:
	spots = list('*' * 5)
	spots[0]=wordChoice[0]
	for spot in spots:
		print spot,
	choice += 1
	if (choice > 5):
		break


