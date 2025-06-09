class User():
    def __init__(self, name, email_address, drivers_license_number):
        self.name = name
        self.email_address = email_address
        self.drivers_license_number = drivers_license_number
        
user1 = User("dfs", "dasfd@dfs.com", 1343441314341)
user2 = User("dfsfsdaaa", "pjil,j,@dfs.com", 15533449)
user3 = User("dfsaaaaaa", "fjgkhk@dfs.com", 1399998888)

print(user1.name)
print(user1.email_address)
print(user2.name)
print(user2.drivers_license_number)
print(user3.drivers_license_number)