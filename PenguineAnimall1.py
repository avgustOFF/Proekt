from BaseAnimall import *

class PenguineAnimall1 (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Полюс', 25, 'Пенгвин', 'Мясо', 7, 4)
        self.__color = color
        self.__tail = tail
        self.__sound = 'AAAAA'


    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.__tail