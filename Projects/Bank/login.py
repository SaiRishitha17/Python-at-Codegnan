def login(account:int, password:str)->bool:
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False