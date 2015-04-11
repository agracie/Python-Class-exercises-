# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below.mbox-short.txt


fname = raw_input('Enter file name: ')
try:
    fh = open(fname)
except:
    print 'File cannot be opened: ',fname
    exit()

listdata = []

for line in fh:
    line = line.rstrip()
    if not line.startswith('X-DSPAM-Confidence:') : continue
    data = line
    sdata = data.find('0')
    edata = data.find(' ',sdata)
    data = float(data[sdata:edata])
    

    print data
 


