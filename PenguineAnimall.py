from BaseAnimall import *

class PenguineAnimall (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Полюс', 25, 'Пенгвин', 'Мясо', 6)
        self.__color = color
        self.tail = tail
        self._sound = 'AAAAA'

    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.tail