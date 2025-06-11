from user import User

class PremiumUser(User):

    def __init__(self, name, email, password, id):
        super().__init__(name, email, password, id)
    
    def make_post(self, post):
        return super().make_post(post)