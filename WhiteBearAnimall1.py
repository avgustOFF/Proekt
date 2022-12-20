from BaseAnimall import *

class WhiteBearAnimall1 (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Полюс', 34, 'Белый медведь', 'Мясо', 34, 15)
        self.__color = color
        self.__tail = tail
        self.__sound = 'RRRRR'


    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.__tail