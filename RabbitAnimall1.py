from BaseAnimall import *

class RabitAnimall1 (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Степь', 15, 'Кролик', 'Растения', 6, 2)
        self.__color = color
        self.__tail = tail
        self.__sound = 'FITFIT'


    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.__tail