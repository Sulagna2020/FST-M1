	
fruit_shop = {
	
    "strawberry": 20,
	
    "apple": 25,
	
    "orange": 19,
	
    "blueberry": 0
	
}
	
key_to_check = input("Which fruit do you need? ").lower()
	
if(key_to_check in fruit_shop):
	
    print("I have that")
	
else:
	
    print("I dont have that")