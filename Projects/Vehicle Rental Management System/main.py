from vehicle_management import (
    add_vehicle,
    view_vehicles,
    search_vehicle,
    update_vehicle,
    delete_vehicle
)

from user_management import (
    register_customer,
    create_admin,
    login
)

from rental_management import (
    rent_vehicle,
    view_rentals,
    return_vehicle
)


def main():

    while True:

        print("\n====== Vehicle Rental Management System ======")

        print("\n--- Vehicle Management ---")
        print("1. Add Vehicle")
        print("2. View Vehicles")
        print("3. Search Vehicle")
        print("4. Update Vehicle")
        print("5. Delete Vehicle")

        print("\n--- User Management ---")
        print("6. Register Customer")
        print("7. Create Admin")
        print("8. Login")

        print("\n--- Rental Management ---")
        print("9. Rent Vehicle")
        print("10. View Rentals")
        print("11. Return Vehicle")

        print("\n0. Exit")


        choice = input("\nEnter your choice: ")


        # Vehicle Management

        if choice == "1":
            add_vehicle()

        elif choice == "2":
            view_vehicles()

        elif choice == "3":
            search_vehicle()

        elif choice == "4":
            update_vehicle()

        elif choice == "5":
            delete_vehicle()


        # User Management

        elif choice == "6":
            register_customer()

        elif choice == "7":
            create_admin()

        elif choice == "8":
            login()


        # Rental Management

        elif choice == "9":
            rent_vehicle()

        elif choice == "10":
            view_rentals()

        elif choice == "11":
            return_vehicle()


        elif choice == "0":
            print("Thank you for using Vehicle Rental Management System")
            break


        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()