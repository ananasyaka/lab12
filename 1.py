from tkinter import *

class IceCreamStand:
    def __init__(self, ICS_name, location, time, list=None):
        self.ICS_name = ICS_name
        self.loc = location
        self.time = time
        self.flavours = list

IceCream1 = IceCreamStand("Мечта", "Гороховая ул., д.35", "9-21",["Vanilla","Chocolate","Strawberry","mint"])
root = Tk()
Label(text="Available flavours", width=20, height=2).pack()
a = list(IceCream1.flavours)
for i in range(len(a)):
    Label(text=str(a[i]), width=20, height=2).pack()
root.mainloop()
