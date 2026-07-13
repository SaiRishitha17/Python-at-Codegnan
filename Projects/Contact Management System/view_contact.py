# view_contact.py

from data import contacts

def view_contact():

    if not contacts:
        print("No contacts available.")
        return

    print("\n===== CONTACT LIST =====")

    for contact_id, details in contacts.items():

        print(f"\nContact ID : {contact_id}")
        print(f"Name       : {details['name']}")
        print(f"Phone      : {details['phone']}")
        print(f"Email      : {details['email']}")
        print(f"Address    : {details['address']}")
        print("-" * 30)