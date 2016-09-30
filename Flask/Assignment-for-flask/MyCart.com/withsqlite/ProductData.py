class Product:
    def __init__(self, productdict):
        self.name = productdict['name']
        self.category = productdict['category']
        self.price = productdict['price']
        self.image = productdict['image']
        self.description = productdict['description']
        self.instock = productdict['instock']
