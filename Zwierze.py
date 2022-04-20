from Organizm import Organizm
from abc import abstractmethod

class Zwierze(Organizm):
    def __init__(self, swiat, sila, inicjatywa, polozenieX, polozenieY, literaOrganizmu, image):
        super().__init__(swiat, sila, inicjatywa, polozenieX, polozenieY, 0, literaOrganizmu, image)

    @abstractmethod
    def czyTenSamGatunek(self, organizm):
        pass

    def Rozmnazanie(self, partner):
        if self.swiat.czyWszystkiePolaZajete(self.polozenieX, self.polozenieY) and self.swiat.czyWszystkiePolaZajete(partner.polozenieX, partner.polozenieY):
            return False

        losowePole = self.swiat.getLosowePustePoleDlaObuOrganizmow(self, partner)

        if losowePole == 1:
            doceloweX = self.polozenieX
            doceloweY = self.polozenieY - 1
        elif losowePole == 2:
            doceloweX = self.polozenieX
            doceloweY = self.polozenieY + 1
        elif losowePole == 3:
            doceloweX = self.polozenieX - 1
            doceloweY = self.polozenieY
        elif losowePole == 4:
            doceloweX = self.polozenieX + 1
            doceloweY = self.polozenieY
        elif losowePole == 5:
            doceloweX = partner.polozenieX
            doceloweY = partner.polozenieY - 1
        elif losowePole == 6:
            doceloweX = partner.polozenieX
            doceloweY = partner.polozenieY + 1
        elif losowePole == 7:
            doceloweX = partner.polozenieX - 1
            doceloweY = partner.polozenieY
        elif losowePole == 8:
            doceloweX = partner.polozenieX + 1
            doceloweY = partner.polozenieY
        else:
            return False

        nowyOrganizm = self.Dziecko(doceloweX, doceloweY)
        self.swiat.dodajOrganizm(nowyOrganizm)
        self.swiat.dodajOrganizmDoPola(nowyOrganizm, doceloweX, doceloweY)
        self.swiat.komentarze.append(self.getNazwa() + " rozmnaza sie")
        return True

    def wykonajRuch(self):
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

    def Kolizja(self, atakujacy):
        if self.sila > atakujacy.sila:
            return False
        else:
            self.swiat.komentarze.append(atakujacy.getNazwa() + " zjada " + self.getNazwa())
            self.swiat.usunOrganizmZPola(self)
            self.inicjatywa = -1
            return True

    def Akcja(self):
        self.wykonajRuch()  

    



