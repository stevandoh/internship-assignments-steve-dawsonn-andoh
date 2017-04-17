from sys import argv

script, filename = argv
#open a text file
txt = open(filename)
#Display the content
print txt.read()