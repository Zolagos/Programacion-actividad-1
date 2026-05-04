class car:

    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        
    def describe(self):
        print(self.brand)
        print(self.model)
        print(self.year)

    def getBrand(self):
        return self.__brand

    def setBrand(self, brand):
        self.__brand = brand

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model

    def getYear(self):
        return self.__year

    def setYear(self, year):
        self.__year = year
        
car1 = car("Ford", "F150", 2022)
car2 = car("Ford", "Mustang GT", 2014)
car3 = car("Seat", "Ibiza", 2026)
car4 = car("Ferrari","F80", 2026)
car5 = car("Aston Martin", "Vantage S", 2025)

car1.describe()
car2.describe()
car3.describe()
car4.describe()
car5.describe()

