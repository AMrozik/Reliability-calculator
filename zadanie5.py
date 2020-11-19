#!/usr/bin/python3

"""
find_reliability_after_certain_time.py: Rozwiązuje zadanie 6 z pliku reliability.pdf.

Suppose that a component we wish to model has a constant failure rate with a mean time
between failures of 25 hours? Find:-
    (a) The reliability function.
    (b) The reliability of the item at 30 hours.
"""

__author__ = "Kamil Skrzypkowski, Andrzej Mrozik"
__credits__ = ["Paweł Czapiewski"]
__version__ = "1.0.1"
__maintainer__ = "Andrzej Mrozik"
__email__ = "andrzej.mrozik98@gmail.com"
__status__ = "Production"


from math import exp


def load_data():
    """Pobiera dane od użytkownika z konsoli\n
        - Jeśli udało się sparsować dane do liczby rzeczywistej:
            zwraca krotkę (MTBF, time_without_failure)
        - Jeśli nie udało się sparsować danych:
            zwraca None
    """
    try:
        MTBF = float(input("Podaj MTBF: "))
        time_without_failure = float(input("Podaj żądany czas dla ktorego chcesz wyliczyc reliability: "))
        return MTBF, time_without_failure
    except ValueError:
        return None


def solve():
    """Pobiera dane używając load_data().
     Mając MTBF oblicza reliability, dla urzadzenia po okreslonej ilosci godzin
     Zwraca wynik jako liczbę rzeczywistą
     Jeśli napotkano błąd zwraca None"""

    try:
        MTBF, time_without_failure = load_data()
        failure_rate = 1/MTBF
        result = exp(-time_without_failure * failure_rate)
        print(f"failure rate: {round(result, 4)}")
        return result
    except TypeError:
        return None
