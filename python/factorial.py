#Factorial of a number

def factorial(number):
	if(number < 0):
		return 0
	elif (number == 0 or number == 1):
		return 1
	else:
		return number * factorial(number - 1)

print("Enter the number:")
number = int(input())
print("Factorial is: ", factorial(number))
