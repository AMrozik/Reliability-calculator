#!/usr/bin/python3

"""
find_reliability_and_failure_rate_in_time_interval.py: Rozwiązuje zadanie 2 z pliku reliability.pdf.

One thousand transistors are placed on life test, and the number of failures in each time interval are recorded.
    Find the reliability and the failure rate at 0, 100, 200, etc hours.
    (You may find it helpful to set this up on a spreadsheet.)
    Time interval   Number of failures\n
    0-100           160\n
    100-200         86\n
    200-300         78\n
    300-400         70\n
    400-500         64\n
    500-600         58\n
    600-700         52\n
    700-800         43\n
    800-900         42\n
    900-1000        36\n
    Draw a graph to show the change in the failure rate as the transistors get older.
    Do you think this component shows the bath tub pattern of failure?
    Draw a graph to show how the reliability changes over time.
"""

__author__ = "Kamil Skrzypkowski, Andrzej Mrozik"
__credits__ = ["Paweł Czapiewski"]
__version__ = "1.0.1"
__maintainer__ = "Andrzej Mrozik"
__email__ = "andrzej.mrozik98@gmail.com"
__status__ = "Production"


import matplotlib.pyplot as plt


# jak dam zero to dostaje jakieś useless wykresy

def reliability(number_of_survivors, number_of_items):
    """Zwraca wyliczone reliability.\n
    - number_of_survivors - ilosc obiektow ktora przetrwala
    - number_of_items - ilosc wszystkich obiektow
    """
    if number_of_items != 0:
        return number_of_survivors/number_of_items


def failure_rate(failures, survivors, time_interval):
    """Zwraca wyliczony failure rate.\n
    - failures - ilosc elementow ktore sie zepsuly w czasie\n
    - survivors - pozostala ilosc przedmiotow\n
    - time_interval - interwal czasu w ktorym nastapil pomiar zniczen
    """
    if survivors * time_interval != 0:
        return failures/(survivors * time_interval)


def load_data():
    """Zwraca pobrane dane od użytkownika\n
        - RETURN zwraca None jezeli nie znajdzie pliku lub jezeli nie uda sie wczytac danych.
    """
    try:
        file = open("time_failures_tab.txt", "r")
    except FileNotFoundError:
        print("Nie znaleziono pliku time_failures_tab")
        return None

    try:
        transistors_amount = int(input("Podaj ilosc tranzystorow: "))

    except ValueError and TypeError:
        print("Blad podanej wartosci tranzystorow")
        return None

    time_failures_tab = []
    try:
        for line in file:
            time_failures_tab.append(line.split(",", 3))

        return transistors_amount, time_failures_tab
    except ValueError:
        print("Blad wczytywania danych z pliku")
        return None


def solve():
    """Pobiera dane za pomoca load_data(), wylicza failure rate oraz pokazuje go na wykresie.\n
    - RETURN metoda zwraca tablice reliabilit, failure rates i time. Tablica time slozy do przedstawiania tych tanych w czasie.
    - RETURN zwraca None jezeli nie udalo sie wczytac zmiennych.
    """
    try:
        transistors_amount, time_failures_tab = load_data()

    # failed_amount holds number of already dead transistors and failure_rates_time is for displaying plots

    # jak w pliku jest float to wybuchnie

        failed_amount = 0
        failure_rates = []
        failure_rates_time = []
        reliability_time = []
        for time_start, time_end, failures in time_failures_tab:
            failed_amount += int(failures)
            failure_rates.append([failure_rate(int(failures), transistors_amount - failed_amount, float(time_end) - float(time_start))])
            failure_rates_time.append(float(time_end))
            reliability_time.append(reliability(transistors_amount - failed_amount, transistors_amount))

        plt.plot(failure_rates_time, failure_rates)
        plt.xlabel("time")
        plt.ylabel("failure rates")
        plt.show()

        plt.plot(failure_rates_time, reliability_time)
        plt.xlabel("time")
        plt.ylabel("reliability")
        plt.show()
        return reliability_time, failure_rates, failure_rates_time

    except TypeError and ValueError:
        return None
