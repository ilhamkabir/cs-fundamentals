

class UserData:
    user_name = "ilham"
    password = "aj;flsdjks"

class User(UserData):

    @property
    def user_name(self):
        return UserData.user_name

    @property
    def password(self):
        return "********"

user = User()
print(user.user_name)
print(user.password)
