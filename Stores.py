from Product import Product

class Store:
    def __init__(self, name):
        self.name=name
        self.list_of_products=[]
    def add_product(self, name, price, category):
        self.new_product=Product(name, price, category)
        self.list_of_products.append(self.new_product)
        return self
    def sell_product(self, id):
        self.list_of_products.pop(id)
        return self
    def inflation(self, percent_increase):
        for i in range(len(self.list_of_products)):
            self.list_of_products[i].update_price(percent_increase, True)
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.list_of_products)):
            if self.list_of_products[i].category==category:
                self.list_of_products[i].update_price(percent_discount, False)
