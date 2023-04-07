#Activty 21 acitvity 22

import pytest

# Additon test
def test_addition():
	
    # Initialize two numbers
	num1 = 10
	num2 = 20
    
	# Add them
	sum = num1 + num2

	# Assertion
	assert sum == 30

# Subtraction test
def test_subtraction():
  
	# Initialize two numbers
	num1 = 100
	num2 = 50
    
	# Subtract them
	diff = num1 - num2

	# Assertion
	assert diff == 50

# Multiplication test
@pytest.mark.activity
def test_multiplication():
  
	# Initialize two numbers
	num1 = 35
	num2 = 2
    
	# Multiply them
	prod = num1 * num2

	# Assertion
	assert prod == 70

# Division test
	
@pytest.mark.activity
def test_division():
  
	# Initialize two numbers
	num1 = 160
	num2 = 4
    
	# Divide them
	quot = 160/4

	# Assertion
	assert quot == 40
