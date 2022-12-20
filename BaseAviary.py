from BaseAnimall import *
class BaseAvairy:
    def __init__(self, biome, squear, type, food):
        self.__biome = biome
        self.__squear = squear
        self.type = type
        self.food = food
        self.animalls = []

    @property
    def Biome(self):
        return self.__biome

    @property
    def Squear(self):
        return self.__squear

    @property
    def Type(self):
        return self.type

    @property
    def Food(self):
        return self.food

    def DoAddAnimall(self, NewAnimall : BaseAnimall):
        if len(self.animalls) == 0 and self.squear >= NewAnimall.squear and self.biome == NewAnimall.biome :
            self.animalls.append(NewAnimall)
        else:
         if self.__biome == NewAnimall.biome and self.squear >= NewAnimall.squear and self.type == NewAnimall.type and self.food == NewAnimall.food
