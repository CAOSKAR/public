#Beispieldatei pandas -datafram.py

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Daten einlesen
data = pd.read_csv('bundeslaender.csv', sep='\t', decimal=',', header= None)
print(data)