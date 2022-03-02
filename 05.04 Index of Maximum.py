x= int(input("Enter a number(zero to quit:"))
maximum = x
maximumindex = 1
index = 1
if x != 0:
    while x != 0:
        if x>maximum:
            maximum = x
            maximumindex = index
        x= int(input("Enter a number(zero to quit:"))  
        index += 1
else: 
 maximumindex = 0
print("Maximum:{}".format(maximum))
print("Index of Maximum:{}".format(maximumindex)) 