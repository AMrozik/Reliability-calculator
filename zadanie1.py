#!/usr/bin/python3

"""
zadanie1.py: Rozwiązuje zadanie 2 z pliku reliability.pdf.

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


def reliability(number_of_survivors, number_of_items):
    if number_of_items != 0:
        return number_of_survivors/number_of_items


def failure_rate(failures, survivors, time_interval):
    if survivors * time_interval != 0:
        return failures/(survivors * time_interval)


def exercise():
    """"""

    transistors_amount = 1000
    time_failures_tab = [0, 100, 160], [100, 200, 86], [200, 300, 78], [300, 400, 70], [400, 500, 64], [500, 600, 58], [600, 700, 52], [700, 800, 43], [800, 900, 42], [900, 1000, 36]

    # time is overhaul time passing and failures are amount on this time interval
    failed_amount = 0
    failure_rates = []
    failure_rates_time = []
    reliability_time = []
    for previous_time, time, failures in time_failures_tab:
        failed_amount += failures
        failure_rates.append([failure_rate(failures, transistors_amount - failed_amount, time - previous_time)])
        failure_rates_time.append(time)
        reliability_time.append(reliability(transistors_amount - failed_amount, transistors_amount))

    plt.plot(failure_rates_time, failure_rates)
    plt.xlabel("time")
    plt.ylabel("failure rates")
    plt.show()

    plt.plot(failure_rates_time, reliability_time)
    plt.xlabel("time")
    plt.ylabel("reliability")
    plt.show()