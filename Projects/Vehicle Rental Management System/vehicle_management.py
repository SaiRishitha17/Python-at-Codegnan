from file_handling import append_data
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
    vehicle_type = input("Enter Vehicle Type (Car/Bike/Truck): ")
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