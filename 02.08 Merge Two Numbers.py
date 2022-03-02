FirstNumber= int(input("Enter First 2 Digit Number: "))
SecondNumber= int(input("Enter Second 2 Digit Number: "))
UnitsDigitFirstNumber= FirstNumber % 10
TensDigitFirstNumber= FirstNumber // 10
UnitsDigitSecondNumber= SecondNumber % 10
TensDigitSecondNumber= SecondNumber // 10
MergedNumber= str(TensDigitFirstNumber) + str(TensDigitSecondNumber) + str(UnitsDigitFirstNumber) + str(UnitsDigitSecondNumber)
print("Merged Number: {}".format(MergedNumber))