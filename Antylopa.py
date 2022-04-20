import random
from Zwierze import Zwierze

class Antylopa(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 4, 4, polozenieX, polozenieY, 'A', 'antylopa.png')
    
    def czyTenSamGatunek(self, organizm):
        if organizm.literaOrganizmu == "A":
            return True
        return False

    def wykonajUnik(self, atakujacy):
        losowaLiczba = random.randrange(100)
        if losowaLiczba < 50:
            if self.swiat.czyWszystkiePolaZajete(self.polozenieX, self.polozenieY):
                return False
            else:
                losowePole = self.swiat.getLosowePustePole(self)
                doceloweX = self.polozenieX
                doceloweY = self.polozenieY
                if losowePole == 1:
                    doceloweY = self.polozenieY - 1
                elif losowePole == 2:
                    doceloweY = self.polozenieY + 1
                elif losowePole == 3:
                    doceloweX = self.polozenieX - 1
                elif losowePole == 4:
                    doceloweX = self.polozenieX + 1

                self.swiat.usunOrganizmZPola(self)
                self.polozenieX = doceloweX
                self.polozenieY = doceloweY
                self.swiat.dodajOrganizmDoPola(self, doceloweX, doceloweY)
                return True
        return False

    def Kolizja(self, atakujacy):
        if self.sila > atakujacy.sila:
            return False

        if self.wykonajUnik(atakujacy):
            self.swiat.komentarze.append(self.getNazwa() + " unika ataku " + atakujacy.getNazwa())
            return True
        else:
            self.swiat.komentarze.append(atakujacy.getNazwa() + " zjada " + self.getNazwa())
            self.swiat.usunOrganizmZPola(self)
            self.inicjatywa = -1
            return False

    def getNazwa(self):
        return "Antylopa"

    def Dziecko(self, x, y):
        return Antylopa(self.swiat, x, y)


