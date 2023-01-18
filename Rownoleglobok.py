import math


class Rownoleglobok:
    bok1: int
    bok2: int
    kat: int

    def __init__(self, bok1: int, bok2: int, kat: int) -> None:
        self.bok1 = bok1
        self.bok2 = bok2
        self.kat = kat
        if bok1 < 0 or bok1 > 100 or bok2 < 0 or bok2 > 100 or kat < 0 or kat > 180:
            print("Zle parametry")

    def pobierz_pole(self) -> float:
        return self.bok1 * self.bok2 * (math.sin(self.kat))

    def pobierz_obwod(self) -> float:
        return (2 * self.bok1) + (2 * self.bok2)

    def duplikuj_ze_skala(self) -> None:
        skala: int


    def skrocone(self) -> str:
        return f"{self.bok1} {self.bok2} {self.kat}"
