# app.py

from add_contact import add_contact
from view_contact import view_contact
from update_contact import update_contact
from delete_contact import delete_contact

print("***** CONTACT MANAGEMENT SYSTEM *****")

while True:

    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        add_contact()

    elif choice == 2:
        view_contact()

    elif choice == 3:
        update_contact()

    elif choice == 4:
        delete_contact()

    elif choice == 5:
        print("Thank you for using Contact Management System.")
        break

    else:
        print("Invalid Choice. Please select between 1 and 5.")