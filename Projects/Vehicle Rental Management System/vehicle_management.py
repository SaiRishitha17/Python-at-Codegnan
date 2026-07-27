from file_handling import append_data, read_data, write_data
class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price, availability):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.__rental_price = rental_price   # Encapsulation
        self.availability = availability
    def get_rental_price(self):
        return self.__rental_price

class Car(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price, availability):
        super().__init__(
            vehicle_id,
            brand,
            model,
            rental_price,
            availability
        )
     # Polymorphism
    def calculate_rent(self, days):
        return self.get_rental_price() * days
class Bike(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price, availability):
        super().__init__(
            vehicle_id,
            brand,
            model,
            rental_price,
            availability
        )
    # Polymorphism
    def calculate_rent(self, days):
        return self.get_rental_price() * days

class Truck(Vehicle):

    def __init__(self, vehicle_id, brand, model, rental_price, availability):
        super().__init__(
            vehicle_id,
            brand,
            model,
            rental_price,
            availability
        )
     # Polymorphism
    def calculate_rent(self, days):
        return self.get_rental_price() * days

def add_vehicle():

    # Taking vehicle details from admin
    vehicle_id = input("Enter Vehicle ID: ")
    vehicle_type = input("Enter Vehicle Type (Car/Bike/Truck): ").capitalize()
    brand = input("Enter Brand: ")
    model = input("Enter Model: ")
    rental_price = int(input("Enter Rental Price: "))
    availability = "Available"


    # Creating object based on vehicle type
    if vehicle_type == "Car":

        vehicle = Car(
            vehicle_id,
            brand,
            model,
            rental_price,
            availability
        )

    elif vehicle_type == "Bike":

        vehicle = Bike(
            vehicle_id,
            brand,
            model,
            rental_price,
            availability
        )

    elif vehicle_type == "Truck":

        vehicle = Truck(
            vehicle_id,
            brand,
            model,
            rental_price,
            availability
        )

    else:
        print("Invalid vehicle type")
        return


    # Converting object data into dictionary
    vehicle_data = {
        "vehicle_id": vehicle.vehicle_id,
        "vehicle_type": vehicle_type,
        "brand": vehicle.brand,
        "model": vehicle.model,
        "rental_price": vehicle.get_rental_price(),
        "availability": vehicle.availability
    }


    # Saving vehicle details into vehicles.csv
    append_data("vehicles.csv", vehicle_data)

    print("Vehicle added successfully")

# Function to display all vehicles
def view_vehicles():

    # Read all vehicle records from vehicles.csv
    vehicles = read_data("vehicles.csv")

    # If there are no vehicles
    if not vehicles:
        print("No vehicles available.")
        return

    print("\n------ Vehicle List ------")

    # Display each vehicle
    for vehicle in vehicles:
        print("Vehicle ID:", vehicle["vehicle_id"])
        print("Vehicle Type:", vehicle["vehicle_type"])
        print("Brand:", vehicle["brand"])
        print("Model:", vehicle["model"])
        print("Rental Price:", vehicle["rental_price"])
        print("Availability:", vehicle["availability"])
        print("--------------------------")
# Function to search a vehicle by vehicle ID
def search_vehicle():

    vehicle_id = input("Enter Vehicle ID to search: ")

    vehicles = read_data("vehicles.csv")

    for vehicle in vehicles:

        if vehicle["vehicle_id"] == vehicle_id:

            print("\nVehicle Found")
            print("Vehicle ID:", vehicle["vehicle_id"])
            print("Vehicle Type:", vehicle["vehicle_type"])
            print("Brand:", vehicle["brand"])
            print("Model:", vehicle["model"])
            print("Rental Price:", vehicle["rental_price"])
            print("Availability:", vehicle["availability"])
            return

    print("Vehicle not found")

# Function to update vehicle details
def update_vehicle():

    vehicle_id = input("Enter Vehicle ID to update: ")

    vehicles = read_data("vehicles.csv")

    for vehicle in vehicles:

        if vehicle["vehicle_id"] == vehicle_id:

            print("Vehicle found")

            vehicle["brand"] = input("Enter New Brand: ")
            vehicle["model"] = input("Enter New Model: ")
            vehicle["rental_price"] = input("Enter New Rental Price: ")
            vehicle["availability"] = input("Enter Availability: ")

            write_data(
                "vehicles.csv",
                vehicles,
                vehicles[0].keys()
            )

            print("Vehicle updated successfully")
            return

    print("Vehicle not found")


# Function to delete a vehicle
def delete_vehicle():

    vehicle_id = input("Enter Vehicle ID to delete: ")

    vehicles = read_data("vehicles.csv")

    updated_vehicles = []

    for vehicle in vehicles:

        if vehicle["vehicle_id"] != vehicle_id:
            updated_vehicles.append(vehicle)

    if len(updated_vehicles) == len(vehicles):

        print("Vehicle not found")

    else:

        write_data(
            "vehicles.csv",
            updated_vehicles,
            updated_vehicles[0].keys()
        )

        print("Vehicle deleted successfully")