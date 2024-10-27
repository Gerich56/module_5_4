class House:
    houses_history = []

    def __new__(cls, *args):

        __instance = super(House, cls).__new__(cls)

        cls.houses_history.append(args[0])
        return __instance  #

    def __init__(self, name, number_of_floors):
        self.name = name  #  атрибуты имени
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")  #


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3

print(House.houses_history)

del h1

