s= input("Enter Values separated by Spaces:")
x=s.split()
for i in range(len(x)):
    if int(x[i]) % 2==1:
        print(x[i])