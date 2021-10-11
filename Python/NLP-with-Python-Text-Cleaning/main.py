import urllib.request
import string

url = "http://www.gutenberg.org/files/2701/2701-0.txt"

file = urllib.request.urlopen(url)

text = [line.decode('utf-8') for line in file]
text = ''.join(text)

text[7600:8000]

tokens = text.split()

tokens[200:222]

tokens = text.lower().split()

tokens[200:222]

table = str.maketrans('','',string.punctuation)

[word for word in tokens if word.isalpha()]