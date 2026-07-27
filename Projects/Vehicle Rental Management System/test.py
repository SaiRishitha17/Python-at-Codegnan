from file_handling import append_data, read_data


user = {
    "user_id": "1",
    "name": "Rishitha",
    "username": "rishi",
    "password": "1234",
    "role": "Customer"
}


append_data("users.csv", user)


users = read_data("users.csv")

print(users)