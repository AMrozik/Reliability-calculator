#!/usr/bin/python3

"""
reliability_after_certain_time.py: Rozwiązuje zadanie 3 z pliku reliability.pdf.

An industrial machine compresses natural gas into an interstate gas pipeline.
The compressor is on line 24 hours a day. (If the machine is down, a gas field has to be shut
down until the natural gas can be compressed, so down time is very expensive.)
The vendor knows that the compressor has a constant failure rate of 0.000001 failures/hr.
What is the operational reliability after 2500 hours of continuous service?
"""

__author__ = "Kamil Skrzypkowski, Andrzej Mrozik"
__credits__ = ["Paweł Czapiewski"]
__version__ = "1.0.1"
__maintainer__ = "Andrzej Mrozik"
__email__ = "andrzej.mrozik98@gmail.com"
__status__ = "Production"


from math import exp


def load_data():
    """Zwraca dane pobrane od użytkownika z konsoli.\n
    - RETURN zwraca None dla zle sparsowanych danych wejsciowych
    """
    try:
        reliability = float(input("Podaj failure rate: "))
        time = int(input("Podaj żądany czas w godzinach dla ktorego chcesz sprawdzic reliability: "))
        return reliability, time
    except ValueError:
        return None


def solve():
    """Wylicza reliability po podanej liczbie godzin i okresleniu reliability.\n
    - RETURN zwraca wartosc reliability po podanych godzinach lub None jezeli wystapi blad danych.
    """

    try:
        reliability, time = load_data()
        result = exp(-reliability * time)
        print("Po okreslonym czasie reliability jest rowne: ", result)
        return result
    except TypeError:
        return None
