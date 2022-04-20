from Zwierze import Zwierze

class Lis(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 3, 7, polozenieX, polozenieY, 'L', 'lis.png')
    
    def czyTenSamGatunek(self, organizm):
        if organizm.literaOrganizmu == "L":
            return True
        return False

    def wykonajRuch(self):
        losowePole = self.swiat.getLosowePoleMniejszegoSila(self)
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

        if self.swiat.czyPoleJestPuste(doceloweX, doceloweY) == False:
            zajmujacy = self.swiat.getOrganizm(doceloweX, doceloweY)
            if self.czyTenSamGatunek(zajmujacy):
                if Rozmnazanie(zajmujacy) == False:
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
        return "Lis"

    def Dziecko(self, x, y):
        return Lis(self.swiat, x, y)


