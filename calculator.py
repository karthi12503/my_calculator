number1=int(input("enter the value of first number:"))
number2=int(input("enter the value of second number:"))
print("choose the operation")
print("addition = 1; subtraction = 2; multiplication = 3; division = 4")
operation=int(input("enter the operation:"))

if (operation == 1):
	print("the answer is ",number1+number2)
elif (operation == 2):
	print("the answer is ",number1-number2)
elif (operation == 3):
	print("the answer is ",number1*number2)
elif (operation == 4):
	print("The answer is ",number1/number2)
else:
	print(" Pls enter the correct number")