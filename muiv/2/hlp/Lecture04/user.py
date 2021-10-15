from datetime import datetime


class User:
    DEFAULT_STATUS = 0
    DEFAULT_LICENSE = "Free"

    def __init__(self, username, password):
        self.username, self.password = username, password
        self.register_time = datetime.now()
        self.status = User.DEFAULT_STATUS
        self.license = User.DEFAULT_LICENSE
        self.products = []


users: list[User] = []


def register_new_user(username, password):
    register_time = datetime.now()
    user_status = 0    # 0 = новичок
    user_license = "Free"
    user_products = []
    users.append([username, password, register_time,
                  user_status, user_license, user_products])


def update_user_status(user_id, new_status):
    users[user_id][1] = new_status


def add_user_product(user_id, new_product):
    users[user_id][6].append(new_product)


if __name__ == '__main__':
    register_new_user("Newsky", "asdf")
    update_user_status(0, 1)
    add_user_product(0, "minecraft")
    print(users[0])
