class Product:
    def __init__(self, pcode, pname, pprice):
        self.pcode = pcode
        self.pname = pname
        self.pprice = pprice

    def __str__(self):
        return f"Code: {self.pcode}, Name: {self.pname}, Price: {self.pprice}"


class Category:
    def __init__(self, code, name, parent=None, product_info=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.products = []
        self.display_name = self.generate_display_name()
        
        if product_info is not None:
            self.add_products_from_info(product_info)

    def generate_display_name(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.generate_display_name()} > {self.name}"

    def add_product(self, product):
        self.products.append(product)

    def add_products_from_info(self, product_info):
        product_list = product_info.get(self.name, [])
        for i, (name, price) in enumerate(product_list):
            product = Product(f"P0{self.code}{i+1}", name, price)
            self.add_product(product)

    def display_category(self):
        print(f"Category Code: {self.code}, Display Name: {self.display_name}")
        print("Products:")
        for product in self.products:
            print(f"  {product}")
        print("-" * 60)

    def display_all_categories(categories):
        print("Displaying all categories with products:\n")
        for category in categories:
            category.display_category()

    def sort_categories(categories):
        n = len(categories)
        for i in range(n):
            for j in range(0, n-i-1):
                if categories[j].name > categories[j+1].name:
                    categories[j], categories[j+1] = categories[j+1], categories[j]

    def display_products_grouped_by_category(categories):
        print("\nProducts grouped by category (ordered by category name):\n")
        Category.sort_categories(categories)

        for category in categories:
            print(f"Category: {category.display_name}")
            for product in category.products:
                print(f"  {product}")
            print("-" * 60)


# Create product objects
product_info = {
    "Vehicle": [("Vehicle Tire", 11000), ("Vehicle Engine", 21000), ("Vehicle Battery", 31000)],
    "Car": [("Car Engine", 12000), ("Car Battery", 22000), ("Car Tire", 32000)],
    "Petrol": [("Fuel Pump", 500), ("Fuel Filter", 600), ("Fuel Injector", 700)],
    "Bike": [("Bike Chain", 300), ("Bike Brake", 400), ("Bike Pedal", 500)],
    "Electric": [("Electric Motor", 10000), ("Electric Battery", 15000), ("Electric Controller", 20000)],
}

vehicle = Category(1, "Vehicle", product_info=product_info)
car = Category(2, "Car", vehicle, product_info=product_info)
petrol = Category(3, "Petrol", car, product_info=product_info)
bike = Category(4, "Bike", vehicle, product_info=product_info)
electric = Category(5, "Electric", bike, product_info=product_info)

categories = [vehicle, car, petrol, bike, electric]
Category.display_all_categories(categories)
Category.display_products_grouped_by_category(categories)
