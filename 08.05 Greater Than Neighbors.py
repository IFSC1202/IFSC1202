s= input("Enter Values Separated by Values:")
x= s.split()
for i in range (1,len(x)):
    if int(x[i]) > int(x[i-1]):
        print(x[i])