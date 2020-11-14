import math


def failure_rate(time, reliability):
    return (math.log(reliability)/time) * -1


def exercise():
    '''What is the highest failure rate for a product if it is to have a reliability
    (or probability of survival) of 98 percent at 5000 hours?
    Assume that the time to failure follows an exponential distribution.'''
    print("Najwiekszy failure rate jest rowny: ", failure_rate(5000, 0.98))
