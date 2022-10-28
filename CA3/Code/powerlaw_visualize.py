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


def vis_pdf_Lin():
    degrees = df["views"]
    data = list(degrees)
    ####
    fit = powerlaw.Fit(data, discrete=True, xmin=1)

    figPDF = powerlaw.plot_pdf([x for x in data if x != 0], color='b')
    # powerlaw.plot_pdf(data, linear_bins=True, color='r', ax=figPDF)
    fit.power_law.plot_pdf(color='r', linestyle='--', ax=figPDF)

    ####
    figPDF.set_ylabel("p(k)")
    figPDF.set_xlabel(r"views")
    plt.title("PDF Linear of views")
    plt.show()


# vis_pdf_Lin()


def vis_pdf_Bin():
    degrees = df["views"]
    data = list(degrees)
    ####
    fit = powerlaw.Fit(data, discrete=True, xmin=1)

    # figPDF = powerlaw.plot_pdf(data, color='b')
    figPDF = powerlaw.plot_pdf([x for x in data if x != 0], linear_bins=True, color='b')
    fit.power_law.plot_pdf(color='r', linestyle='--', ax=figPDF)

    ####
    figPDF.set_ylabel("p(k)")
    figPDF.set_xlabel(r"views")
    plt.title("PDF Linear Binning of views")
    plt.show()


# vis_pdf_Bin()


def vis_cdf():
    degrees = df["views"]
    data = list(degrees)
    ####
    fit = powerlaw.Fit(data, discrete=True, xmin=1)
    # figPDF = powerlaw.plot_pdf(data, color='b')
    figCCDF = powerlaw.plot_ccdf([x for x in data if x != 0], color='g')
    fit.power_law.plot_ccdf(color='r', linestyle='--', ax=figCCDF)
    ####
    figCCDF.set_ylabel("p(k)")
    figCCDF.set_xlabel(r"views")
    plt.title("CCDF of views")
    plt.show()


vis_cdf()
