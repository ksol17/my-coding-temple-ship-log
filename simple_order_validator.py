def validate_order():
    while True:
        try:
            quantity = int(input("Enter the quantity of books you want to order: "))
            if quantity > 0:
                print(f"Thank you! You have ordered {quantity} books.")
                break
            else: 
                print("Invalid quantity. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            






validate_order()
