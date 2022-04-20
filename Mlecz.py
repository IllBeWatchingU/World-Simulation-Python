from Roslina import Roslina

class Mlecz(Roslina):
    def __init__(self, swiat, polozenieX, polozenieY):
        super().__init__(swiat, 0, polozenieX, polozenieY, 'M', 'mlecz.png')

    def Akcja(self):
        for i in range(3):
            proba = self.ProbaRozmnozeniaSie()

            if proba == True:
                self.swiat.komentarze.append(self.getNazwa() + " rozmnaza sie")
                break
    
    def getNazwa(self):
        return "Mlecz"

    def Dziecko(self, x, y):
        return Mlecz(self.swiat, x, y)


