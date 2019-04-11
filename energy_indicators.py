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

# energy = energy.set_index("Country")

energy['Energy Supply'] = energy['Energy Supply'] * 1000000


country_renames = {
    "Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"
}

energy.Country = energy.Country.replace(country_renames)


def remove_parentheticals(x):
    """
        Removes any parenthetical expression from a string
        Returns "Bolivia" from "Bolivia (Plurinational State of)" 
    """ 
    if "(" in x:
        return (x[:x.index("(")]).strip()
    else:
        return x

# Strip out any parenthetical parts of a country name.
energy.Country = energy.Country.apply(remove_parentheticals)

def remove_digits(s):
    """
        Returns a string with all digits removed.
    """
    return ''.join(filter(lambda x: not x.isdigit(), s))

energy.Country = energy.Country.apply(remove_digits)

energy["Energy Supply"] = pd.to_numeric(energy["Energy Supply"], errors="coerce")
energy["Energy Supply per Capita"] = pd.to_numeric(energy["Energy Supply per Capita"], errors="coerce")
energy["% Renewable"] = pd.to_numeric(energy["% Renewable"], errors="coerce")

