	
# Enter the list of numbers
	
numList = list(input("Enter list of the numbers separated by comma:").split(",")) 
	
print("Given list is ", numList)
	
	
# Get first element in list
	
firstElement = numList[0]
print("The first number is:", firstElement)	
# Get last element in list
	
lastElement = numList[-1]
print("The last number is:", lastElement)	
 
	
# Check if first and last element are equal
	
if (firstElement == lastElement):
	
    print(True)
	
else:
	
    print(False)