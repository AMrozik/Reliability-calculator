import matplotlib.pyplot as plt


def reliability(number_of_survivors, number_of_items):
    return number_of_survivors/number_of_items


def failure_rate(failures, survivors, time_interval):
    return failures/(survivors * time_interval)


def exercise():
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