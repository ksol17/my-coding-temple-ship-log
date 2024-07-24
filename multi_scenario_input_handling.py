# Promt the user to enter their age.
# Use a 'try-except' block to handle the following scenarios:
# The input is not a number ('ValueError')
# the number is not within the range of 0 to 120 ('ValueError').
# If an exception is raised, provide a specific error message for the type of exception and ask for the input again. 
# If the input is valid, print a confirmation message.

while True:
    try:
        user_age = input("Enter your age: ")
        age = int(user_age)
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120")
    except ValueError as ve:
        if "invalid literal" in str(ve):
            print("That's not a number. Please enter your age using digits.")
        else:
            print(ve)
    else:
        print(f"Thank you. Your age is recorded as {age}.")
        break
