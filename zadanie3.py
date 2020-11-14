from math import log


def exercise():
    """What is the highest failure rate for a product if it is to have a reliability
    (or probability of survival) of 98 percent at 5000 hours?
    Assume that the time to failure follows an exponential distribution."""

    reliability = 0.98
    time = 5000

    print("Najwiekszy failure rate jest rowny: ", (log(reliability)/time) * -1)
