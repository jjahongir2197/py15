inventory = {}

def add_item(name, qty):
    if name in inventory:
        inventory[name] += qty
    else:
        inventory[name] = qty

def remove_item(name, qty):
    if name in inventory:
        inventory[name] -= qty
        if inventory[name] <= 0:
            del inventory[name]

def show_inventory():
    for item in inventory:
        print(item, ":", inventory[item])


add_item("Pen", 10)
add_item("Book", 5)

remove_item("Pen", 3)

show_inventory()
