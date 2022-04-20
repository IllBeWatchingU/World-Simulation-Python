from Roslina import Roslina

class Trawa(Roslina):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 0, polozenieX, polozenieY, 'T', 'trawa.png')
    
    def getNazwa(self):
        return "Trawa"

    def Dziecko(self, x, y):
        return Trawa(self.swiat, x, y)


