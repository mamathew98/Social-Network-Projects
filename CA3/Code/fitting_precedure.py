import numpy as np
import pandas as pd
import seaborn as sns
from fitter import Fitter, get_common_distributions, get_distributions

df = pd.read_csv('data_with_hidden.csv')

f = Fitter(list(df["count"]),
           distributions=get_common_distributions())
f.fit()
print(f.get_best())
print(f.summary()
)