a=int(input("Enter a 3 Digit Number: "))
unitsdigit= a % 10
a= a // 10
tensdigit= a % 10
a= a // 10
hundredsdigit= a
reverse= str(unitsdigit) + str(tensdigit) + str(hundredsdigit)
print("Reverse of Digits: {}".format(reverse))

