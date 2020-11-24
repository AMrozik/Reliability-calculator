#!/usr/bin/python3

"""main.py: Importuje moduły rozwiązujące poszczególne zadania
 oraz tworzy CLI do wyboru konkretnego problemu przez użytkownika."""

__author__ = "Kamil Skrzypkowski, Andrzej Mrozik"
__credits__ = ["Paweł Czapiewski"]
__version__ = "1.0.1"
__maintainer__ = "Andrzej Mrozik"
__email__ = "andrzej.mrozik98@gmail.com"
__status__ = "Production"

import find_reliability_and_failure_rate_in_time_interval as z1
import reliability_after_certain_time as z2
import failure_rate_after_certain_hours as z3
import probability_of_operation_for_demanded_time as z4
import draw_plot_and_find_reliability_at_certain_time as z5


if __name__ == '__main__':
    while True:
        print("Podaj numer zadania (aby wyjsc wpisz 'exit')\n"
              "1: Liczenie reliability i falure rate w przedziale czasowym\n"
              "2: Liczenie reliability po okreslonym czasie\n"
              "3: Liczenie falure rate po okreslonym czasie\n"
              "4: oblicz prawdopodobieństwo, że urządzenie będzie działało bez przeszkód przez zadaną liczbę godzin "
              "mając MTBF.pdf\n"
              "5: Mając MTBF wyrysowuj funkcje reliability, następnie oblicz reliability, dla urzadzenia po "
              "okreslonej ilosci godzin.pdf")
        console_in = input(">")

        if console_in == "1":
            # zadanie 2 z pliku reliability.pdf
            if z1.solve() is None:
                print("Niepoprawne dane")
            input("Wciśnij klawisz Enter, aby kontynuować.")
            print()
        elif console_in == "2":
            # zadanie 3 z pliku reliability.pdf
            if z2.solve() is None:
                print("Niepoprawne dane")
            input("Wciśnij klawisz Enter, aby kontynuować.")
            print()
        elif console_in == "3":
            # zadanie 4 z pliku reliability.pdf
            if z3.solve() is None:
                print("Niepoprawne dane")
            input("Wciśnij klawisz Enter, aby kontynuować.")
            print()
        elif console_in == "4":
            # zadanie 5 z pliku reliability.pdf
            if z4.solve() is None:
                print("Niepoprawne dane")
            input("Wciśnij klawisz Enter, aby kontynuować.")
            print()
        elif console_in == "5":
            # zadanie 6 z pliku reliability.pdf
            if z5.solve() is None:
                print("Niepoprawne dane")
            input("Wciśnij klawisz Enter, aby kontynuować.")
            print()
        # exits program loop
        elif console_in == "exit":
            break
