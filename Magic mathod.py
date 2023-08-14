class bike:
    def __init__(self, name, colour):
        self.name = name
        self.color = colour
    def __eq__(self, other):
        return self.name == other.name, self.colour == other.colour
    def __str__(self):
        return ( f" Name = {self.name}, Color = {self.colour}")

    def display(self):
        print(f"Name ={self.name},color ={self.colour} ")
Bike1 =("yamaha R15", " Blue")
Bike2= ("yamaha R15", " Blue")
#Bike2 = ("Pulser ns 160cc", "Red")
print(str(Bike1))
print(Bike1 == Bike2)