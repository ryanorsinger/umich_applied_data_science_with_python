import numpy as np
import pandas as pd

energy_url = "http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls"

raw_energy = pd.read_excel(energy_url)

# drop the headers
print(raw_energy[14:22])

