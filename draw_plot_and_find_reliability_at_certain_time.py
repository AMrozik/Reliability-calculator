#!/usr/bin/python3

"""
draw_plot_and_find_reliability_at_certain_time.py: Rozwiązuje zadanie 6 z pliku reliability.pdf.

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
import matplotlib.pyplot as plt


def load_data():
    """Pobiera dane od użytkownika z konsoli\n
        - Jeśli udało się sparsować dane do liczby rzeczywistej:
            zwraca krotkę (MTBF, time_without_failure)
        - Jeśli nie udało się sparsować danych:
            zwraca None
    """
    try:
        MTBF = float(input("Podaj MTBF: "))
        time_without_failure = float(input("Podaj żądany czas dla którego chcesz wyliczyc reliability: "))
        return MTBF, time_without_failure
    except ValueError and TypeError:
        return None


def reliability_function(failure_rate, time):
    """Funkcja reliability
    przyjmuje failure rate oraz czas
    zwraca wartość realibility dla podanych argumentów"""
    return exp(-time * failure_rate)


def solve():
    """Pobiera dane używając load_data().
     Mając MTBF wyrysowuje funkcje reliability,
     następnie oblicza reliability, dla urzadzenia po okreslonej ilosci godzin
     Zwraca wynik jako liczbę rzeczywistą
     Jeśli napotkano błąd zwraca None"""

    try:
        MTBF, time_without_failure = load_data()
        failure_rate = 1/MTBF
        x = list(range(int(MTBF)))
        y = []
        for value in x:
            y.append(reliability_function(failure_rate, value))
        plt.plot(x, y)
        plt.xlabel("time")
        plt.ylabel("reliability")
        plt.show()
        result = reliability_function(failure_rate, time_without_failure)
        print(f"reliability elementu o MTBF równym {MTBF},"
              f" po upływie {time_without_failure} wynosi: {round(result, 4)}")
        return result
    except TypeError and ZeroDivisionError and MemoryError and ValueError:
        return None
