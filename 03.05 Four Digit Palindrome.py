x= int(input("Enter a Number:"))
units= x%10
x= x//10
tens= x%10
x= x//10
hundreds= x%10
thousands= x//10
if thousands== units and hundreds ==  tens:
 print("YES")
else: 
 print("NO")
