#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.

fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp = inp.upper()
#this makes it single spaced. removes /n at end of line.
inp = inp.rstrip()
print inp
