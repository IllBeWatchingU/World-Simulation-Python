import random
from Zwierze import Zwierze

class Czlowiek(Zwierze):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 5, 4, polozenieX, polozenieY, 'C', 'czlowiek.png')
        self.cooldownZdolnosci = 0
        self.czasZdolnosci = 5
        self.czyZdolnoscAktywna = False
    
    def czyTenSamGatunek(self, organizm):
        return False

    def aktywujUmiejetnosc(self):
        if self.czyZdolnoscAktywna == False and self.cooldownZdolnosci == 0:
            self.czyZdolnoscAktywna = True
            return True
        return False

    # sprawdza czy zdolność może być aktywowana
    def czyZdolnoscMoze(self):
        if self.cooldownZdolnosci != 0:
            self.cooldownZdolnosci = self.cooldownZdolnosci - 1
            return False
        return True

    def wykonajUmiejetnosc(self):
        if self.czyZdolnoscAktywna == False:
            return

        if self.czasZdolnosci == 0:
            self.cooldownZdolnosci = 5
            self.czasZdolnosci = 5
            self.czyZdolnoscAktywna = False

    def wykonajRuch(self):
        losowePole = self.swiat.ruchCzlowieka
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
            if zajmujacy.Kolizja(self):
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

    def Akcja(self):
        if self.czyZdolnoscMoze():
            if self.czyZdolnoscAktywna:
                self.wykonajUmiejetnosc()

        if self.czyZdolnoscAktywna:
            # przez pierwsze 3 tury człowiek porusza się o dwa pola
            if self.czasZdolnosci >= 3:
                for i in range(2):
                    if self.wykonajRuch() == False:
                        break
                self.czasZdolnosci = self.czasZdolnosci - 1
            # w  ostatnich dwóch turach umiejętności jest 50% szansy, że poruszy się o dwa pola
            elif self.czasZdolnosci > 0 and self.czasZdolnosci < 3:
                chance = random.randrange(100)
                if chance >= 50:
                    for i in range(2):
                        if self.wykonajRuch() == False:
                            break
                    self.czasZdolnosci = self.czasZdolnosci - 1
                else:
                    self.czasZdolnosci = self.czasZdolnosci - 1
                    self.wykonajRuch()
        else:
            self.wykonajRuch()

    def getNazwa(self):
        return "Czlowiek"

    def Dziecko(self, x, y):
        return Czlowiek(self.swiat, x, y)




