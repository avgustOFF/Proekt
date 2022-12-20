from BaseAnimall import *

class RabitAnimall (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Степь', 15, 'Кролик','Растения', 5)
        self.__color = color
        self.tail = tail
        self._sound = 'UUUUU'

    @property
    def Color(self):
        return self.__color

    @property
    def Tail(self):
        return self.tail