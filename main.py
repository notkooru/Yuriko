#10/Feb/2023
import json
#Database
db = [] 

#CRUD
def create_account(account):
    db.append((account.get_username(), account.get_password()))

def read_accounts():
    counter = 0
    for account in db:
        print(counter, account[0], account[1])
        counter+=1

def update_account():
    pass

def delete_account(id):
   db.pop(int(id)) 

#Classes
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def set_username(self, username):
        self.username = username

    def get_username(self): 
        return self.username
    
    def set_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password