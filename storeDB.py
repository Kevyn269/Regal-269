import csv
import copy



from store import Store



class storeDB(object):
    

    def __init__(self, filename):
        self.__filename = filename
        self.__store_dict = {}
        self.__store_obj_list = []



    def read_file(self):
        with open(self.__filename, encoding='utf-8', mode='r') as reading:
            reader = csv.reader(reading)
            for rows in reader:
                self.__store_dict[rows[0]]=[rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8]]
            del self.__store_dict['\ufeffInventoryId']
        print(f"{len(self.__store_dict.keys())} added to the Dictionary")


    def store_exists(self,str_obj):
        str_name = str_obj.get_store_name()
        str_city = str_obj.get_city()
        str_area = str_obj.get_area()
       
        for store_obj in self.__store_obj_list:
            store_name = store_obj.get_store_name()
            store_city = store_obj.get_city()
            store_area = store_obj.get_area()
            if (str_name == store_name) and (str_city == store_city) and (str_area == store_area):
                return self.__store_obj_list.index(store_obj)
        return -1

    def add_store_products(self):
        for store_obj in self.__store_dict.values():
            store_object = store_obj [0:3]
            prod_obj = store_obj [3:8]
            s = Store(*store_object)
            exists = self.store_exists(s)
            if exists == -1:
                self.__store_obj_list.append(s)
                s.add_product(*prod_obj)
            else:
                s.add_product(*prod_obj)
        print(f"{len(self.__store_dict)} records added to unique {len(self.__store_obj_list)} stores")

            
    def print_store_info(self, str_nm):
        print(f"Searching for Store named {str_nm}")

        for store_obj in self.__store_obj_list:
            store_name = store_obj.get_store_name().lower().strip()
            if str_nm.lower().strip() == store_name:
                str_id = store_obj.get_store_id()
                str_city = store_obj.get_city()
                str_area = store_obj.get_area()
        
                print(f"Store_ID: {str_id}; Store_Name: {str_nm}; Store_City: {str_city}, Store_Area: {str_area}")

    def print_product_info(self, str_id):
        print(f"Printing Product List For Store ID {str_id}")
        for s_obj in self.__store_obj_list:
            store_id = s_obj.get_store_id()
            if str_id == store_id:
                products = s_obj.get_product()
                if products:

                    for product_id, product in products.items():
                        p_nm = product.get_name()
                        p_sold = product.get_num_sold()
                        p_av = product.get_num_available()
                    
                        print(f"Product ID: {product_id}", end = " ")
                        print(f"Product Name: {p_nm}", end = " ")
                        print(f"Sold: {p_sold}", end = " ")
                        print(f"Available: {p_av}")
                    return
                else:
                    print("Products Not Found")
                    return
        print("Store not Found")
        


    def remove_store_data(self, str_id):
        
        for str_obj in self.__store_obj_list:
            store_id = str_obj.get_store_id()
            if str_id == store_id:
                self.__store_obj_list.remove(str_obj)
                print(f"Successfully removed store with store id: {str_id}")
                return
            
        print("Store not Found")

    def add_new_store(self, s_nm, s_city, s_area):
        new_store = Store(s_nm,s_city,s_area)
        exists = self.store_exists(new_store)
        if exists == -1:
            self.__store_obj_list.append(new_store)
            print(f"Successfully added new {new_store.get_store_name()} store")

    def add_new_product(self, s_id, p_nm, p_sold, p_avl, p_cost, p_price):
        
        for store_obj in self.__store_obj_list:
            store_id = store_obj.get_store_id()
            if store_id == s_id:
                store_obj.add_product(p_nm,p_sold,p_avl, p_cost, p_price)
                print(f"Successfully added new {p_nm} ")

                return
        print ("Store not found, Product can't be added")

                

def main():
    comp = storeDB("inventory.csv")
    print("******************************************************************************")
    comp.read_file()
    print("******************************************************************************")
    comp.add_store_products()
    print("******************************************************************************")
    #str_nm = input("Enter the store name that you want to search: ")
    comp.print_store_info("Walmart")
    print("******************************************************************************")
    #str_id = int(input("Enter the store ID for the product list: "))
    comp.print_product_info(29)
    print("******************************************************************************")
    #str_id = int(input("Enter the store ID of the store that you want to remove: "))
    comp.remove_store_data(996)
    print("******************************************************************************")
    comp.add_new_store('Walmart', 'Charlottetown', '1 abc st')
    print("******************************************************************************")
    comp.add_new_product(1001, 'Laptop', 300, 200, 2048.12, 2132.43)
    print("******************************************************************************")
    comp.print_store_info("Walmart")
    print("******************************************************************************")
    comp.print_product_info(1001)
    print("******************************************************************************")

if __name__ == "__main__":
    main()
