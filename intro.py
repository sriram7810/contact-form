contacts = {}

while True:
    print("\nContact Book App")
    print("1. Add new contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("please Enter your choice: ")

#Add contacts
    if choice == "1":
        name = input("Please enter name:  ")
        if name in contacts:
            print(f"contact '{name}' already exists!")
        else:
            mobile = input("please enter mobile number: ")
            email = input("please enter email: ")
            city = input("please enter city: sr ")
            contacts[name] = {"mobile": mobile, "email": email, "city": city}
            print(f"contact '{name} has been successfully added")

#view contacts
    elif choice == "2":
        if contacts:
            print("\n-- All contacts ---")
            for name, info in contacts.items():
                print(f"Name: {name}, Mobile: {info['mobile']}, Email: {info['email']}, city: {info['city']}")
            else:
                print("contact list is empty!")

#Search contacts
    elif choice == "3":
        search_name = input("please enter name to search: ")
        found = False
        for name, info in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found: Name: {name}, Mobile: {info['mobile']}, Email: {info['email']}, city: {info['city']}")
                found = True
            if not found:
                print("No contact found with that name.")

#Delete contact
    elif choice == "4":
        name = input("please enter name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"contact '{name} deleted successfully!")
        else:
            print("contact not found.")

#Exit
    elif choice == "5":
        print("Exiting.. Good Bye!")
        break

    else:
        print("Invalid input. Please enter a valid choice.")
        