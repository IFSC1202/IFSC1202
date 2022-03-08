def ProperCase(s):
    return s[0:1].upper() + s[1:].lower()
def RemoveCR(s):
    return s.replace("/n","")   
def Trim(s):
    return s.strip(" ")  
def FirstName(s):
    firstnameindex=s.find(" ")    
    firstname=s[:firstnameindex] 
    firstname=ProperCase(firstname)
    return firstname
def LastName(s):
    lastnameindex=s.rfind(" ") +1
    lastname=s[lastnameindex:]   
    lastname=ProperCase(lastname)
    return lastname
def MiddleName(s):
    firstnameindex= s.find(" ") 
    lastnameindex= s.rfind(" ") + 1
    middlename= s[firstnameindex:lastnameindex]
    middlename= Trim(middlename)
    middlename= ProperCase(middlename)
    if len(middlename) == 1:
        middlename += "."
    return middlename
print("{:10s} {:10s} {:10s}".format("First","Middle","Last"))
print("{:10s} {:10s} {:10s}".format("-"*10,"-"*10,"-"*10))   
inputfile = open("names.txt",'r') 
fullname= Trim(RemoveCR(inputfile.readline()))   
while fullname != "":
    print("{:10s} {:10s} {:10s}".format(FirstName(fullname),MiddleName(fullname),LastName(fullname)))
    fullname= Trim(RemoveCR(inputfile.readline()))

