

def add_property(properties, property_id, location, price):
    if property_id not in properties:
        properties[property_id] = {"location": location, "price": price, "status": "available", "inquiries": []}
        print(f"Property ID {property_id} added.")
    else:
        print(f"Property ID {property_id} already exists.")

def update_status(properties, property_id, status):
    if property_id in properties:
        properties[property_id]["status"] = status
        print(f"Property Id {property_id} status updated to {status}.")
    else:
        print(f"Property ID {property_id} not found.")
    
def add_inquiry(properties, property_id, customer_name, inquiry):
    if property_id in properties:
        properties[property_id]["inquiries"].append({"customer": customer_name, "inquiry": inquiry})
        print(f"Inquiry added for Property ID {property_id} by {customer_name}.")
    else:
        print(f"Property ID {property_id} not found. ")


def display_properties(properties):
    for pid, details in properties.items():
        print(f"Property ID: {pid}, Location {details['location']}, Price: {details['price']}")
        for inquiry in details["inquiries"]:
            print(f"  Inquiry by {inquiry['customer']}: {inquiry['inquiry']}")
    


real_estate_properties = {}

while True:
    print("\nReal Estate Management System")
    print("1: Add Property\n2: Update Property Status\n3: Add Inquiry\n4: Display Properties\n5: Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        pid = input("Enter property ID: ")
        loc = input("Enter location: ")
        price = input("Enter price: ")
        add_property(real_estate_properties, pid, loc, price)
    elif choice == '2':
        pid = input("Enter property ID: ")
        status = input("Enter status (available/sold): ")
        update_status(real_estate_properties, pid, status)
    elif choice == '3':
        pid = input("Enter property ID for inquity: ")
        name = input("Enter customer name: ")
        inquiry = input("Enter inquiry details: ")
        add_inquiry(real_estate_properties, pid, name, inquiry)
    elif choice == '4':
        display_properties(real_estate_properties)
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")