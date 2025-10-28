"oop - abyektga yo'naltirilgan dasturlash"
"Encapsulation- Malumot va u bilan ishlovchi metodlarni bitta obyekt ichida joylaydi"

"Public-Hamma joydan ko'rish va ishlatish mumkin.Hech qanday cheklov yo'q. Pythonda: oddiy nom bn yoziladi."
class User:
    def __init__(self,name):
        self.name=name
u=User("Ali")
print(u.name)

"Protected - Faqat ichki class va undan meros olgan classlarda ishlatish un mo'ljallangan. lekin barbir tashqaridan ham kira qolsa bo'ladi _ bn yoz"
class User:
    def __init__(self,name):
        self._name=name
u=User("Ali")
print("u._name")# texnik jihatdan ishlaydi lekin tavsiya qilinmaydi

"Private - Faqat class ichida ishlatiladi, tashqaridan kira olmaysan. Pythonda: __ chiziqcha bn yoz."
class User:
    def __init__(self,password):
        self.__password=password
u=User("1234")
"Getter - private/protected o'zgaruvchini tashqaridan o'qib olish un metot."
"Setter - private/protected o'zgaruvchini tashqaridan qiymat berish un metot."
class User:
    def __init__(self,name,password):
        self.name=name
        self.__password=password

    def get_password(self):
        return self.__password

    def set_password(self,new_password):
        if len(new_password)>=4:
            self.__password=new_password
            print("Parol muvaffaqiyatli o'zgartirildi")
        else:
            print("Parol xato")


"Absraction - Murakkab narsani soddalashtiradi, faqat kerakli malumotni olish, qolgan ortiqchasini yashirish"
"Abstract class va Interface( faqat metodlar shabloni)"
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
c=Circle(5)
print(c.area())
"Vorislik - Supclass Superclassdan xususiyat va metotlarni meros qilib olishiga aytiladi"

"Single - bitta classdan meros olish"
"Multiple - 1 nechta classdan meros olish"
"Multilevel - zanjirli meros"
"Tree inheritance - bitta ota classdan 1 nechta bola class"

"Polimorfizim - Bir metot turli classlarda turlicha ishlatilishiga aytiladi"

"Konstiruktorlar - obyekt yaratilganda ishlaydi. Pythonda bu metod har doim __init__ deb yoziladi. U obyektning dastlabki xususiyatlarini belgilash uchun kerak."

"Destructor - bu obyekt yo'q qilinayotganda (memorydan o'chirilganda) avtomatik ishlaydigan metod. Pythonda __del__ nomi bn yoziladi."



"katigori tayteli , prodakt va kotigoriya promo key, podact 3 dan katta 50 dan kichkina narxi 1 dan katta 1000 dan kichkina costumer name 1 dan katta 30 dan kichikina"

"tel nomer , ordesni qualtetisi 1 dan katta 1100 dan kichkina , orderni 08 01 bo'lishi kerak"