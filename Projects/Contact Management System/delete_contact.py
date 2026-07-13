# delete_contact.py

from data import contacts

def delete_contact():

    contact_id = int(input("Enter Contact ID to delete: "))

    if contact_id in contacts:

        del contacts[contact_id]

        print("Contact deleted successfully.")

    else:
        print("Contact not found.")