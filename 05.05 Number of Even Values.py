x= int(input("Enter a number(zero to quit:"))
even = 0
while x != 0:
 if x % 2 == 0:
     even += 1
 x= int(input("Enter a number(zero to quit:"))
print("Number of Even Values:{}".format(even))