x = input("Enter Values Separated by Spaces:")
a = x.split()
for i in range (1,len(a),2):
    temp = a[i]
    a[i] = a[i-1]
    a[i-1] = temp
print("Swapped Values:",end="")
for i in range (len(a)):
    print(a[i], sep =" ",end=" ")  
print()     