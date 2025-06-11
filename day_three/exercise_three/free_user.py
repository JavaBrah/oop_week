from user import User

class FreeUser(User):
    
    def __init__(self, name, email, password, id, post_counter=0):
        super().__init__(name, email, password, id)
        self.post_counter = post_counter
    
    @property
    def post_counter(self):
        return self._post_counter
    
    @post_counter.setter
    def post_counter(self, new_counter):
        if new_counter == 0:
            self._post_counter = new_counter
        else:
            raise ValueError("Double check self.post_counter")

    def add_to_post_counter(self):
        self.post_counter += 1

    def make_post(self, post):
        if self.post_counter < 2:
            return super().make_post(post)
        else:
            print("You have reach your post limit")
            return None