class vehicle:
    velocity = 0
    def accelerate(self):
        self.velocity +=5

class car(vehicle):
    
    def __init__(self, brand, model, year):
        self.__brand = brand
        self.__model = model
        self.__year = year
        
    def describe(self):
        print(self.getBrand())
        print(self.getModel())
        print(self.getYear())

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

    def accelerate(self):
        self.velocity +=10
        

class bicicle(vehicle):

    def __init__(self, type, brand):
        self.__type = type
        self.__brand = brand

    def describe(self):
        print(self.__type)
        print(self.__brand)

    def accelerate(self):
        self.velocity +=2