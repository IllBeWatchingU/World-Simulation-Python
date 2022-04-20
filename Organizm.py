from abc import ABC, abstractmethod

class Organizm(ABC):
    def __init__(self, swiat, sila, inicjatywa, polozenieX, polozenieY, wiek, literaOrganizmu, image):
        self.swiat = swiat
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.polozenieX = polozenieX
        self.polozenieY = polozenieY
        self.wiek = wiek
        self.literaOrganizmu = literaOrganizmu
        self.image = image

    @property
    def sila(self):
        return self._sila

    @sila.setter
    def sila(self, sila):
        self._sila = sila

    @property
    def inicjatywa(self):
        return self._inicjatywa

    @inicjatywa.setter
    def inicjatywa(self, inicjatywa):
        self._inicjatywa = inicjatywa

    @property
    def polozenieX(self):
        return self._polozenieX

    @polozenieX.setter
    def polozenieX(self, polozenieX):
        self._polozenieX = polozenieX

    @property
    def polozenieY(self):
        return self._polozenieY

    @polozenieY.setter
    def polozenieY(self, polozenieY):
        self._polozenieY = polozenieY

    @property
    def literaOrganizmu(self):
        return self._literaOrganizmu

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, wiek):
        self._wiek = wiek

    @property
    def literaOrganizmu(self):
        return self._literaOrganizmu

    @literaOrganizmu.setter
    def literaOrganizmu(self, literaOrganizmu):
        self._literaOrganizmu = literaOrganizmu

    @abstractmethod
    def Akcja(self):
        pass

    @abstractmethod
    def Kolizja(self, atakujacy):
        pass

    @abstractmethod
    def getNazwa():
        pass

    @abstractmethod
    def Dziecko(self):
        pass





