from BaseAnimall import *

class HorseAnimall1 (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Саванна', 55, 'Жираф', 'Растения', 34, 12)
        self.__color = color
        self.__tail = tail
        self.__sound = 'YUYUYU'


    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.__tail