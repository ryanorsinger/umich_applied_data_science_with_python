import numpy as np
import pandas as pd

energy_url = "EnergyIndicators.xls"

energy = pd.read_excel(energy_url)

# drops all the header and footer lines
energy = energy.iloc[15:243]

print(energy)

# assign columns "Country", "Energy Supply", "Energy Supply per Capita", "% Renewable"
