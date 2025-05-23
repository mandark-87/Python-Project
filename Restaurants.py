menu = {
    'Pizza': 70,
    'Burger': 50,
    'Noodles': 100,
    'Tomato Soup': 60,
    'Coffee': 40
}

# Greeting
print("________________________________________\n")
print("***** Welcome to Restaurant *****")
print("________________________________________\n")
print("You can order as shown in the below menu\n")

for item, price in menu.items():
    print(f"{item}: {price}")

# Orders
total_order = 0

while True:
    item = input("Enter the name of the item you want to order: ").strip()
    if item in menu:
        total_order += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Your item '{item}' is not available yet.")

    another_order = input("Do you want to order another item? (Yes/No): ").strip().lower()
    if another_order != "yes":
        break

print(f"\nYour total order amount is: {total_order}")
