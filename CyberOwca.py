from Zwierze import Zwierze

class CyberOwca(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 11, 4, polozenieX, polozenieY, 'R', 'cyberowca.png')
        self.doceloweX = -1
        self.doceloweY = -1
    
    def czyTenSamGatunek(self, organizm):
        if organizm.literaOrganizmu == "R":
            return True
        return False

    def wykonajRuch(self):
        if self.swiat.czyBarszczIstnieje():
            self.swiat.znajdzNajblizszyBarszcz(self)
            if self.doceloweX < self.polozenieX and self.doceloweY < self.polozenieY:
                losowePole = 3
            elif self.doceloweX == self.polozenieX and self.doceloweY < self.polozenieY:
                losowePole = 1
            elif self.doceloweX > self.polozenieX and self.doceloweY < self.polozenieY:
                losowePole = 4
            elif self.doceloweX < self.polozenieX and self.doceloweY > self.polozenieY:
                losowePole = 3
            elif self.doceloweX == self.polozenieX and self.doceloweY > self.polozenieY:
                losowePole = 2
            elif self.doceloweX > self.polozenieX and self.doceloweY > self.polozenieY:
                losowePole = 4
            elif self.doceloweX < self.polozenieX and self.doceloweY == self.polozenieY:
                losowePole = 3
            elif self.doceloweX > self.polozenieX and self.doceloweY == self.polozenieY:
                losowePole = 4
        else:
            losowePole = self.swiat.getLosowePole(self)

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
        else:
            return False

        if doceloweX < 0 or doceloweY < 0 or doceloweX >= self.swiat.szerokosc or doceloweY >= self.swiat.wysokosc:
            return False

        if self.swiat.czyPoleJestPuste(doceloweX, doceloweY) == False:
            zajmujacy = self.swiat.getOrganizm(doceloweX, doceloweY)
            if self.czyTenSamGatunek(zajmujacy):
                if self.Rozmnazanie(zajmujacy):
                    return True
            elif zajmujacy.Kolizja(self):
                self.swiat.usunOrganizmZPola(self)
                self.polozenieX = doceloweX
                self.polozenieY = doceloweY
                self.swiat.dodajOrganizmDoPola(self, doceloweX, doceloweY)
            return False
        else:
            self.swiat.usunOrganizmZPola(self)
            self.polozenieX = doceloweX
            self.polozenieY = doceloweY
            self.swiat.dodajOrganizmDoPola(self, doceloweX, doceloweY)
            return True

    def getNazwa(self):
        return "Cyberowca"

    def Dziecko(self, x, y):
        return CyberOwca(self.swiat, x, y)

