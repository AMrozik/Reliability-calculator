#!/usr/bin/python3

"""
probability_of_operation_for_demanded_time.py: Rozwiązuje zadanie 5 z pliku reliability.pdf.

The equipment in a packaging plant has a MTBF of 1000 hours. What is the probability that
the equipment will operate for a period of 500 hours without failure?
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
            zwraca krotkę (MTBF, demanded_time_without_failure)
        - Jeśli nie udało się sparsować danych:
            zwraca None
    """
    try:
        MTBF = float(input("Podaj MTBF: "))
        demanded_time_without_failure = float(input("Podaj żądany czas w godzinach "
                                                    "w jakim urządzenie ma działać bez usterek: "))
        return MTBF, demanded_time_without_failure
    except ValueError:
        return None


def solve():
    """Pobiera dane używając load_data().
     Mając MTBF oblicza prawdopodobieństwo,
     że urządzenie będzie działało bez przeszkód przez zadaną liczbę godzin
     Zwraca wynik jako liczbę rzeczywistą
     Jeśli napotkano błąd zwraca None"""

    try:
        MTBF, time_without_failure = load_data()
    except TypeError:
        return None

    if MTBF != 0:
        failure_rate = 1/MTBF
        R = exp(-time_without_failure * failure_rate)
        print("failure rate:", round(R, 2))
        return R
    else:
        return None
