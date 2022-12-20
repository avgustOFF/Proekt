from BaseAnimall import *

class Horse (BaseAnimall):
    def __init__(self, name, color, tail):
        super().__init__(name, 'Саванна', 45, 'Лошадь', 'Растения', 14)
        self.color = color
        self.tail = tail
        self.__sound = 'EEEEE'

    @property
    def Color(self):
        return self.color

    @property
    def Tail(self):
        return self.tail