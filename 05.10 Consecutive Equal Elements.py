chunk = 1
mc = 1
a = int(input('Enter a Number (zero to quit): '))
b = a
while b != 0:
    b, a = int(input('Enter a Number (zero to quit): ')), b
    if b == a:
        chunk += 1
    else:
        if chunk > mc:
            mc = chunk
        chunk = 1
print( '7 repeated ' + str(mc) + ' times.')