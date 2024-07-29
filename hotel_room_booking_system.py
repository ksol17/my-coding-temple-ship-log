def add_room(hotel, room_number):
    if room_number not in hotel:
        hotel[room_number] = True  # True indicates the room is available
        print(f"Room {room_number} added.")
    else:
        print(f"Room {room_number} already exists.")

def is_available(hotel, room_number):
    return hotel.get(room_number ,False)

def book_room(hotel, room_number):
    if is_available(hotel, room_number):
        hotel[room_number] = False
        print(f"Room {room_number} booked.")
    else:
        print(f"Room {room_number} is not available or does not exist.")

def display_rooms(hotel):
    for room, available in hotel.items():
        status = "Available" if available else "Booked"
        print(f"Room {room}: {status}")

hotel_rooms = {"101": True, "102": False, "103": True}

while True: 
    print("\nHotel Management System")
    print("1: Add Room\n2: Book Room\n3: Check Room Availability\4: Display Rooms\n5: Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        room = input("Enter room number to add: ")
        add_room(hotel_rooms, room)
    elif choice == "2":
        room = input("Enter room number to book: ")
        book_room(hotel_rooms, room)
    elif choice == "3":
        room = input("Enter room number to check availability: ")
        available = is_available(hotel_rooms, room)
        print(f"Room {room} is {'available' if available else 'not available'}.")
    elif choice == "4":
        display_rooms(hotel_rooms)
    elif choice == "5":
        print("Exciting system.")
        break
    else:
        print("Invalid choice. Please try again.")