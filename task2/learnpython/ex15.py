from sys import argv

script, filename = argv
#open a text file
txt = open(filename)

print "Here's your file %r:" % filename
#Display the content
print txt.read()

print "Type the filename again:"
#Prompt the user to re enter the filename
file_again = raw_input("> ")
#open it again
txt_again = open(file_again)
#read it again
print txt_again.read()