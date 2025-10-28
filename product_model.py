

class Products:
    def __init__(self,title,price,quantity):
        self.title=title
        self.price=int(price)
        self.quantity=int(quantity)

    def info(self):
        return f"title:{self.title} price:{self.price} quantity:{self.quantity}"

p1=Products("olma",12000,100)
p2=Products("olcha",20000,100)
p3=Products("nok",15000,100)
p4=Products("qulupnay",25000,100)
product_baza=[p1,p2,p3,p4]
