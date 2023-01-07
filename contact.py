import re


def main():
    menu()
    while True:
        user_input = input("Enter: ")
        if user_input == "5":
            print("Bye!, Thankyou for using this system")
            break
        elif user_input == "1":
            view_contacts()
        elif user_input == "2":
            add_contact()
        elif user_input == "3":
            delete_contact()
        elif user_input == "4":
            search_contact()
        else:
            print("Invalid Input please select from the options given!")


def view_contacts():
    with open("contacts.txt") as file:
        lines = file.read().split()
        every_3rd = lines[::3]
        for i, name in enumerate(every_3rd):
            print(i + 1, name)


def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")
    with open("contacts.txt", "a") as file:
        file.write("\n")
        file.write(f"{name} {number} {email}")
        print(name + " was added to the contacts")


def delete_contact():
    number = input("Enter number to delete: ")
    with open("contacts.txt") as file:
        lines = file.readlines()
        for line in lines:
            if number in line:
                lines.remove(line)
        with open('contacts.txt', 'w') as file:
            for line in lines:
                file.write(line)


def search_contact():
    search = input("Enter number keyword to search: ")
    with open("contacts.txt") as file:
        lines = file.readlines()
        for line in lines:
            if re.search((r'\d+'), search, re.IGNORECASE):
                print(line.strip())
            else:
                print("No matches found")
                break


def menu():
    print("""
                  Welcome to the Contact Management System
                  1. view all contacts
                  2. add a contact
                  3. delete a contact
                  4. search for a contact
                  5. exit the program
                  """)


if __name__ == "__main__":
    main()
