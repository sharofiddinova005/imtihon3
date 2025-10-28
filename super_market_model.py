from os import remove

from user_model import User, user_baza
from product_model import Products, product_baza

class Shop:
    def __init__(self,title):
        self.title=title
        self.baza=[]
        self.users=[]
        self.balans=0

    def login(self):
        username=input("username:")
        password=input("password:")
        for item in self.users:
            if item.name == username and item.password == password:
                return item
        return None


    def add_product(self):
        title=input("title")
        price=input("price")
        quantity=input("quantity")
        p=Products(title,price,quantity)
        self.baza.append(p)
        print(f"{title} bazaga qo'shildi!")

    def view_products(self):
        count=0
        for item in self.baza:
            count+=1
            print(f"{count}.", item.info())

    def add_to_basket(self,user:User):
        self.view_products()
        tanlov=int(input("Mahsulot raqamini tanlang:"))
        index=1
        for product in self.baza:
            if index == tanlov:
                quantity=int(input("Miqdori:"))
                if quantity<=product.quantity:
                    user.basket.append((product,quantity))
                    print("Mahsulot korzinkaga qo'shildi!")
                else:
                    print("Buncha mahsulot yetarli emas!")
                break
            index+=1


    def buy_product(self,user:User):
        self.view_products()
        if not self.baza:
            return
        tanlov =int(input("Qaysi mahsulotni olasiz? (raqam):"))-1
        if tanlov<0 or tanlov>=len(self.baza):
            print("Noto'g'ri tanlov! \n")
            return
        product=self.baza[tanlov]
        soni =int(input("Nechta olmoqchisiz?"))
        if soni>product.quantity:
            print(f"Uzur, bizda {product.title} dan {product.quantity} dona bor xolos. \n")
            return
        umumiy_summa=soni*product.price
        if user.balans<umumiy_summa:
            print("Supermarket balansida yetarli mablag' yo'q! \n")
            return
        user.balans-=umumiy_summa
        self.balans+=umumiy_summa
        product.quantity-=soni
        user.basket.append((product.title, soni, umumiy_summa))
        print(f"{soni} dona {product.title} muvaffaqiyatli sotib olindi! \n")



shop = Shop("Shop")
shop.users = user_baza
shop.baza = product_baza


def admin_manager(s:Shop):
    while True:
        kod=input("\n===ADMIN MENYU=== \n 1.Mahsulot qo'shish \n 2.Mahsulot ko'rish \n 3.Shop balans \n 4.Chiqish \n Tanlov: ")
        if kod=="1":
            s.add_product()
        elif kod=="2":
            s.view_products()
        elif kod=="3":
            print(f"\n Shop balansi:{s.balans} so'm\n")
        elif kod=="4":
            break
        else:
            print("No'to'g'ri tanlov!")


def user_manager(u: User, s: Shop):
    while True:
        print("\n ====FOYDALANUVCHI MENYUSI====")
        kod1=input("1.Maxsulotlarni ko'rish va qo'shish \n 2.Savatni ko'rish \n 3.Maqsulot sotib olish \n 4.Savat maqsulotini o'chirish \n 5. Chiqish \n Tablov:")
        if kod1=="1":
            s.view_products()
            index=input("index:")
            quantity=int(input("miqdori:"))
            p1=s.baza[int(index)-1]
            if quantity>p1.quantity:
                print(f"Uzur, bizda {p1.title} dan {p1.quantity} dona bor")
            else:
                u.basket.append((p1,quantity))
                print(f"{p1.title} dan {quantity} ta korzinkaga qo'shildi.")
        elif kod1=="2":
            u.view_basket()
        elif kod1=="3":
            u.view_product()
        elif kod1=="4":
            u.view_basket()
            index=int(input("O'chirimoqchi bo'lgan mahsulot indexini kiriting:"))
            if 0<index<=len(u.basket):
                removed_product, removed_quantity=u.basket.pop(index-1)
                print(f"{removed_product.title} savatdan o'chirish!({removed_quantity} dona \n")
            else:
                print("Noto'g'ri index! \n")
        elif kod1=="5":
            print("Dastur tugadi")
            break
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring! \n")



def shop_manager(s:Shop):
    while True:
        kod2=input("1.Login \n 2.Exit \n Tanlov: ")
        if kod2 =="1":
            user = s.login()
            if user is None:
                print("Login yoki password xato! \n")
                continue
            if user.types =="admin":
                print("Admin paneliga xush kelibsiz!")
                admin_manager(s)
            elif user.types =="user":
                print(f"Xush kelibsiz {user.name}!")
                user_manager(user,s)
            else:
                print("User turi noma'lum! \n")

        elif kod2=="2":
            print("Chiqildi!")
            break
        else:
            print("No'to'g'ri tanlov, qayta urinib ko'ring. \n")
