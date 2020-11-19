#!/usr/bin/python3

"""
zadanie3.py: Rozwiązuje zadanie 4 z pliku reliability.pdf.

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


def exercise():
    """"""

    reliability = 0.98
    time = 5000

    print("Najwiekszy failure rate jest rowny: ", (log(reliability)/time) * -1)
