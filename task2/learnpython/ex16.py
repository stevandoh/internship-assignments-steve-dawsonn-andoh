from sys import argv
script, filename = argv

print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do wnat that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file. GoodBye!"
target.truncate()

print "Now I', going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'am going to write these to the file."
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write("%r\n%r\n%r" % (line1,line2,line3))

print "And finally, we close it."
target.close()