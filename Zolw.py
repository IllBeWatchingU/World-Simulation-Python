from Zwierze import Zwierze

class Zolw(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 2, 1, polozenieX, polozenieY, 'Z', 'zolw.png')
    
    def czyTenSamGatunek(self, organizm):
        if organizm.literaOrganizmu == "Z":
            return True
        return False

    def odeprzyjAtak(self, atakujacy):
        if atakujacy.sila < 5:
            return True
        return False

    def Kolizja(self, atakujacy):
        if self.sila > atakujacy.sila:
            return False

        if self.odeprzyjAtak(atakujacy):
            self.swiat.komentarze.append(self.getNazwa() + " odpiera atak " + atakujacy.getNazwa())
            return False
        else:
            self.swiat.komentarze.append(atakujacy.getNazwa() + " zjada " + self.getNazwa())
            self.swiat.usunOrganizmZPola(self)
            self.inicjatywa = -1
            return True

    def getNazwa(self):
        return "Zolw"

    def Dziecko(self, x, y):
        return Zolw(self.swiat, x, y)
