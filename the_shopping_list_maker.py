# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.


def add_items(items):
    for count, item in enumerate(items, start = 1):
        print (f"Item {count} in cart: {str.capitalize(item)}")

def total_list(items):
    shopping_list = []
    while True:
        users_choice = input("Do you want to [A]dd, [R]emove, [V]iew, or [E]xit? ").upper()
        if users_choice == "E":
            break
        elif users_choice == "A":
            num_of_items = int(input("How many items do you want to add? "))
            for i in range(num_of_items):
                items_to_add = input(f"What items would you like to put in the cart?  ({i+1}): ")
                shopping_list.append(items_to_add)
        elif users_choice == "R":
            num_of_items = int(input("How many items do you want to remove? "))
            for i in range(num_of_items):
                items_to_remove = input(f"What items would you like to remove? ({i+1}): ")
                shopping_list.remove(items_to_remove)
        elif users_choice == "V":
            add_items(shopping_list)
        else:
            print("Invalid input!")

    print("Your shopping list: ")
    add_items(shopping_list)

while True:
    user_input = input("Are you ready to start making your list? [Y/N]").upper()
    if user_input == "Y":
        total_list([])
    elif user_input == "N":
        print("Thank you! Come again!")
        break
    else:
        print("Invalid input!")