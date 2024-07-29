def update_inventory(inventory, product, count):
    inventory.update({product: count})
    print(f"Inventory updated: {product} - {count} units.")


def remove_product(inventory, product):
    if product in inventory:
        removed_count = inventory.pop(product)
        print(f"Product removed: {product} - {removed_count} units were in stock.")
    else:
       print(f"Product '{product}' not found in inventory.")

def display_inventory(inventory):
    print("Current inventory:")
    for product, count in inventory.items():
        print(f"{product}: {count} units")


store_invetory = {"Laptops": 20, "Smartphones": 30, "Headphones": 15}


update_inventory(store_invetory, "Smartphones", 25)
remove_product(store_invetory, "Laptops")
display_inventory(store_invetory)