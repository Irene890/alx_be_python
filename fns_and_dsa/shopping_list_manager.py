# # Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items
# # Implement functionality to add items to the list, remove items, and display the current list.
# # Use a loop to continuously display a menu with options to the user until they choose to exit. The menu should offer options to add an item, remove an item, view the list, and exit.
# # For adding items, prompt the user for the item name and append it to shopping_list.
# # For removing items, ask the user for the item name and remove it from shopping_list. If the item is not found, display a message indicating so.
# # To view the list, print each item in shopping_list to the console.
# # Ensure your script handles invalid menu choices gracefully.

def display_menu():
    print("\nShopping List Manager")
    print("1. Add the Item")
    print("2. Remove the Item")
    print("3. View the List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice(1,2,3 or 4): ").strip()

        if choice == '1':
            add_item = input("Enter the item to add: ").strip().title()
            if add_item:
                shopping_list.append(add_item)
                print(f"'{add_item}' has been added to the list")
            else:
                print("Please, item cannot be empty.")

        elif choice == '2':
            remove_item = input("Enter the item to remove from shopping list: ").strip().title()
            try:
                shopping_list.remove(remove_item)
                print(f"'{remove_item}' has been removed from the list")
            except ValueError:
                print(f"{remove_item} is not in the list")
        elif choice == '3':
            if shopping_list:
                for index, add_item in enumerate(shopping_list, 1):
                    print(f"{index}. {add_item}")
            else:
                print("The shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":