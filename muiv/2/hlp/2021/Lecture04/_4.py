from datetime import datetime


class User:
    DEFAULT_STATUS = 0
    ADVANCED_STATUS = 1
    DEFAULT_LICENSE = "Free"

    @classmethod
    def print_organization(cls, bytes):
        """Восстанавливает пользователя из сетевых байт"""
        return cls(*User.data_from_bytes(bytes))

    @staticmethod
    def data_from_bytes(bytes):
        """Восстанавливает имя и пароль из сетевых байт"""
        return "Имя", "Пароль"

    def __init__(self, username, password):
        self.username, self.password = username, password
        self.register_time = datetime.now()
        self.status = User.DEFAULT_STATUS
        self.license = User.DEFAULT_LICENSE
        self._products = []

    def add_product(self, product):
        if self.status == User.DEFAULT_STATUS:
            self.status = User.ADVANCED_STATUS
        self._products.append(product)

    def __str__(self):
        return f'User({vars(self)})'
