prevx= int(input("Enter a Number(zero to quit):"))
count = 0
while prevx !=0:
  x= int(input("Enter a Number(zero to quit):"))
  if x != 0 and prevx < x:
    count += 1
  prevx = x
print("Number of Values Greater Than the Previous:{}".format(count))    
