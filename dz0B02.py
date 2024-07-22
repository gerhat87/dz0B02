class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._level = "user"

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def set_name(self, name):
        self._name = name

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._level = "admin"


    def add_users(self, user_list, user):
        user_list.append(user)
        print(f"{user}  успешно добавлен в список")


    def remove_user(self, user_list, user):
        user_list.remove(user)

users = []

admin = Admin("1212", "Ivan")

user1= User("11", "Max")

print(user1.get_name())
admin.add_users(users, user1)
admin.remove_user(users, user1)