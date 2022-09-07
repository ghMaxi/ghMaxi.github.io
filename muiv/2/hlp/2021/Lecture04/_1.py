from datetime import datetime

users = []

_1.py
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
