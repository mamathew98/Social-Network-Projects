from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import powerlaw
import numpy as np
import pandas as pd
import scipy
import scipy.stats as st
import seaborn as sns
from fitter import Fitter, get_common_distributions, get_distributions

df = pd.read_csv('data_with_hidden.csv')


def get_best_distribution(data):
    dist_names = ["norm", "exponweib", "weibull_max", "weibull_min", "pareto", "genextreme", "powerlaw"]
    dist_results = []
    params = {}
    for dist_name in dist_names:
        dist = getattr(st, dist_name)
        param = dist.fit(data)

        params[dist_name] = param
        # Applying the Kolmogorov-Smirnov test
        D, p = st.kstest(data, dist_name, args=param)
        print("p value for " + dist_name + " = " + str(p))
        dist_results.append((dist_name, p))

    # select the best fitted distribution
    best_dist, best_p = (max(dist_results, key=lambda item: item[1]))
    # store the name of the best fit and its p value

    print("Best fitting distribution: " + str(best_dist))
    print("Best p value: " + str(best_p))
    print("Parameters for the best fit: " + str(params[best_dist]))

    return best_dist, best_p, params[best_dist]


# get_best_distribution(list(df["Degree"]))


def linear_scale():
    # df = pd.read_csv('data.csv')
    degrees = df["count"]
    fit = powerlaw.Fit(list(degrees), discrete=True)
    gama = fit.power_law.alpha
    print(gama)
    degrees_dist = Counter(list(degrees))
    x = []
    y = []
    y_fit = []
    for deg in degrees_dist:
        x.append(deg)
        y.append(degrees_dist[deg] / len(degrees))
        y_fit.append(deg ** (-gama))
    plt.scatter(x, y, label="main", c='b')
    # plt.plot(x, y_fit, label="fit", c="r", linestyle="--")
    plt.title("Linear Scale Distribution plot")
    plt.ylabel("Pk")
    plt.xlabel("Degree")
    # plt.legend()
    plt.show()


# linear_scale()


def linear_binning():
    degrees = df["views"]
    fit = powerlaw.Fit(list(degrees), discrete=True)
    gama = fit.power_law.alpha
    degrees_dist = Counter(list(degrees))
    x = []
    y = []
    y_fit = []

    for deg in degrees_dist:
        x.append(deg)
        y.append(degrees_dist[deg] / len(degrees))
        y_fit.append(deg ** (-gama))

    plt.loglog(x, y, 'bo', label="label")
    plt.loglog(x, y_fit, label="fit", c="r", linestyle="--")
    plt.title("Linear Binning Distribution plot")
    plt.ylabel("Pk")
    plt.xlabel("Degree")
    plt.legend()
    plt.show()


# linear_binning()


def log_binning():
    degrees = df["Degree"]
    fit = powerlaw.Fit(list(degrees), discrete=True)
    gama = fit.power_law.alpha
    degrees_list = list(degrees)
    bins = []
    for n in range(int(np.log2(max(degrees_list)) + 1)):
        b = [i for i in degrees_list if (2 ** n) <= i <= (2 ** (n + 1) - 1)]
        bins.append(b)
    print(bins)
    lists = []
    for i in range(len(bins)):
        if len(bins[i]) == 0:
            continue
        k = sum(bins[i]) / len(bins[i])
        p = len(bins[i]) / (2**i)
        lists.append((k, p))
    print(lists)
    x, y = zip(*lists)
    # y_fit = [(i ** (-gama)) for i in x]
    ax = plt.gca()
    ax.scatter(x, y)
    # ax.plot(x, y_fit, label="test", c='r')
    ax.set_yscale('log')
    ax.set_xscale('log')
    plt.title("Log Binning Distribution plot")
    plt.ylabel("Pk")
    plt.xlabel("Degree")
    # plt.legend()
    plt.show()


# log_binning()


def cumulative():
    degrees = df["count"]
    fit = powerlaw.Fit(list(degrees), discrete=True)
    gama = fit.power_law.alpha
    s = fit.power_law.sigma
    R, p = fit.distribution_compare('power_law', 'exponential', normalized_ratio=True)
    print(R, p)
    print(fit.power_law.alpha)
    print(fit.power_law.xmin)
    print(fit.power_law.xmax)
    print(fit.power_law.sigma)
    print(fit.power_law.D)
    degree_sequence = sorted([d for d in list(degrees)], reverse=True)  # degree sequence
    degreeCount = Counter(degree_sequence)
    deg, cnt = zip(*degreeCount.items())
    cs = np.cumsum(cnt) / len(degrees)
    y_fit = [(x ** (-gama + 1)) for x in deg if x != 0]
    plt.loglog(deg, cs, 'bo', label="main")
    plt.plot([x for x in deg if x != 0], y_fit, label="fit", c="r", linestyle="--")
    plt.title("Cumulative Distribution plot")
    plt.ylabel("Pk")
    plt.xlabel("Degree")
    plt.legend()
    plt.show()


# cumulative()
