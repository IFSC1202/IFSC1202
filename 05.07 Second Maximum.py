first_max= int(input("Enter the first number:"))
second_max= int(input("Enter the second number:"))
if first_max < second_max:
    first_max,second_max = second_max,first_max
    x= int(input("Enter a Number(zero to quit):"))
    while x !=0:
        if x > first_max:
            first_max,second_max = second_max,first_max
            first_max = x
        elif x>second_max:
            second_max= x
        x= int(input("Enter a Number(zero to quit:")) 
print("First Maximum:{}".format(first_max)) 
print("Second Maximum:{}".format(second_max))        

