from free_user import FreeUser
from premium_user import PremiumUser

scrub = FreeUser("Jimmy", "jimmy@jimmy.com", "qazxsw", 'j1234')
other = PremiumUser("Seth", 'seth@seth.com', '123456', "1234s")

print(scrub.make_post("fdsfsd"))
print(scrub.make_post("orueowro"))
print(scrub.make_post("orueowro"))

