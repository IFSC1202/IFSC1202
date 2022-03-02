total  = 0
seq = 0
num = 0
largest = 0
a = float(int(input("Enter a number (zero to quit):")))
smallest = a 

while a != 0 :
    if a > largest:
        largest = a
    if a < smallest:
        smallest = a
    total += a
    seq += a
    num += 1
    a = float(int(input("Enter a Number (zero to quit):")))

avg = (seq/num)

print("Count:",num)
print("Sum:",total)
print ("Average:",avg)
print("Minimum:",smallest)
print("Maximum:",largest)