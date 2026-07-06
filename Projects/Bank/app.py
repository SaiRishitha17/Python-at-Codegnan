#user table
users = {
    1234:{'name':"Rishitha", 'email':"rishithamarvathu@gmail.com", 'balance':5000, 'password':"1234"},
    1235:{'name':"priya", 'email':"priyapittala12@gmail.com", 'balance':55000, 'password':"12345"}
    }

#services
def register(name:str, email:str,initial_deposite:int, password:str):
    pass

def login(account:int, password:str)->bool:
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False

#balance function defination
def balance(account:int)->int:
    curr_amount = users[account]['balance']
    return curr_amount
#withdraw function defination
def withdraw(account:int,withdraw_amount:int)->str:
    curr_amount = users[account]['balance']
    #check amount
    if curr_amount >= withdraw_amount:
        users[account]['balance'] -= withdraw_amount
        return f"{withdraw_amount} withdrawl successful and Current balance is{users[account]['balance']}"
    return "Insufficient balance"
#deposite function defination
def deposite(account:int, deposite_amount:int):
    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite successful and Current balance is{users[account]['balance']}"
#transfer function defination
def transfer(sender:int, reciever:int,transfer_amount:int):
    if reciever in users:
        curr_amount = users[sender]['balance']
        if curr_amount >= transfer_amount:
            users[sender]['balance'] -= transfer_amount
            users[reciever]['balance'] += transfer_amount
            return f"{transfer_amount} Transfer successful and current balance is {users[sender]['balance']}"
        return "Insufficient Balance"
    return "Reciever account not found"
#ministatement Function Defination
def ministatement(account:int):
    return "Ministatement under development process"
#logout function defination
def logout():
    return "Thank you for using Large Scale Bank servieces, Bye Bye..."

# main
if __name__== "__main__":

    print("Welcome to the Large Scale Bank")
    print("1. Register \n 2.Login")
    choice = int(input("Select Your choice:"))

    # calling register function
    if choice == 1:
        print("Registration Page under development process....")
    #calling Login Function
    elif choice == 2:
        account = int(input("Enter Your account number:"))
        password = input("Enter your password:")
        login_val = login(account=account, password=password)

        while True:
            print("The Large Scale Bank providing services")
            print("1. Balance \n 2. Withdraw \n 3. Deposite \n\
                   4. Transfer \n 5. Ministatement \n 6. Logout")
            choice = int(input("Enter your choice(1-6):"))

            if choice == 1:
                #call balance function
                current_balance = balance(account=account)
                print(f"Current balance is:{current_balance}")
            elif choice == 2:
                amount = int(input("Enter your withdraw amount:"))
                #call withdraw function
                res = withdraw(account=account, withdraw_amount=amount)
                print(res)
            elif choice == 3:
                #call deposite function
                amount = int(input("Enter your deposite amount"))
                #call withdraw function
                res = deposite(account=account, deposite_amount=amount)
                print(res)
            elif choice == 4:
                #call transfer function
                reciever_account = int(input("Enter your recievers account number"))
                amount = int(input("Enter your transfer amount:"))
                res = transfer(sender=account, reciever=reciever_account, transfer_amount=amount)
                print(res)
            elif choice == 5:
                # call ministatement
                # amount = int(input("Enter your withdraw amount:"))
                res = ministatement(account=account)
                print(res)
            elif choice == 6:
                #call logout function
                print(logout())
                exit()
            else:
                print("Invalid choice,select option in betweeen 1 to 6")
        print("invalid login credentials")
    else:
        print("invalid choice,select option in between 1 and 2")


                

