from Roslina import Roslina

class BarszczSosnowskiego(Roslina):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 10, polozenieX, polozenieY, 'B', 'barszcz.png')

    def Akcja(self):
        if self.polozenieY != 0:
            if self.swiat.czyPoleJestPuste(self.polozenieX, self.polozenieY - 1) == False:
                organizm = self.swiat.getOrganizm(self.polozenieX, self.polozenieY - 1)
                if self.swiat.czyOrganizmJestZwierzeciem(organizm):
                    self.swiat.usunOrganizmZPola(organizm)
                    organizm.inicjatywa = -1
                    self.swiat.komentarze.append(self.getNazwa() + " zabija " + organizm.getNazwa())

        if self.polozenieY != self.swiat.wysokosc - 1:
            if self.swiat.czyPoleJestPuste(self.polozenieX, self.polozenieY + 1) == False:
                organizm = self.swiat.getOrganizm(self.polozenieX, self.polozenieY + 1)
                if self.swiat.czyOrganizmJestZwierzeciem(organizm):
                    self.swiat.usunOrganizmZPola(organizm)
                    organizm.inicjatywa = -1
                    self.swiat.komentarze.append(self.getNazwa() + " zabija " + organizm.getNazwa())

        if self.polozenieX != 0:
            if self.swiat.czyPoleJestPuste(self.polozenieX - 1, self.polozenieY) == False:
                organizm = self.swiat.getOrganizm(self.polozenieX - 1, self.polozenieY)
                if self.swiat.czyOrganizmJestZwierzeciem(organizm):
                    self.swiat.usunOrganizmZPola(organizm)
                    organizm.inicjatywa = -1
                    self.swiat.komentarze.append(self.getNazwa() + " zabija " + organizm.getNazwa())

        if self.polozenieX != self.swiat.szerokosc - 1:
            if self.swiat.czyPoleJestPuste(self.polozenieX + 1, self.polozenieY) == False:
                organizm = self.swiat.getOrganizm(self.polozenieX + 1, self.polozenieY)
                if self.swiat.czyOrganizmJestZwierzeciem(organizm):
                    self.swiat.usunOrganizmZPola(organizm)
                    organizm.inicjatywa = -1
                    self.swiat.komentarze.append(self.getNazwa() + " zabija " + organizm.getNazwa())

        if self.ProbaRozmnozeniaSie():
            self.swiat.komentarze.append(self.getNazwa() + " rozmnaza sie")
    
    def Kolizja(self, atakujacy):
        # jeśli organizmem atakującym jest cyberowca, to barszcz ginie
        if self.swiat.czyOrganizmJestCyberOwca(atakujacy):
            self.swiat.komentarze.append(atakujacy.getNazwa() + " zjada " + self.getNazwa())
            self.swiat.usunOrganizmZPola(self)
            self.inicjatywa = -1
            return True
        # w przeciwnym wypadku oba organizmy giną
        else:
            self.swiat.komentarze.append(atakujacy.getNazwa() + " probuje zjesc " + self.getNazwa() + " i ginie")
            self.swiat.usunOrganizmZPola(self)
            self.swiat.usunOrganizmZPola(atakujacy)
            atakujacy.inicjatywa = -1
            self.inicjatywa = -1
            return False

    def getNazwa(self):
        return "Barszcz Sosnowskiego"

    def Dziecko(self, x, y):
        return BarszczSosnowskiego(self.swiat, x, y)


