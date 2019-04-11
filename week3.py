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


## Acquire GDP Data
GDP = pd.read_csv("./world_bank.csv")

country_renames = { "Korea, Rep.": "South Korea", 
                    "Iran, Islamic Rep.": "Iran",
                    "Hong Kong SAR, China": "Hong Kong"}

GDP["Country Name"] = GDP["Country Name"].replace(country_renames)
GDP["Country"] = GDP["Country Name"]

# Acquire Sciamgo Journal and Country Rank data for energy engineering and power technology
ScimEn = pd.read_excel("./scimagojr-3.xlsx")

# Join the three datasets: GDP, Energy, and ScimEn using the intersection of country names.
a = GDP.merge(energy, how="inner", left_on="Country", right_on="Country")
df = a.merge(ScimEn, how="inner", left_on="Country", right_on="Country")

# Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).

dates_to_drop = ['1960',
 '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970',
 '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980',
 '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990',
 '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000',
 '2001', '2002', '2003', '2004', '2005', '2016', '2017', '2018']

# TODO drop any date column not 2006-2015
df = df.drop(dates_to_drop, axis=1)

# TODO keep only the rows where RANK is 15 or less

# df = df[df.Rank <= 15]


# The index of this DataFrame should be the name of the country
# columns should be:
#  ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015'].

    