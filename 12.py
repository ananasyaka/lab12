
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating
    def describe_restaurant(self):
        print(f"Название Ресторана - {self.restaurant_name},  кухня:  {self.cuisine_type} ")
    def open_restaurant(self):
        print("Ресторан сейчас открыт.")
    def rait_restaurant(self,new_rait):
        old_rait = self.rating
        self.rating = new_rait
        print(f"Рейтинг ресторана {self.restaurant_name} был обновлен до {self.rating}, предыдущий рейтинг: {old_rait}")

class IceCreamStand(Restaurant):
    def __init__(self, ICS_name, location, time, list1=None, list2=None, list3=None):
        self.ICS_name = ICS_name
        self.loc = location
        self.time = time
        self.flavours = [str(list1)] + [str(list2)] + [str(list3)]
    def describe_ICS(self):
        print(f"Название Кафе - {self.ICS_name}")
        print(f"Вкусы мороженого:")
        a = list(self.flavours)
        for i in range(len(a)):
            print(a[i])
        print(f"Адрес:{self.loc}")
        print(f"Время работы:{self.time}")
    def appflavors(self,fl):
        self.flavours.append(str(fl))
    def delflavors(self,fl1):
        a=str(fl1)
        self.flavours.remove(a)
    def nalichie(self,fl2):
        a = list(self.flavours)
        b = str(fl2)
        nal = False
        for i in range(len(a)):
            if b == a[i]:
                nal= True
        if nal == True:
            print("Вкус в наличие")
        else: print("Вкуса нет в наличие!")
class IceCreamMyagk(IceCreamStand):
    def __init__(self, ICS_name, price, list1=None, list2=None, list3=None):
        self.ICS_name = ICS_name
        self.flavours = [str(list1)] + [str(list2)] + [str(list3)]
        self.sharik = int(price)
    def price(self,kolvo):
        pr = self.sharik * kolvo
        print("Стоимость " + str(kolvo) + " шариков мороженого:" + str(pr) + " руб")

class IceCreamPalochka(IceCreamStand):
    def __init__(self, ICS_name, fl=None):
        self.ICS_name = ICS_name
        self.flavours = fl
    def nalichie(self,flav):
        a = dict(self.flavours)
        b = str(flav)
        if b in a:
            print("Вкус в наличие в кол-ве " + str(a[b]) + " шт.")
        else:
            print("Вкуса нет в наличие!")

IceCreamStand = IceCreamStand("Монпасье","Садовая ул. д.40","9-18","шоколад","ваниль","клубника")

IceCreamStand.appflavors("апельсин")
IceCreamStand.describe_ICS()
IceCreamStand.delflavors("ваниль")
IceCreamStand.nalichie("ваниль")

IceCreamM = IceCreamMyagk("Монпасье", 150, "банан","лимон","клубника")
IceCreamP = IceCreamPalochka("Монпасье",{"ваниль":10,"шоколад":15,"пралине":5})

IceCreamM.nalichie("банан")
IceCreamP.nalichie("ваниль")
IceCreamM.price(3)



