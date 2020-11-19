#!/usr/bin/python3

"""
zadanie2.py: Rozwiązuje zadanie 3 z pliku reliability.pdf.

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


def exercise():
    """"""

    reliability = 0.000001
    time = 2500

    print("Po 2500 godzinach reliability jest rowne: ", exp(-reliability * time))
