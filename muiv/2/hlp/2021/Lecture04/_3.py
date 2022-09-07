from _2 import User

users: list[User] = []


def register_new_user(username, password):
    users.append(User(username, password))


if __name__ == '__main__':
    register_new_user("Newsky", "asdf")
    users[0].status = 1
    User.add_product(users[0], "minecraft")
    users[0]._products.append("minecraft")
    print(users[0])
