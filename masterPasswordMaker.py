#!/usr/bin/env python
import argparse
import math
import random

# Parse command line
parser = argparse.ArgumentParser(
	description = 'Generate a random password from a wordlist',
	formatter_class = argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--file'    , default = 'words.txt', help='file to get wordlist from')
parser.add_argument('--numWords', type = int, default = 5, help='number of words to generate')
args = parser.parse_args()

# Read wordlist
words = []
with open(args.file) as f:
	for line in f.readlines():
		words.append(line.strip())

# Generate password
passwordLength = 0
for _ in range(0, args.numWords):
	word = random.choice(words)
	passwordLength += len(word)
	print(word)

# Show statistics
estimatedEntropy = args.numWords * math.log(len(words), 2)
print("Entropy: {0}".format(estimatedEntropy))
print("Length : {0}".format(passwordLength))

