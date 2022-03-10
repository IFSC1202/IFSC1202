minindex = 0
maxindex = 0
x= input("Enter Values Seperated by Spaces:")
a = x.split()
for i in range (1,len(a)):
    if int(a[i])>int(a[maxindex]):
        maxindex = i
    if int(a[i])<int(a[minindex]):
        minindex = i
temp = a[minindex] 
a[minindex] = a[maxindex]  
a[maxindex] = temp
print("Swapped Minimum and Maximum:",end="")
for i in range(len(a)):
    print(a[i],sep=" ",end=" ")
print()    
