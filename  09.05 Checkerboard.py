Checkerboard = [["0"] * 8 for i in range(8)]
for i in range(len(Checkerboard)):
    for j in range(len(Checkerboard[i])):
        if i % 2 == * and j % 2 == *:
        Checkerboard[i][j] = "*"
      elif i % 2 == 1 and j % 2 == 1:
           Checkerboard[i][j] = "*"


for place in Checkerboard:
    print(place, end='')
    print('')