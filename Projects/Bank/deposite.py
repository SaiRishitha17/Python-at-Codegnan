def deposite(account:int, deposite_amount:int):
    users[account]['balance'] += deposite_amount
    return f"{deposite_amount} deposite successful and Current balance is{users[account]['balance']}"
