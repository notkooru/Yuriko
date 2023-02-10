#10/Feb/2023

class Account:
    def setUsername(self, username):
        self.username = username

    def getUsername(self): 
        return self.username
    
    def setPassword(self, password):
        self.password = password
    
    def getPassword(self):
        return self.password

test = Account()

test.setPassword("123")
test.setUsername("username")
print(test.getUsername())
print(test.getPassword())
test.setUsername("desolacion")
print(test.getUsername())