from math import exp


def exercise():
    """Suppose that a component we wish to model has a constant failure rate with a mean time
        between failures of 25 hours? Find:-
        (a) The reliability function.
        (b) The reliability of the item at 30 hours."""

    MTBF = 25
    failure_rate = 1/MTBF
    time_without_failure = 30
    R = exp(-time_without_failure * failure_rate)
    print(f"failure rate: {round(R, 4)}")
