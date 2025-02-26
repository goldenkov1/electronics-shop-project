import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        return int(self.quantity) + int(other.quantity)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return  self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        try:
            csvfile = open('/home/slava/electronics-shop-project/src/items.csv', newline='', encoding='cp1251')
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv_")

        try:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if len(row['name']) < 10:
                    Item(row['name'], row['price'], row['quantity'])
        except Exception:
            raise InstantiateCSVError("Файл item.csv поврежден")






    @staticmethod
    def string_to_number(x):
        number = int(float(x))
        return number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Неизвестная ошибка скрипта.'




