#10/Feb/2023

#Database
db = [] 

#CRUD
def createAccount(account):
    db.append((account.getUsername(), account.getPassword()))

def readAccounts():
    pass

def updateAccount():
    pass

def deleteAccount():
    pass

#Classes
class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def setUsername(self, username):
        self.username = username

    def getUsername(self): 
        return self.username
    
    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password