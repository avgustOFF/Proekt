class BaseAnimall:
    def __init__(self, name, biome, squear, type, food, age):
        self.name = name
        self.__biome = biome
        self.__squear = squear
        self.__type = type
        self.__food = food
        self.__age = age
        self.sound = ''

    @property
    def Biome(self):
        return self.__biome

    @property
    def Squear(self):
        return self.__squear

    @property
    def Type(self):
        return self.__type

    @property
    def Food(self):
        return self.__food

    @property
    def Age(self):
        return self.__age

    def DoSound(self):
        print(self.name, 'издаёт звук', self.sound)