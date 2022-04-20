import random
from Organizm import Organizm

class Roslina(Organizm):
    def __init__(self, swiat, sila, polozenieX, polozenieY, literaOrganizmu, image):
        super().__init__(swiat, sila, 0, polozenieX, polozenieY, 0, literaOrganizmu, image)

    def ProbaRozmnozeniaSie(self):
        los = random.randrange(100)

        # roślina ma 10% szansy, że się rozmnoży
        if los > 10:
            return False

        if self.swiat.czyWszystkiePolaZajete(self.polozenieX, self.polozenieY):
            return False

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
        else:
            return False

        nowyOrganizm = self.Dziecko(doceloweX, doceloweY)
        self.swiat.dodajOrganizm(nowyOrganizm)
        self.swiat.dodajOrganizmDoPola(nowyOrganizm, doceloweX, doceloweY)
        return True

    def Akcja(self):
        if self.ProbaRozmnozeniaSie():
            self.swiat.komentarze.append(self.getNazwa() + " rozmnaza sie")

    def Kolizja(self, atakujacy):
        self.swiat.komentarze.append(atakujacy.getNazwa() + " zjada " + self.getNazwa())
        self.swiat.usunOrganizmZPola(self)
        self.inicjatywa = -1
        return True



