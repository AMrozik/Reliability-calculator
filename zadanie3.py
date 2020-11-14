import math


def failure_rate(time, reliability):
    return (math.log(reliability)/time) * -1


def exercise():
    print("Najwiekszy failure rate jest rowny: ", failure_rate(5000, 0.98))
