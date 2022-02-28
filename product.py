class Product(object):

    unique_id = 0

    @staticmethod
    def get_next_id():
        Product.unique_id += 1
        return Product.unique_id

    def __init__(self, name, sold, available, cost, price):
        self.__prod_id = Product.get_next_id()
        self.__name = name
        self.__sold = sold
        self.__available = available
        self.__cost = cost
        self.__price = price

    def get_id(self):
        return self.__prod_id

    def get_name(self):
        return self.__name

    def get_num_sold(self):
        return self.__sold

    def get_num_available(self):
        return self.__available

    def get_cost(self):
        return self.__cost

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Product Name:{self.__name}; Product ID:{self.__prod_id}; Sold:{self.__sold}; Available:{self.__available}; Cost:{self.__cost}; Price{self.__price}"