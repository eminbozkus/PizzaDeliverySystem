import csv
import datetime


# Main fonksiyonunu tanımla
def main():
    # Hoşgeldin ekranı
    print("""
    ***********************************************************************
                    WELCOME TO THE GALAXY'S BEST PIZZER!
             HERE IS OUR MENU WITH OUR DELICIOUS PIZZAS AND SAUCE
    ***********************************************************************
    
    """)
    # Menu.txt dosyasını açarak menüyü ekrana yazdırma
    with open("Menu.txt", "r") as menu_file:
        print(menu_file.read())

    # Kullanıcının pizza ve sos seçimlerini alıp toplam fiyatı hesaplama
    pizza = input("Please Choose a Pizza Base: ")
    sos = input("And sauce of your choice: ")
    pizza_obj = None
    sos_obj = None

    # Seçilen pizza türüne göre ilgili sınıf objesini oluşturma
    if pizza == "1":
        pizza_obj = ClassicPizza()
    elif pizza == "2":
        pizza_obj = MargheritaPizza()
    elif pizza == "3":
        pizza_obj = TurkishPizza()
    elif pizza == "4":
        pizza_obj = PlainPizza()

    # Seçilen sos türüne göre ilgili sınıf objesini oluşturma
    if sos == "11":
        sos_obj = Olive(pizza_obj)
    elif sos == "12":
        sos_obj = Mushroom(pizza_obj)
    elif sos == "13":
        sos_obj = GoatCheese(pizza_obj)
    elif sos == "14":
        sos_obj = Meat(pizza_obj)
    elif sos == "15":
        sos_obj = Onion(pizza_obj)
    elif sos == "16":
        sos_obj = Corn(pizza_obj)

    # Toplam fiyatı hesaplama ve ekrana yazdırma
    total_cost = sos_obj.get_cost()
    print("Toplam fiyat: ", total_cost, " TL")

    # Kullanıcının kişisel bilgilerini ve sipariş bilgilerini alıp veritabanına kaydetme
    name = input("İsim: ")
    id_number = input("TC Kimlik Numarası: ")
    credit_card_number = input("Kredi Kartı Numarası: ")
    credit_card_password = input("Kredi Kartı Şifresi: ")
    description = sos_obj.get_description()
    order_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Veritabanı tablosuna sipariş bilgilerini kaydetme
    with open("Orders_Database.csv", "a", newline="") as orders_file:
        writer = csv.writer(orders_file)
        writer.writerow(
            ["Secilen pizza: " + pizza_obj.__class__.__name__, " Isim: " + name, "Tc kimlik numarasi: " + id_number,
             " Kredi kart numarasi: " + credit_card_number, " Pizza Ozellikleri: " + description,
             " Sparis zamani: " + order_time, credit_card_password])

    print("Siparişiniz alınmıştır. Teşekkür ederiz!")


# Üst sınıf "Pizza" tanımla
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Tam bir Klasik", 20.0)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 22.0)


class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Türk Pizza", 25.0)


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Plain Pizza", 30.0)


class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin"
        self.cost = 3.0


class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar"
        self.cost = 4.0


class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri"
        self.cost = 5.0


class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et"
        self.cost = 7.0


class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan"
        self.cost = 2.0


class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır"
        self.cost = 3.5


secim = "E"
while secim == "E":
    main()
    secim = input("Sipariş vermeye devam etmek istiyor musunuz? E/H : ")
    secim.upper()  # kullanıcının küçük harf girmesi ihtimaline karşı
    if secim == "H":
        print("Bizi tercih ettiğiniz için teşekkür ederiz!")
