# classes and atributes can be done like so

class HardcodeUser:
    pass  # allows you to write a class or function without anything inside


user_1 = HardcodeUser()
user_1.id = "001"
user_1.username = "connor"

# print(user_1.username)


class User:
    # constructor is below
    # initialise attributes, will be called everytime the class is used
    # when the class is called, the parameters can be passed through into __init__
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # sometimes there are attributes that don't get set this is a default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "cna93")
user_2 = User("002", "cna94")

user_1.follow(user_2)

print(user_2.followers)
print(user_1.following)
# print(user_1.username)

