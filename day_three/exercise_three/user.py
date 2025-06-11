from random import randint

class User():
    list_of_ids = []

    @classmethod
    def append_list_of_ids(cls, new_id):
        cls.list_of_ids.append(new_id)

    def __init__(self, name, email, password, id):
        self.name = name
        self.email = email
        self.password = password
        self.id = id
        self.list_of_ids(self.id)
    
    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, new_name):
        if new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Name can only contain letters")
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        if '@' in new_email and new_email.endswith(".com"):
            self._email = new_email
        else:
            raise ValueError("Please enter email in correct format")
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, new_password):
        if 5 < len(new_password) < 20 and len(new_password).isalnum():
            self._password = new_password
        else:
            raise ValueError("Password length (5-20) and only alnum")
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        if new_id.isalnum() and new_id not in User.list_of_ids:
            self._id = new_id
        else:
            raise ValueError("ID is not in proper format")

    def make_post(self, post):
        print(f"{self.name} made a post: {post}")

