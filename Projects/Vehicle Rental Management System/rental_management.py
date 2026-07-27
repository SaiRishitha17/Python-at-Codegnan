from file_handling import append_data, read_data, write_data


# Function to rent a vehicle
def rent_vehicle():

    user_id = input("Enter Customer ID: ").strip()

    vehicle_id = input("Enter Vehicle ID to rent: ").strip()

    days = int(input("Enter Number of Days: "))


    vehicles = read_data("vehicles.csv")


    for vehicle in vehicles:

        if vehicle["vehicle_id"] == vehicle_id:

            if vehicle["availability"].capitalize() == "Available":

                rental_price = int(vehicle["rental_price"])

                total_amount = rental_price * days


                rental_data = {
                    "user_id": user_id,
                    "vehicle_id": vehicle_id,
                    "days": days,
                    "total_amount": total_amount
                }


                # Store rental details
                append_data("rentals.csv", rental_data)


                # Update vehicle availability
                vehicle["availability"] = "Rented"


                # Save updated vehicle data
                write_data(
                    "vehicles.csv",
                    vehicles,
                    vehicles[0].keys()
                )


                print("Vehicle rented successfully")
                print("Total Rent:", total_amount)

                return


            else:
                print("Vehicle is not available")
                return


    print("Vehicle not found")



# Function to view rental history
def view_rentals():

    rentals = read_data("rentals.csv")


    if not rentals:
        print("No rental records found.")
        return


    print("\n------ Rental History ------")


    for rental in rentals:

        print("Customer ID:", rental["user_id"])
        print("Vehicle ID:", rental["vehicle_id"])
        print("Days:", rental["days"])
        print("Total Amount:", rental["total_amount"])
        print("----------------------------")



# Function to return a vehicle
def return_vehicle():

    vehicle_id = input("Enter Vehicle ID to return: ").strip()


    vehicles = read_data("vehicles.csv")


    for vehicle in vehicles:

        if vehicle["vehicle_id"] == vehicle_id:


            if vehicle["availability"].capitalize() == "Rented":

                vehicle["availability"] = "Available"


                write_data(
                    "vehicles.csv",
                    vehicles,
                    vehicles[0].keys()
                )


                print("Vehicle returned successfully")
                return


            else:

                print("Vehicle is already available")
                return


    print("Vehicle not found")