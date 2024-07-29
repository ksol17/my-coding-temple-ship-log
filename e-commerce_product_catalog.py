def add_category(catalog, category):
    if category not in catalog:
        catalog[category] = []
        print(f"Category '{category}' added.")
    else:
        print(f"Category '{category}' already exists.")


def add_product(catalog, category, product):
    try:
        if product not in catalog[category]:
            catalog[category].append(product)
            print(f"Product '{product}' added to {category}'.")
        else:
            print(f"Product '{product}' already exists in '{category}'.")
    except KeyError:
        print(f"Category '{category}' does not exist.")

def display_categories(catalog):
    for category, products in catalog.items():
        print(f"{category}: {', '.join(products)}")

def search_product(catalog, product):
    found = False
    for category, products in catalog.items():
        if product.lower() in [p.lower() for p in products]:
            print(f"Product '{product}' found in '{category}'.")
            found = True
            break
    if not found:
        print(f"Product '{product}' not found.")


catalog = {
    "Electronics": ["Laptop", "Smartphones"],
    "Books": ["Fiction", "Non-Fiction"]
}

add_category(catalog, "Clothing")
add_product(catalog, "Electronics", "Camera")
display_categories(catalog)
search_product(catalog, "laptop")
#print(catalog)