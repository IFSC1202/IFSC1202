
n = int(input("Enter the size of the snowflake:"))
a = []
for i in range(n):
    a.append([' '] * n)

for i in range(n):

	a[i][i] = '*'

	a[n // 2][i] = '*'

	a[i][n // 2] = '*'
	
	a[i][n - i - 1] = '*'

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
