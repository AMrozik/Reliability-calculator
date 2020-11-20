#!/usr/bin/python3

"""
failure_rate_after_certain_hours.py: Rozwiązuje zadanie 4 z pliku reliability.pdf.

What is the highest failure rate for a product if it is to have a reliability
(or probability of survival) of 98 percent at 5000 hours?
Assume that the time to failure follows an exponential distribution.
"""

__author__ = "Kamil Skrzypkowski, Andrzej Mrozik"
__credits__ = ["Paweł Czapiewski"]
__version__ = "1.0.1"
__maintainer__ = "Andrzej Mrozik"
__email__ = "andrzej.mrozik98@gmail.com"
__status__ = "Production"


from math import log


def load_data():
    """Zwraca dane pobrane od użytkownika z konsoli.\n
    - RETURN zwroci wartosc None jesli zle podamy dane wejsciowe.
    """
    try:
        reliability = float(input("Podaj reliability: "))
        time = float(input("Podaj żądany czas w godzinach dla ktorego chcesz sprawdzic reliability: "))
        return reliability, time
    except ValueError and TypeError:
        return None


def solve():
    """Wylicza maksymalny failure rate dla okreslonej liczby godzin.\n
    - RETURN zwraca failure rate
    - RETURN zwraca None gdy wystapi blad wczytywania danych
    """

    try:
        reliability, time = load_data()
        result = (log(reliability)/time) * -1
        print("Najwiekszy failure rate jest po okreslonym czasie jest rowny: ", result)
        return result
    except ZeroDivisionError and ValueError:
        return None
