from math import exp


def exercise():
    """The equipment in a packaging plant has a MTBF of 1000 hours. What is the probability that
        the equipment will operate for a period of 500 hours without failure?"""

    MTBF = 1000
    time_without_failure = 500
    failure_rate = 1/MTBF

    R = exp(-time_without_failure * failure_rate)
    print(f"failure rate: {round(R, 2)}")
