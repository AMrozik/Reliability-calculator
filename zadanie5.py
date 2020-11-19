#!/usr/bin/python3

"""
zadanie3.py: Rozwiązuje zadanie 4 z pliku reliability.pdf.

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


def exercise():
    """"""

    MTBF = 25
    failure_rate = 1/MTBF
    time_without_failure = 30
    R = exp(-time_without_failure * failure_rate)
    print(f"failure rate: {round(R, 4)}")
