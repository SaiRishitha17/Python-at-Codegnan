# add_contact.py

from data import contacts

def add_contact():

    contact_id = max(contacts.keys(), default=0) + 1

    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts[contact_id] = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    print("Contact added successfully.")