#!/usr/bin/python3

"""
zadanie3.py: Rozwiązuje zadanie 4 z pliku reliability.pdf.

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


def exercise():
    """"""

    MTBF = 1000
    time_without_failure = 500
    failure_rate = 1/MTBF

    R = exp(-time_without_failure * failure_rate)
    print(f"failure rate: {round(R, 2)}")
