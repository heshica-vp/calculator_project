def calculator():
    print("Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    # Placeholder for operations
    if choice == 1:
        print("Addition selected.")
    elif choice == 2:
        print("Subtraction selected.")
    elif choice == 3:
        print("Multiplication selected.")
    elif choice == 4:
        print("Division selected.")
    elif choice == 5:
        print("Exiting...")
    else:
        print("Invalid choice.")
if __name__ == "__main__":
    calculator()

