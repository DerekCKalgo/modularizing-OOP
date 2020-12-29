from Stores import Store

a=Store("xxxx")
a.add_product("xxxx", 2.2, "noodle")
a.add_product("Mountain Dew", 1.2, "Soda")
a.add_product("Coke", 1.3, "Soda")
a.set_clearance("Soda", 0.1)
a.list_of_products[0].print_info()
a.list_of_products[1].print_info()
a.list_of_products[2].print_info()
