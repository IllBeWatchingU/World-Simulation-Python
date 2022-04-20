from Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 4, 4, polozenieX, polozenieY, 'O', 'owca.png')
    
    def czyTenSamGatunek(self, organizm):
        if organizm is None:
            return False
        if organizm.literaOrganizmu == "O":
            return True
        return False

    def getNazwa(self):
        return "Owca"

    def Dziecko(self, x, y):
        return Owca(self.swiat, x, y)


