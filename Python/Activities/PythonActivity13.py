# Function to calculate sum
	
def sum(numbers):
	
	sum = 0
	
	for number in numbers:
	
		sum += number
	
	return sum
	
# List of numbers
	
numList = [10, 40, 60, 90]
	
result = sum(numList)
	
# Result
	
print("Sum of all the numbers is: " + str(result))