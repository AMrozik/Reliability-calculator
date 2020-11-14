import math


def reliability_after_hours(hours, reliability):
    return math.exp(-reliability * hours)


def exercise():
    print("Po 2500 godzinach reliability jest rowne: ", reliability_after_hours(2500, 0.000001))
