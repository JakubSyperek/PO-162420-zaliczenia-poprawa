from Rownoleglobok import Rownoleglobok


class Kwadrat(Rownoleglobok):
    __kolor: str

    @Override
    def __init__(self, bok1: int, bok2: int, kat: int, kolor: str) -> None:
        super().__init__(bok1, bok2, kat)
        self.__kolor = kolor
        if kolor == "" or bok1 < 0 or bok1 > 100 or bok2 < 0 or bok2 > 100:
            print("Zle parametry")

    ##@staticmethod
    ##def generuj_metody(self) -> str:
    ##    kolor: Lista[int]= [czerwony, zielony, niebieski, rozowy, bialy]


    #@Override
    def __opis__(self, other: Rownoleglobok) -> str:
        return f"dlugosc boku: {self.bok1}, kolor: {self.__kolor}, obwod: {s}"
