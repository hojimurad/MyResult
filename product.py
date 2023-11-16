

class Product:
    def __init__(self,name,price,manifacturer):
        self.name = name
        self.price  =price
        self.manifacturer =manifacturer

    def get_name(self):
        return self.name
    def get_price(self):
        return f"{self.price} so'm"

    def get_manifacturer(self):
        return self.manifacturer


class Market(Product):
    def __init__(self,product_name,product_price,product_manifacturer,data_create,product_sale):
        super().__init__(name=product_name,price=product_price,manifacturer=product_manifacturer)

        self.data_create =data_create
        self.product_sale =product_sale
        if 2023-self.data_create>=2:
            self.price  = product_price-(product_price/100)*product_sale
        else:
            self.price =product_price

    def get_data_create(self):
        return self.data_create
    def get_product_sale(self):
        return self.product_sale

olma= Market("olma",100_000,"Apple company",2021,15)
print(olma.get_price())