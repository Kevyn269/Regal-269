from product import Product

class Store(object):
    str_id = 0

    def get_next_id(self):
        Store.str_id = Store.str_id+1
        return Store.str_id

    #InventoryId, StoreName, City, Area

    def __init__(self, store_name, city, area):
        self.__store_id = self.get_next_id()
        self.__store_name = store_name
        self.__city = city
        self.__area = area
        self.__products = {}

    def get_store_id(self):
        return self.__store_id

    def get_store_name(self):
        return self.__store_name

    def get_city(self):
        return self.__city

    def get_area(self):
        return self.__area

    def get_product(self):
        return self.__products

    def add_product(self, product_name, sold, available, cost, price):
        new_product = Product(product_name, sold, available, cost, price)
        self.__products[new_product.get_id()] = new_product

    def remove_product(self, product_id):
        if product_id in self.__products:
            self.__products.remove(product_id)

    def count_products(self):
        return len(self.__products)