numdistinct = 1
x = input("Enter Values Separated by Spaces:")
a = x.split()
for i in range(0,len(a)-1):
    if int(a[i]) != int(a[i+1]):
        numdistinct += 1
print("Number of Distinct Elements:{}".format(numdistinct))        