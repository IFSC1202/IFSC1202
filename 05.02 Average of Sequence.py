sequencesum= 0
sequencecount= 0
x= int(input("Enter a Number(Zero to quit):"))
while x != 0:
    sequencesum += x
    sequencecount += 1
    x= int(input("Enter a Number (Zero to quit:"))  
if sequencecount != 0:
    sequenceaverage = sequencesum / sequencecount
    print("Average:{}".format(sequenceaverage))
else: 
    print("Sequence Length is 0")
