from Roslina import Roslina

class WilczeJagody(Roslina):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 99, polozenieX, polozenieY, 'J', 'jagody.png')
    
    def Kolizja(self, atakujacy):
        # jeśli wilcze jagody będą zaatakowane, oba organizmy giną
        self.swiat.komentarze.append(atakujacy.getNazwa() + " probuje zjesc " + self.getNazwa() + " i ginie")
        self.swiat.usunOrganizmZPola(self)
        self.swiat.usunOrganizmZPola(atakujacy)
        atakujacy.inicjatywa = -1
        self.inicjatywa = -1
        return False

    def getNazwa(self):
        return "Wilcze Jagody"

    def Dziecko(self, x, y):
        return WilczeJagody(self.swiat, x, y)


