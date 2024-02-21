class Client:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
    
    def __str__(self):
        return ("You are " +self.name +"with email "+self.email)


client1=Client("Mina","mina_gh@yahoo.com",22252193)
print(client1)
client2=Client("Mitra","m@gh@yahoo.com","22234564")
print(client2)

#Add child class
class VipClient(Client):
    def __init__(self,name,email,phone,vipNumber):
        Client.__init__(self,name,email,phone)
        self.vipNumber=vipNumber
    def vipcode(self):
        return (self.vipNumber)
    
vip1=VipClient("Jack","mf@yahoo.com",22245329,1562)
print(vip1)
print(vip1.vipcode())