import matplotlib.pyplot as plt


def reliability(number_of_survivors, number_of_items):
    return number_of_survivors/number_of_items


def failure_rate(failures, survivors, time_interval):
    return failures/(survivors * time_interval)


def exercise():
    '''One thousand transistors are placed on life test, and the number of failures in each time interval are recorded.
    Find the reliability and the failure rate at 0, 100, 200, etc hours.
    (You may find it helpful to set this up on a spreadsheet.)
    Time interval   Number of failures
    0-100           160
    100-200         86
    200-300         78
    300-400         70
    400-500         64
    500-600         58
    600-700         52
    700-800         43
    800-900         42
    900-1000        36
    Draw a graph to show the change in the failure rate as the transistors get older.
    Do you think this component shows the bath tub pattern of failure?
    Draw a graph to show how the reliability changes over time.'''
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