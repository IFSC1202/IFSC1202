x= int(input("Enter a Number: "))
units= x%10
x= x//10
tens= x%10
hundreds= x//10
if hundreds<tens and tens<units:
 print("YES")
else:
 print("NO")