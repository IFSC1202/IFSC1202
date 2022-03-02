def FahrToCel(Fvalue):
    Fvalue = (F-32)*5/9
inputfilename = "Ftemps.txt"
outputfilename  = "Ctemps.txt"
recordcount = 0
inputfile = open(inputfilename,'r')
outputfile = open(outputfilename,'w')
ftemp = inputfile.readline()
while ftemp !='':
    ctemp = FahrToCel(float(ftemp))
    outputfile.write(str(round(ctemp,1)) + "/n")
    recordcount += 1
    ftemp = inputfile.readline()
inputfile.close() 
outputfile.close()   
print("{}records written".format(recordcount))

