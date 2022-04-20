import pygame
import tkinter as tk
import os.path
import random
import operator
import copy
import math
from Antylopa import Antylopa
from BarszczSosnowskiego import BarszczSosnowskiego
from CyberOwca import CyberOwca
from Czlowiek import Czlowiek
from Guarana import Guarana
from Lis import Lis
from Mlecz import Mlecz
from Owca import Owca
from Trawa import Trawa
from WilczeJagody import WilczeJagody
from Wilk import Wilk
from Zolw import Zolw

class Swiat:
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.tura = 0
        self.organizmy = []
        self.komentarze = []
        self.tablicaSwiata = [['0' for i in range(wysokosc)] for j in range(szerokosc)]
        self.ruchCzlowieka = 0

        self.menu = True
        self.game = False
        self.screenWidth = 600
        self.screenHeight = 735

        self.window = tk.Tk()

        self.scroll = tk.Scrollbar(self.window, orient="vertical")
        self.listbox=tk.Listbox(self.window, width = 40, height = 30, yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.listbox.yview)

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        self.scroll.grid(row=0, column=1, sticky='ns')
        self.listbox.grid(row=0, column=0, sticky="nsew")

        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        pygame.display.set_caption("Projekt 2 184707")

        self.smallfont = pygame.font.SysFont('Corbel',18)
        self.bigfont = pygame.font.SysFont('Corbel', 35)

        self.wyborOrganizmu = "antylopa"

        self.list = ['antylopa',
                'barszcz',
                'cyberowca',
                'guarana',
                'lis',
                'mlecz',
                'owca',
                'trawa',
                'jagody',
                'wilk',
                'zolw',
                'czlowiek'
                ]

    def czyPoleJestPuste(self, x, y):
        if self.tablicaSwiata[y][x] == '0':
            return True
        else:
            return False

    # zwraca True jeśli nie ma wolnego pola dookoła pola (x,y), w przeciwnym razie zwraca False
    def czyWszystkiePolaZajete(self, x, y):
        north = y - 1
        south = y + 1
        west = x - 1
        east = x + 1

        if north < 0:
            isNorthEmpty = False
        else:
            isNorthEmpty = self.czyPoleJestPuste(x, north)

        if south >= self.wysokosc:
            isSouthEmpty = False
        else:
            isSouthEmpty = self.czyPoleJestPuste(x, south)

        if west < 0:
            isWestEmpty = False
        else:
            isWestEmpty = self.czyPoleJestPuste(x, west)

        if east >= self.szerokosc:
            isEastEmpty = False
        else:
            isEastEmpty = self.czyPoleJestPuste(x, east)

        if isNorthEmpty is False and isSouthEmpty is False and isWestEmpty is False and isEastEmpty is False:
            return True
        else:
            return False

    def czyOrganizmJestZwierzeciem(self, organizm):
        if organizm is None:
            return False
        test = organizm.literaOrganizmu
        if test == 'W' or test == 'O' or test == 'C' or test == 'Z' or test == 'A' or test == 'L':
            return True
        else:
            return False

    def czyOrganizmJestCyberOwca(self, organizm):
        if organizm is None:
            return False
        test = organizm.literaOrganizmu
        if test == 'R':
            return True
        else:
            return False

    def inicjujSwiat(self):
        for i in range(1,12):
            chance = random.randrange(3) + 1
            j = 0
            while j < chance:
                randomX = random.randrange(self.szerokosc)
                randomY = random.randrange(self.wysokosc)

                if self.czyPoleJestPuste(randomX, randomY):
                    j = j + 1

                    if i == 1:
                        organizm = Wilk(self, randomX, randomY)
                    elif i == 2:
                        organizm = Owca(self, randomX, randomY)
                    elif i == 3:
                        organizm = Lis(self, randomX, randomY)
                    elif i == 4:
                        organizm = Zolw(self, randomX, randomY)
                    elif i == 5:
                        organizm = Antylopa(self, randomX, randomY)
                    elif i == 6:
                        organizm = CyberOwca(self, randomX, randomY)
                    elif i == 7:
                        organizm = Trawa(self, randomX, randomY)
                    elif i == 8:
                        organizm = Mlecz(self, randomX, randomY)
                    elif i == 9:
                        organizm = Guarana(self, randomX, randomY)
                    elif i == 10:
                        organizm = WilczeJagody(self, randomX, randomY)
                    elif i == 11:
                        organizm = BarszczSosnowskiego(self, randomX, randomY)

                    self.organizmy.append(organizm)
                    self.tablicaSwiata[randomY][randomX] = organizm.literaOrganizmu

        while True:
            randomX = random.randrange(self.szerokosc)
            randomY = random.randrange(self.wysokosc)
            if self.czyPoleJestPuste(randomX, randomY):
                organizm = Czlowiek(self, randomX, randomY)
                self.organizmy.append(organizm)
                self.tablicaSwiata[randomY][randomX] = organizm.literaOrganizmu
                break

        self.postarzOrganizmy()
        self.sortujOrganizmy()

    def sortujOrganizmy(self):
        self.organizmy.sort(key=operator.attrgetter('inicjatywa'), reverse=True)
        for i in range(1,len(self.organizmy)):
            if self.organizmy[i].inicjatywa == self.organizmy[i-1].inicjatywa:
                if self.organizmy[i].wiek > self.organizmy[i-1].wiek:
                    self.organizmy[i], self.organizmy[i-1] = self.organizmy[i], self.organizmy[i]

    # zwraca organizm znajdujący się na współrzędnych (x,y)
    def getOrganizm(self, x, y):
        for i in range(0,len(self.organizmy)):
            if self.organizmy[i].polozenieX == x and self.organizmy[i].polozenieY == y:
                return self.organizmy[i]

    # zwraca człowieka
    def getCzlowiek(self):
        for i in range(0, len(self.organizmy)):
            if self.organizmy[i].literaOrganizmu == "C":
                return self.organizmy[i]

    @property
    def ruchCzlowieka(self):
        return self._ruchCzlowieka

    @ruchCzlowieka.setter
    def ruchCzlowieka(self, ruchCzlowieka):
        self._ruchCzlowieka = ruchCzlowieka

    # funkcja sprawdzająca, czy gracz nie chce sterować człowiekiem poza planszę
    def sprawdzRuchCzlowieka(self):
        czlowiek = self.getCzlowiek()
        if czlowiek is not None:
            if self.ruchCzlowieka == 1:
                if czlowiek.polozenieY == 0:
                    self.ruchCzlowieka = 0
            elif self.ruchCzlowieka == 2:
                if czlowiek.polozenieY == self.wysokosc - 1:
                    self.ruchCzlowieka = 0
            elif self.ruchCzlowieka == 3:
                if czlowiek.polozenieX == 0:
                    self.ruchCzlowieka = 0
            elif self.ruchCzlowieka == 4:
                if czlowiek.polozenieX == self.szerokosc - 1:
                    self.ruchCzlowieka = 0
            else:
                self.ruchCzlowieka = 0
        else:
            self.ruchCzlowieka = 0

    @property
    def tura(self):
        return self._tura

    @tura.setter
    def tura(self, tura):
        self._tura = tura

    def czyCzlowiekZyje(self):
        organizm = self.getCzlowiek()
        if organizm is not None:
            return True
        return False

    def czyBarszczIstnieje(self):
        for i in range(len(self.organizmy)):
            if self.organizmy[i].literaOrganizmu == 'B':
                return True

        return False

    def aktywujUmiejetnoscCzlowieka(self):
        organizm = self.getCzlowiek()
        if organizm is not None:
            if organizm.aktywujUmiejetnosc():
                return True
            else:
                return False
        else:
            return False

    # znajduje najbliższy barszcz od cyberowcy
    def znajdzNajblizszyBarszcz(self, organizm):
        x = -1
        y = -1
        deltaX = -1
        deltaY = -1
        odl = -1

        for i in range(len(self.organizmy)):
            if self.organizmy[i].literaOrganizmu == "B":
                if deltaX == -1 or deltaY == -1:
                    # obliczanie odleglosci pierwszego barszczu
                    deltaX = abs(self.organizmy[i].polozenieX - organizm.polozenieX)
                    deltaY = abs(self.organizmy[i].polozenieY - organizm.polozenieY)
                    x = self.organizmy[i].polozenieX
                    y = self.organizmy[i].polozenieY
                    odl = math.sqrt(pow(deltaX, 2) + pow(deltaY, 2))

                # obliczanie odleglosci każdego kolejnego barszczu i porównywanie z najkrótszą odległością
                tempDeltaX = abs(self.organizmy[i].polozenieX - organizm.polozenieX)
                tempDeltaY = abs(self.organizmy[i].polozenieY - organizm.polozenieY)
                odlTemp = math.sqrt(pow(tempDeltaX, 2) + pow(tempDeltaY, 2))

                if odlTemp < odl:
                    x = self.organizmy[i].polozenieX
                    y = self.organizmy[i].polozenieY
                    odlTemp = odl

        organizm.doceloweX = x
        organizm.doceloweY = y

    # zabija organizmy o inicjatywie mniejszej od 0
    def zabijOrganizmy(self):
        i = 0
        ran = len(self.organizmy)
        while i < ran:
            if self.organizmy[i].inicjatywa < 0:
                self.organizmy.pop(i)
                ran -= 1
            i += 1

    # postarza organizmy co turę
    def postarzOrganizmy(self):
        for i in range(0, len(self.organizmy)):
            temp = self.organizmy[i].wiek
            temp = temp + 1
            self.organizmy[i].wiek = temp

    # funkcja do dodawania organizmów klikając myszką na puste pole na planszy
    def dodajOrganizmMyszka(self, x, y):
        if self.wyborOrganizmu == 'wilk':
            nowyOrganizm = Wilk(self, x, y)
        elif self.wyborOrganizmu == 'owca':
            nowyOrganizm = Owca(self, x, y)
        elif self.wyborOrganizmu == 'antylopa':
            nowyOrganizm = Antylopa(self, x, y)
        elif self.wyborOrganizmu == 'barszcz':
            nowyOrganizm = BarszczSosnowskiego(self, x, y)
        elif self.wyborOrganizmu == 'cyberowca':
            nowyOrganizm = CyberOwca(self, x, y)
        elif self.wyborOrganizmu == 'czlowiek':
            nowyOrganizm = Czlowiek(self, x, y)
        elif self.wyborOrganizmu == 'guarana':
            nowyOrganizm = Guarana(self, x, y)
        elif self.wyborOrganizmu == 'lis':
            nowyOrganizm = Lis(self, x, y)
        elif self.wyborOrganizmu == 'mlecz':
            nowyOrganizm = Mlecz(self, x, y)
        elif self.wyborOrganizmu == 'trawa':
            nowyOrganizm = Trawa(self, x, y)
        elif self.wyborOrganizmu == 'jagody':
            nowyOrganizm = WilczeJagody(self, x, y)
        elif self.wyborOrganizmu == 'zolw':
            nowyOrganizm = Zolw(self, x, y)
        elif self.wyborOrganizmu == 'czlowiek':
            nowyOrganizm = Czlowiek(self, x, y)

        nowyOrganizm.wiek = 1
        self.dodajOrganizm(nowyOrganizm)
        self.dodajOrganizmDoPola(nowyOrganizm, x, y)
        if self.wyborOrganizmu == 'czlowiek':
            self.wyborOrganizmu = 'antylopa'

    def dodajOrganizm(self, nowyOrganizm):
        self.organizmy.append(nowyOrganizm)

    # zwraca losowe pole, może być zajęte, wokół organizmu
    def getLosowePole(self, organizm):
        losowe = [1 , 2, 3, 4]
        size = 4
        random.shuffle(losowe)
        losowePole = losowe[0]
        while size != 0:
            if losowePole == 1:
                if organizm.polozenieY != 0:
                    return 1
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

            elif losowePole == 2:
                if organizm.polozenieY != self.wysokosc - 1:
                    return 2
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

            elif losowePole == 3:
                if organizm.polozenieX != 0:
                    return 3
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

            elif losowePole == 4:
                if organizm.polozenieX != self.szerokosc - 1:
                    return 4
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

        return 0

    # zwraca pole dookoła organizmu, jeśli jest puste albo stoi na nim organizm, który ma mniejszą siłę
    def getLosowePoleMniejszegoSila(self, organizm):
        losowe = [1 , 2, 3, 4]
        size = 4
        random.shuffle(losowe)
        losowePole = losowe[0]
        while size != 0:
            if losowePole == 1:
                if organizm.polozenieY != 0:
                    if self.czyPoleJestPuste(organizm.polozenieX, organizm.polozenieY - 1) == False:
                        naPolu = self.getOrganizm(organizm.polozenieX, organizm.polozenieY - 1)
                        if naPolu.sila < organizm.sila:
                            return 1
                    else:
                        return 1
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

            elif losowePole == 2:
                if organizm.polozenieY != self.wysokosc - 1:
                    if self.czyPoleJestPuste(organizm.polozenieX, organizm.polozenieY + 1) == False:
                        naPolu = self.getOrganizm(organizm.polozenieX, organizm.polozenieY + 1)
                        if naPolu.sila < organizm.sila:
                            return 2
                    else: 
                        return 2
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

            elif losowePole == 3:
                if organizm.polozenieX != 0:
                    if self.czyPoleJestPuste(organizm.polozenieX - 1, organizm.polozenieY) == False:
                        naPolu = self.getOrganizm(organizm.polozenieX - 1, organizm.polozenieY)
                        if naPolu.sila < organizm.sila:
                            return 3
                    else: 
                        return 3
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

            elif losowePole == 4:
                if organizm.polozenieX != self.szerokosc - 1:
                    if self.czyPoleJestPuste(organizm.polozenieX + 1, organizm.polozenieY) == False:
                        naPolu = self.getOrganizm(organizm.polozenieX + 1, organizm.polozenieY)
                        if naPolu.sila < organizm.sila:
                            return 4
                    else:
                        return 4
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

        return 0

    # zwraca losowe puste pole dookoła organizmu
    def getLosowePustePole(self, organizm):
        losowe = [1 , 2, 3, 4]
        size = 4
        random.shuffle(losowe)
        losowePole = losowe[0]
        while size != 0:
            if losowePole == 1:
                if organizm.polozenieY != 0:
                    if self.tablicaSwiata[organizm.polozenieY - 1][organizm.polozenieX] == '0':
                        return 1
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1
            elif losowePole == 2:
                if organizm.polozenieY != self.wysokosc - 1:
                    if self.tablicaSwiata[organizm.polozenieY + 1][organizm.polozenieX] == '0':
                        return 2
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1
            elif losowePole == 3:
                if organizm.polozenieX != 0:
                    if self.tablicaSwiata[organizm.polozenieY][organizm.polozenieX - 1] == '0':
                        return 3
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1
            elif losowePole == 4:
                if organizm.polozenieX != self.szerokosc - 1:
                    if self.tablicaSwiata[organizm.polozenieY][organizm.polozenieX + 1] == '0':
                        return 4
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

        return 0

    # zwraca losowe puste pole albo dookoła organizmu, albo jego partnera
    def getLosowePustePoleDlaObuOrganizmow(self, organizm, partner):
        losowe = [1 , 2, 3, 4]
        size = 4
        random.shuffle(losowe)
        losowePole = losowe[0]
        while size != 0:
            if losowePole == 1:
                if organizm.polozenieY != 0:
                    if self.tablicaSwiata[organizm.polozenieY - 1][organizm.polozenieX] == '0':
                        return 1
                elif partner.polozenieY != 0:
                    if self.tablicaSwiata[partner.polozenieY - 1][partner.polozenieX] == '0':
                        return 5
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1
            elif losowePole == 2:
                if organizm.polozenieY != self.wysokosc - 1:
                    if self.tablicaSwiata[organizm.polozenieY + 1][organizm.polozenieX] == '0':
                        return 2
                elif partner.polozenieY != self.wysokosc - 1:
                    if self.tablicaSwiata[partner.polozenieY + 1][partner.polozenieX] == '0':
                        return 6
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1
            elif losowePole == 3:
                if organizm.polozenieX != 0:
                    if self.tablicaSwiata[organizm.polozenieY][organizm.polozenieX - 1] == '0':
                        return 3
                elif partner.polozenieX != 0:
                    if self.tablicaSwiata[partner.polozenieY][partner.polozenieX - 1] == '0':
                        return 7
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1
            elif losowePole == 4:
                if organizm.polozenieX != self.szerokosc - 1:
                    if self.tablicaSwiata[organizm.polozenieY][organizm.polozenieX + 1] == '0':
                        return 4
                elif partner.polozenieX != self.szerokosc - 1:
                    if self.tablicaSwiata[partner.polozenieY][partner.polozenieX + 1] == '0':
                        return 8
                elif size == 1:
                    losowe.pop(0)
                else:
                    losowe.pop(0)
                    losowePole = losowe[0]
                size -= 1

        return 0

    def usunOrganizmZPola(self, organizm):
        self.tablicaSwiata[organizm.polozenieY][organizm.polozenieX] = '0'

    def dodajOrganizmDoPola(self, organizm, x, y):
        self.tablicaSwiata[y][x] = organizm.literaOrganizmu

    def wyczyscKomentarze(self):
        self.komentarze.clear()

    def wykonajTure(self):
        i = 0
        ran = len(self.organizmy)
        while i < ran:
            if self.organizmy[i].inicjatywa >= 0 and self.organizmy[i].wiek > 0:
                self.organizmy[i].Akcja()
            if self.organizmy[i].inicjatywa < 0:
                ran -= 1
            i += 1
        self.zabijOrganizmy()
        self.postarzOrganizmy()
        self.sortujOrganizmy()
        self.tura += 1

    # zapisuje stan gry do pliku .txt
    def zapiszDoPliku(self):
        file = open(r"save.txt", "w")

        file.write(str(self.tura) + "\n")
        
        for i in range(len(self.organizmy)):
            string = self.organizmy[i].literaOrganizmu + " " + str(self.organizmy[i].sila) + " " + str(self.organizmy[i].polozenieX) + " " + str(self.organizmy[i].polozenieY) + " " + str(self.organizmy[i].wiek) + "\n"
            file.write(string)

    # wczytuje stan gry z pliku .txt
    def wczytajZPliku(self):
        file = open(r"save.txt", "r")

        tura = file.readline()
        self.tura = int(tura)

        next(file)
        for line in file:
            string = file.readline()
            info = string.split()
            if len(info) == 0:
                return
            x = int(info[2])
       
            y = int(info[3])
            if info[0] == 'W':
                nowyOrganizm = Wilk(self, x, y)
            elif info[0] == 'O':
                nowyOrganizm = Owca(self, x, y)
            elif info[0] == 'A':
                nowyOrganizm = Antylopa(self, x, y)
            elif info[0] == 'B':
                nowyOrganizm = BarszczSosnowskiego(self, x, y)
            elif info[0] == 'R':
                nowyOrganizm = CyberOwca(self, x, y)
            elif info[0] == 'C':
                nowyOrganizm = Czlowiek(self, x, y)
            elif info[0] == 'G':
                nowyOrganizm = Guarana(self, x, y)
            elif info[0] == 'L':
                nowyOrganizm = Lis(self, x, y)
            elif info[0] == 'M':
                nowyOrganizm = Mlecz(self, x, y)
            elif info[0] == 'T':
                nowyOrganizm = Trawa(self, x, y)
            elif info[0] == 'J':
                nowyOrganizm = WilczeJagody(self, x, y)
            elif info[0] == 'Z':
                nowyOrganizm = Zolw(self, x, y)

            sila = int(info[1])
            wiek = int(info[4])
            nowyOrganizm.sila = sila
            nowyOrganizm.wiek = wiek
            self.dodajOrganizmDoPola(nowyOrganizm, x, y)
            self.organizmy.append(nowyOrganizm)

        self.sortujOrganizmy()
        file.close()

    # tutaj są wszystkie funkcje związane z graficzną reprezentacją

    # rysuje wybór zwierząt
    def rysujWybor(self):
        for i in range(len(self.list)):
            pixelX = i * 30
            pixelY = 700
            name = self.list[i] + ".png"
            icon = pygame.image.load(name)
            self.screen.blit(icon,(pixelX, pixelY))

    # dodaje komentarze do listboxa
    def addComments(self):
        for i in range(len(self.komentarze)):
            self.listbox.insert('end', self.komentarze[i])

    # rysuje ikony organizmów na planszy
    def rysujSwiat(self):
        for i in range(len(self.organizmy)):
            pixelX = self.organizmy[i].polozenieX * 30
            pixelY = self.organizmy[i].polozenieY * 30
            icon = pygame.image.load(self.organizmy[i].image)
            self.screen.blit(icon,(pixelX, pixelY))

    # pętla, w której wyświetla się menu główne
    def menuGlowne(self):
        while self.menu == True:

            self.screen.fill((242,189,186))

            # renderowanie napisów 
            self.screen.blit(self.bigfont.render("N - nowa gra", True, (0,0,0)), (170, 165))
            self.screen.blit(self.bigfont.render("L - laduj gre", True, (0,0,0)), (170, 255))
            self.screen.blit(self.bigfont.render("Q - wyjdz", True, (0,0,0)), (170, 350))

            self.window.update()
            pygame.display.update()

            # czytanie klawiatury
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n:
                        self.inicjujSwiat()
                        self.menu = False
                        self.game = True

                    elif event.key == pygame.K_l:
                        if os.path.isfile("save.txt"):
                            self.wczytajZPliku()
                        else:
                            self.inicjujSwiat()
                        self.menu = False
                        self.game = True

                    elif event.key == pygame.K_q:
                        self.menu = False

    # główna pętla symulacji
    def symulacja(self):
        while self.game == True:
            textTura = "tura: " + str(self.tura)
            textOrganizmy = "organizmy:" + str(len(self.organizmy))
            textChoice = "Wybrano: " + self.wyborOrganizmu
            self.screen.fill((213,219,212))
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(self.screen,(196,214,214),[0,600, 600, 165])
            self.screen.blit(self.smallfont.render(textChoice, True, (0,0,0)), (410, 617))
            self.screen.blit(self.smallfont.render(textTura, True, (0,0,0)), (50, 617))
            self.screen.blit(self.smallfont.render(textOrganizmy, True, (0,0,0)), (50, 637))
            self.screen.blit(self.smallfont.render("Wybierz organizm do dodania:", True, (0,0,0)), (0, 677))
            self.rysujSwiat()
            self.rysujWybor()
            self.window.update()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        if self.aktywujUmiejetnoscCzlowieka():
                            self.listbox.delete(0, 'end')
                            self.listbox.insert('end', "Zdolnosc czlowieka zostala aktywowana!")
                        else:
                            self.listbox.delete(0, 'end')
                            self.listbox.insert('end', "Zdolnosc czlowieka nie mogła byc aktywowana!")
                    if event.key == pygame.K_DOWN:
                        self.ruchCzlowieka = 2
                        self.sprawdzRuchCzlowieka()
                        self.listbox.delete(0, 'end')
                        self.wykonajTure()
                        self.addComments()
                        self.wyczyscKomentarze()
                    elif event.key == pygame.K_UP:
                        self.ruchCzlowieka = 1
                        self.sprawdzRuchCzlowieka()
                        self.listbox.delete(0, 'end')
                        self.wykonajTure()
                        self.addComments()
                        self.wyczyscKomentarze()
                    elif event.key == pygame.K_LEFT:
                        self.ruchCzlowieka = 3
                        self.sprawdzRuchCzlowieka()
                        self.listbox.delete(0, 'end')
                        self.wykonajTure()
                        self.addComments()
                        self.wyczyscKomentarze()
                    elif event.key == pygame.K_RIGHT:
                        self.ruchCzlowieka = 4
                        self.sprawdzRuchCzlowieka()
                        self.listbox.delete(0, 'end')
                        self.wykonajTure()
                        self.addComments()
                    elif event.key == pygame.K_n:
                        self.listbox.delete(0, 'end')
                        self.wykonajTure()
                        self.addComments()
                    elif event.key == pygame.K_s:
                        self.zapiszDoPliku()
                        self.listbox.insert('end', "Gra zostala zapisana!")
                    elif event.key == pygame.K_q:
                        self.game = False
                self.wyczyscKomentarze()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 600 and 0 <= mouse[1] <= 600:
                        posX = mouse[0]//30
                        posY = mouse[1]//30
                        if self.czyPoleJestPuste(posX, posY) == False:
                            self.listbox.insert('end', "Nie mozna dodac organizmu na zajete pole!")
                        else:
                            self.dodajOrganizmMyszka(posX, posY)
                            self.listbox.insert('end', "Dodano organizm!")
                    elif 0 <= mouse [0] <= len(self.list)*30 and 700 <= mouse[1] <= 730:
                        choiceX = mouse[0]//30
                        if self.list[choiceX] == 'czlowiek' and self.czyCzlowiekZyje():
                            self.listbox.insert('end', "Nie mozna wybrac czlowieka, jesli drugi zyje!")
                        else:
                            self.wyborOrganizmu = self.list[choiceX]
                        












