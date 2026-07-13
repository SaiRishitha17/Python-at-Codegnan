# update_contact.py

from data import contacts

def update_contact():

    contact_id = int(input("Enter Contact ID to update: "))

    if contact_id in contacts:

        print("Enter new details:")

        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")

        contacts[contact_id]["name"] = name
        contacts[contact_id]["phone"] = phone
        contacts[contact_id]["email"] = email
        contacts[contact_id]["address"] = address

        print("Contact updated successfully.")

    else:
        print("Contact not found.")