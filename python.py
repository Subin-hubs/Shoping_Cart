# Initialize an empty list to store the shopping list items
shopping_list = []

# Function to add an item to the shopping list
def add_item(item):
    shopping_list.append(item)
    print(f"Added {item} to the shopping list.")

# Function to view the shopping list
def view_list():
    if shopping_list:
        print("\nShopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        print()  # Blank line for better readability
    else:
        print("\nYour shopping list is empty.\n")

# Function to remove an item from the shopping list
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the shopping list.")
    else:
        print(f"{item} not found in the shopping list.")

# Main loop to interact with the user
while True:
    print("\nOptions:")
    print("1. Add an item")
    print("2. View the list")
    print("3. Remove an item")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == "2":
        view_list()
    elif choice == "3":
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
        break
