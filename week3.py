import numpy as np
import pandas as pd

energy_url = "EnergyIndicators.xls"

energy = pd.read_excel(energy_url)

# drops all the header and footer lines
energy = energy.iloc[17:243]

# drop unnecessary columns
energy = energy.drop(columns=['Unnamed: 0', 'Unnamed: 2'])

# rename columns of interest
energy = energy.rename(columns = {
    "Unnamed: 1": "Country", 
    "Unnamed: 3": 'Energy Supply',
    "Unnamed: 4": "Energy Supply per Capita",
    "Unnamed: 5": "% Renewable"});

energy = energy.set_index("Country")

energy['Energy Supply'] = energy['Energy Supply'] * 1000000

print(energy.head())

