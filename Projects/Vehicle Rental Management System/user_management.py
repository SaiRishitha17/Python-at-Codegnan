from file_handling import append_data, read_data
class User:
    def __init__(self, user_id, name, username, password, role):
        self.user_id = user_id
        self.name = name
        self.username = username
        self.__password = password   # Encapsulation
        self.role = role
    def check_password(self, password):
        return self.__password == password
class Admin(User):
    def __init__(self, user_id, name, username, password):
        super().__init__(
            user_id,
            name,
            username,
            password,
            "Admin"
        )
class Customer(User):
    def __init__(self, user_id, name, username, password):
        super().__init__(
            user_id,
            name,
            username,
            password,
            "Customer"
        )

# Function for registering a new customer
def register_customer():
    # Taking customer details as input
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    # Creating a Customer object
    # Customer automatically gets role = Customer
    customer = Customer(
        user_id,
        name,
        username,
        password
    )
    # Converting object data into dictionary format
    # because CSV stores data in rows and columns
    customer_data = {
        "user_id": customer.user_id,
        "name": customer.name,
        "username": customer.username,
        "password": password,
        "role": customer.role
    }
    # Saving customer details into users.csv
    # append_data() is imported from file_handling.py
    append_data("users.csv", customer_data)

    print("Customer registration successful")
# Function for user login
def login():
    # Taking username and password from user
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    # Reading user details from users.csv
    users = read_data("users.csv")
    # Checking entered details with stored user details
    for user in users:
        if user["username"] == username and user["password"] == password:
            print("Login successful")
            print("Welcome", user["name"])
            print("Role:", user["role"])
            return user
    # If username or password does not match
    print("Invalid username or password")
    return None


# Function for creating an admin user
def create_admin():
    # Taking admin details as input
    user_id = input("Enter Admin ID: ")
    name = input("Enter Admin Name: ")
    username = input("Enter Admin Username: ")
    password = input("Enter Admin Password: ")
    # Creating an Admin object
    # Admin automatically gets role = Admin
    admin = Admin(
        user_id,
        name,
        username,
        password
    )
    # Converting admin object data into dictionary format
    # because CSV stores data in rows and columns
    admin_data = {
        "user_id": admin.user_id,
        "name": admin.name,
        "username": admin.username,
        "password": password,
        "role": admin.role
    }
    # Saving admin details into users.csv
    append_data("users.csv", admin_data)
    print("Admin created successfully")
