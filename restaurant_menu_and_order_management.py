
def add_category(menu, category):
    if category not in menu:
        menu[category] = []
        print(f"Category '{category}' added.")
    else:
        print(f"Category '{category}' already exists.")


def add_item(menu, category, item):
    if category in menu:
        if item not in menu[category]:
            menu[category].append(item)
            print(f"Item '{item}' added to '{category}'.")
        else:
            print(f"Item '{item}' already exists in '{category}'.")
    else:
        print(f"Category '{category}' does not exist.")

def take_order(menu, order):
    try:
        order_items = [menu[category][item_index] for category, item_index in order]
        return order_items
    except (KeyError, IndexError):
        print("Invalid order. Please check menu and order again.")
        return None
    

def display_menu(menu):
     for category, items in menu.items():
         print(f"{category}: {', '.join(items)}")


restaurant_menu = {
    "Starters":["Soup", "Salad"],
    "Main Course":["Steak", "Salmon", "Pasta"],
    "Deserts":["Cake", "Ice Cream"]
}


add_category(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Water")
customer_order = [("Main Course", 1), ("Desserts", 2)]
order_items = take_order(restaurant_menu, customer_order)
if order_items:
    print("Customer order:", order_items)
display_menu(restaurant_menu)