from BaseAnimall import *

class WolfAnimall (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Степь', 32, 'Волк', 'Мясо', 12, 7)
        self.__color = color
        self.__tail = tail
        self.__sound = 'AUF'


    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.__tail