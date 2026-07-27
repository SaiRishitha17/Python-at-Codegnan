from file_handling import write_data


vehicles = [
    {
        "vehicle_id": "c101",
        "vehicle_type": "Car",
        "brand": "Honda",
        "model": "City",
        "rental_price": "1800",
        "availability": "Available"
    },
    {
        "vehicle_id": "c102",
        "vehicle_type": "Car",
        "brand": "Toyota",
        "model": "Camry",
        "rental_price": "2000",
        "availability": "Available"
    },
    {
        "vehicle_id": "c103",
        "vehicle_type": "Car",
        "brand": "Hyundai",
        "model": "Creta",
        "rental_price": "2200",
        "availability": "Available"
    },
    {
        "vehicle_id": "c104",
        "vehicle_type": "Car",
        "brand": "Maruti",
        "model": "Baleno",
        "rental_price": "1500",
        "availability": "Available"
    },
    {
        "vehicle_id": "c105",
        "vehicle_type": "Car",
        "brand": "Tata",
        "model": "Nexon",
        "rental_price": "1900",
        "availability": "Available"
    },
    {
        "vehicle_id": "b101",
        "vehicle_type": "Bike",
        "brand": "Yamaha",
        "model": "R15",
        "rental_price": "800",
        "availability": "Available"
    },
    {
        "vehicle_id": "b102",
        "vehicle_type": "Bike",
        "brand": "Royal Enfield",
        "model": "Classic 350",
        "rental_price": "1000",
        "availability": "Available"
    },
    {
        "vehicle_id": "b103",
        "vehicle_type": "Bike",
        "brand": "Honda",
        "model": "Activa",
        "rental_price": "600",
        "availability": "Available"
    },
    {
        "vehicle_id": "t101",
        "vehicle_type": "Truck",
        "brand": "Tata",
        "model": "Ultra",
        "rental_price": "3000",
        "availability": "Available"
    },
    {
        "vehicle_id": "t102",
        "vehicle_type": "Truck",
        "brand": "Ashok Leyland",
        "model": "Dost",
        "rental_price": "3500",
        "availability": "Available"
    }
]


write_data(
    "vehicles.csv",
    vehicles,
    vehicles[0].keys()
)


print("Vehicle data loaded successfully")