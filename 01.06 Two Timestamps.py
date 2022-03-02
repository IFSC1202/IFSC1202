hours1= int(input(" Enter hours: "))
minutes1= int(input("Enter minutes: "))
seconds1= int(input("Enter seconds: "))
print("First timestamp")
hours2= int(input("Enter hours: "))
minutes2= int(input("Enter minutes: "))
seconds2= int(input("Enter seconds: "))
print("second stamp")
totalseconds1= (hours1*3600) + (minutes1*60)+ seconds1
totalseconds2= (hours2*3600) + (minutes2*60) + seconds2
difference= totalseconds2- totalseconds1
print(difference)