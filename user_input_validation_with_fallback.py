# Create a list of fruit that are allowed inputs.
# Prompt the user to enter their favorite fruit.
# Use a 'try-except-else' block to validate the input.
# If the input is not in the list, raise a 'ValueError' and handle it by asking for input again.
# If the input is valid, print a confirmation message. 

allowed_fruits= ['apple', 'banana', 'cherry', 'date', 'elderberry']

while True:
    try:
        favorite_fruit = input("Enter your favorite fruit: ").lower()
        if favorite_fruit not in allowed_fruits:
            raise ValueError("Fruit not allowed in the list.")
    except ValueError as ve:
        print(ve)
        print("Please choose a fruit from the list.")
    else:
        print(f"Great choice! Your favorite fruit is {favorite_fruit}.")
        break