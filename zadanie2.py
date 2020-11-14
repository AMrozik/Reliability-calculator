import math


def reliability_after_hours(hours, reliability):
    return math.exp(-reliability * hours)


def exercise():
    '''An industrial machine compresses natural gas into an interstate gas pipeline.
    The compressor is on line 24 hours a day. (If the machine is down, a gas field has to be shut
    down until the natural gas can be compressed, so down time is very expensive.)
    The vendor knows that the compressor has a constant failure rate of 0.000001 failures/hr.
    What is the operational reliability after 2500 hours of continuous service?'''
    print("Po 2500 godzinach reliability jest rowne: ", reliability_after_hours(2500, 0.000001))
