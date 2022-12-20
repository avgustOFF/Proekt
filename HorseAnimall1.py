from BaseAnimall import *

class HorseAnimall1 (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Саванна', 45, 'Лошадь', 'Растения', 12, 9)
        self.__color = color
        self.__tail = tail
        self.__sound = 'EEEEE'


    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.__tail