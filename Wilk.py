from Zwierze import Zwierze

class Wilk(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 9, 5, polozenieX, polozenieY, 'W', 'wilk.png')
    
    def czyTenSamGatunek(self, organizm):
        if organizm.literaOrganizmu == "W":
            return True
        return False

    def getNazwa(self):
        return "Wilk"

    def Dziecko(self, x, y):
        return Wilk(self.swiat, x, y)


