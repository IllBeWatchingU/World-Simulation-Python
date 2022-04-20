from Roslina import Roslina

class Guarana(Roslina):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 0, polozenieX, polozenieY, 'G', 'guarana.png')
    
    def Kolizja(self, atakujacy):
        self.swiat.komentarze.append(atakujacy.getNazwa() + " zjada " + self.getNazwa())
        nowaSila = atakujacy.sila
        nowaSila = nowaSila + 3
        atakujacy.sila = nowaSila
        self.swiat.usunOrganizmZPola(self)
        self.inicjatywa = -1
        return True

    def getNazwa(self):
        return "Guarana"

    def Dziecko(self, x, y):
        return Guarana(self.swiat, x, y)


