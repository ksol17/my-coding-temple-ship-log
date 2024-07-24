class UsernameError(Exception):
    def __init__(self, message):
        self.message = message

def check_username(username):
    if len(username) < 6:
        raise UsernameError("Username must be at least 6 characters long.")

while True:
    username_input = input("Please enter your username: ")
    try:
        check_username(username_input)
        print("Username is valid!")
        break
    except UsernameError:
        print(f"Error: {UsernameError.message}")

    try_again_input = input("Would you like to try a different username? (yes/no): ").lower()
    if try_again_input != 'yes':
        break