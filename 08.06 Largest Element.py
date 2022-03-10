
x = input("Enter Values Separated by Spaces:")
a = x.split()
indexofmax = 0
for i in range(1,len(a)):
    if int(a[i])>int(a[indexofmax]):
     indexofmax = i
print("Largest Value:{}".format(a[indexofmax]))
print("Index of Largest Value:{}".format(indexofmax))    