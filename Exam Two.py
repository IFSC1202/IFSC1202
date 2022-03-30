open("CarSales.txt","r")
sales_data= []
line= car_sales.readline()
while line:make,
price=line.split(",")
sales_data.append([make,int(price)])
line=car_sales.readline()

