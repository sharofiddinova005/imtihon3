class User:
    def __init__(self,name,phone,types,balans,password):
        self.name=name
        self.phone=phone
        self.types=types
        self.password=password
        self.balans=balans
        self.basket=[]

    def info(self):
        return f"name:{self.name} phone:{self.phone} balans:{self.balans}"

    def add_to_basket(self,product,quantity):
        if quantity<=0:
            print("Miqdori 0 dan katta bo'lishi kerak!")
            return
        if quantity>product.quantity:
            print("Do'konda bunday miqdorda mahsulot yo'q!")
            return
        self.basket.append(product,quantity)
        print(f"{product.titly} dan {quantity} ta savatga qo'shiladi.")

    def view_basket(self):
        if not self.basket:
            print("Savat bo'sh")
            return
        print("\n ====SAVATDAGI MAHSULOTLAR====")
        for index, (product,quantity) in enumerate(self.basket, start=1):
            print(f"{index}.{product.title} | {quantity} dona | {product.price * quantity} so'm")


    def view_product(self):
        if not self.basket:
            print("Savat bo'sh!")
            return
        for i in range(len(self.basket)):
            product,quantity=self.basket[i]
            print(f"{i+1}.{product.title} | {quantity} dona | {product.price * quantity} so'm")

    def view_balance(self):
        print(f"Sizning balansingiz: {self.balans} so'm")



admin=User("admin","784512","admin",0,"123")
user1=User("ali","784512","user",100_000_000,"123")
user2=User("vali","784512","user",100_000_000,"123")
user_baza=[admin,user1,user2]