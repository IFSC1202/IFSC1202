n= int(input("Enter N: "))
prime= True
for i in range(2, n//2 +1):
 if n % i == 0:
  prime = False
if prime:
 print("PRIME")
else:
 print("COMPOSITE")
