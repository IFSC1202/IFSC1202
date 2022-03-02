x= int(input("Enter a number(zero to quit):"))
maximum = x
number_of_maximum = 0
while x != 0:
    if x > maximum:
        maximum = x
        number_of_maximum = 1
    elif x == maximum:
         number_of_maximum += 1
    x= int(input("Enter a number(zero to quit):"))
print("Maximum:{}".format(maximum))
print("Number of Occurrences:{}".format(number_of_maximum))

