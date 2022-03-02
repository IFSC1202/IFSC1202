a = 0
b = 1
n = int(input("Enter Fibonacci Sequence Number:"))
if n == 0:
  print("Fibonacci Number: 0")
else:
    for i in range(2,n+1):
        temp = a
        a = b
        b = temp + b
print("Fibonacci Number:{}".format(b))  

