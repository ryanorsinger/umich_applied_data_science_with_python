
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.5** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# # Assignment 3 - More Pandas
# This assignment requires more individual learning then the last one did - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.

# ### Question 1 (20%)
# Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and renewable electricity production](Energy%20Indicators.xls) from the [United Nations](http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year 2013, and should be put into a DataFrame with the variable name of **energy**.
# 
# Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude the footer and header information from the datafile. The first two columns are unneccessary, so you should get rid of them, and you should change the column labels so that the columns are:
# 
# `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# 
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule). For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# 
# Rename the following list of countries (for use in later questions):
# 
# ```"Republic of Korea": "South Korea",
# "United States of America": "United States",
# "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# "China, Hong Kong Special Administrative Region": "Hong Kong"```
# 
# There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these, 
# 
# e.g. 
# 
# `'Bolivia (Plurinational State of)'` should be `'Bolivia'`, 
# 
# `'Switzerland17'` should be `'Switzerland'`.
# 
# <br>
# 
# Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960 to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**. 
# 
# Make sure to skip the header, and rename the following list of countries:
# 
# ```"Korea, Rep.": "South Korea", 
# "Iran, Islamic Rep.": "Iran",
# "Hong Kong SAR, China": "Hong Kong"```
# 
# <br>
# 
# Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology](http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# 
# Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names). Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15). 
# 
# The index of this DataFrame should be the name of the country, and the columns should be ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
#        'Citations per document', 'H index', 'Energy Supply',
#        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
#        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# 
# *This function should return a DataFrame with 20 columns and 15 entries.*

# In[220]:


import pandas as pd


# In[221]:


def remove_parentheticals(x):
    """
        Removes any parenthetical expression from a string
        Returns "Bolivia" from "Bolivia (Plurinational State of)" 
    """ 
    if "(" in x:
        return (x[:x.index("(")]).strip()
    else:
        return x

def remove_digits(s):
    """
        Returns a string with all digits removed.
    """
    return ''.join(filter(lambda x: not x.isdigit(), s))


def get_energy():
    import pandas as pd
    energy = pd.read_excel("Energy Indicators.xls")
    
    # drops all the header and footer lines
    energy = energy.iloc[17:243]
    # rename columns of interest
    
    energy = energy.rename(columns = {
        "Unnamed: 1": "Country", 
        "Unnamed: 3": 'Energy Supply',
        "Unnamed: 4": "Energy Supply per Capita",
        "Unnamed: 5": "% Renewable"});

    # drop unnecessary columns
    energy = energy.drop('Unnamed: 0', axis=1)
#     energy = energy.drop('Environmental Indicators: Energy')
    energy['Energy Supply'] = energy['Energy Supply'] * 1000000

    # country renames
    country_renames = {
        "Republic of Korea": "South Korea",
        "United States of America": "United States",
        "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
        "China, Hong Kong Special Administrative Region": "Hong Kong"
    }

    energy.Country = energy.Country.replace(country_renames)
    
    # Strip out any parenthetical parts of names and remove any digits
    energy.Country = energy.Country.apply(remove_parentheticals)
    energy.Country = energy.Country.apply(remove_digits)
    energy["Energy Supply"] = pd.to_numeric(energy["Energy Supply"], errors="coerce")
    energy["Energy Supply per Capita"] = pd.to_numeric(energy["Energy Supply per Capita"], errors="coerce")
    energy["% Renewable"] = pd.to_numeric(energy["% Renewable"], errors="coerce")
    return energy


# In[222]:


def get_gdp():
    import pandas as pd
    GDP = pd.read_csv('world_bank.csv')
    
    GDP = GDP.iloc[3:]
    GDP.columns = GDP.iloc[0]
    
    GDP["Country"] = GDP["Country Name"]
    
    columns_to_keep = ["Country", 2006.0, 2007.0, 2008.0, 2009.0, 2010.0, 2011.0, 2012.0, 2013.0, 2014.0, 2015.0]
    GDP = GDP.filter(columns_to_keep)
    
    # rename the floats of years to integers
    renames = { 2006.0: 2006,
                2007.0: 2007,
                2008.0: 2008, 
                2009.0: 2009,
                2010.0: 2010,
                2011.0: 2011,
                2012.0: 2012,
                2013.0: 2013,
                2014.0: 2014,
                2015.0: 2015 }

    GDP = GDP.rename(index=str, columns=renames)

    # rename country names
    country_renames = { "Korea, Rep.": "South Korea", 
                        "Iran, Islamic Rep.": "Iran",
                        "Hong Kong SAR, China": "Hong Kong"}

    GDP["Country"] = GDP["Country"].replace(country_renames)
    return GDP


# In[223]:


# Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology from the file scimagojr-3.xlsx, which ranks countries based on their journal contributions in the aforementioned area. Call this DataFrame ScimEn.
def get_scimen():
    import pandas as pd
    ScimEn = pd.read_excel("scimagojr-3.xlsx")
    return ScimEn


# In[224]:


def answer_one():
    import pandas as pd

    energy, GDP, ScimEn = get_energy(), get_gdp(), get_scimen()
    a = GDP.merge(energy, how="inner", left_on="Country", right_on="Country")
    df = a.merge(ScimEn, how="inner", left_on="Country", right_on="Country")
    
    # Drop unnecessary column
    df = df.drop('Environmental Indicators: Energy', axis=1)

    # Keep only ranks 1-5
    df = df[df.Rank <= 15]
    
    # set the index to be Country
    df = df.set_index("Country")

    return df

df = answer_one()
df


# ### Question 2 (6.6%)
# The previous question joined three datasets then reduced this to just the top 15 entries. When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?
# 
# *This function should return a single number.*

# In[225]:


get_ipython().run_cell_magic('HTML', '', '<svg width="800" height="300">\n  <circle cx="150" cy="180" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="blue" />\n  <circle cx="200" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="red" />\n  <circle cx="100" cy="100" r="80" fill-opacity="0.2" stroke="black" stroke-width="2" fill="green" />\n  <line x1="150" y1="125" x2="300" y2="150" stroke="black" stroke-width="2" fill="black" stroke-dasharray="5,3"/>\n  <text  x="300" y="165" font-family="Verdana" font-size="35">Everything but this!</text>\n</svg>')


# In[226]:


def answer_two():
    energy, GDP, ScimEn = get_energy(), get_gdp(), get_scimen()
    inner_df = GDP.merge(energy, how="inner", left_on="Country", right_on="Country")
    inner_df = inner_df.merge(ScimEn, how="inner", left_on="Country", right_on="Country")
    
    outer_df = GDP.merge(energy, how="outer", left_on="Country", right_on="Country")
    outer_df = outer_df.merge(ScimEn, how="outer", left_on="Country", right_on="Country")
    
    return len(outer_df) - len(inner_df)

answer_two()


# ## Answer the following questions in the context of only the top 15 countries by Scimagojr Rank (aka the DataFrame returned by `answer_one()`)

# ### Question 3 (6.6%)
# What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# 
# *This function should return a Series named `avgGDP` with 15 countries and their average GDP sorted in descending order.*

# In[227]:


def answer_three():
    Top15 = answer_one()
    years = Top15.iloc[:,0:10]
    means = years.mean(axis=1)
    means = means.sort_values(ascending=False)
    return pd.Series(means)

answer_three()


# ### Question 4 (6.6%)
# By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# 
# *This function should return a single number.*

# In[228]:


def answer_four():
    Top15 = answer_one()
    Top15['avg_GDP'] = answer_three()
    
    # sort by avg_GDP
    Top15 = Top15.sort_index(by='avg_GDP', ascending=False)
    
    # get the 6th largest avg_GDP
    sixth = Top15.iloc[5]

    # isolate only the GDP numeric columns
    sixth = sixth.iloc[0:11]

    # return the highest value minus the lowest value
    return sixth.loc[2015] - sixth.loc[2006]

print(answer_four())


# ### Question 5 (6.6%)
# What is the mean `Energy Supply per Capita`?
# 
# *This function should return a single number.*

# In[229]:


def answer_five():
    Top15 = answer_one()
    return Top15["Energy Supply per Capita"].mean()

answer_five()


# ### Question 6 (6.6%)
# What country has the maximum % Renewable and what is the percentage?
# 
# *This function should return a tuple with the name of the country and the percentage.*

# In[230]:


def answer_six():
    Top15 = answer_one()
    
    # index of the country with the highest percentage of renewables    
    country_index = Top15["% Renewable"].argmax()

    return (country_index, Top15.loc[country_index]["% Renewable"])
           

df = answer_six()
print(df)


# ### Question 7 (6.6%)
# Create a new column that is the ratio of Self-Citations to Total Citations. 
# What is the maximum value for this new column, and what country has the highest ratio?
# 
# *This function should return a tuple with the name of the country and the ratio.*

# In[231]:


def answer_seven():
    Top15 = answer_one()
    Top15['citation_ratio'] = Top15["Self-citations"] / Top15["Citations"]

    country = Top15['citation_ratio'].idxmax()
    highest_ratio = Top15['citation_ratio'].max()
    return (country, highest_ratio)

answer_seven()


# ### Question 8 (6.6%)
# 
# Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
# What is the third most populous country according to this estimate?
# 
# *This function should return a single string value.*

# In[232]:


def answer_eight():
    Top15 = answer_one()
    Top15["population_estimate"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    Top15 = Top15.sort_values(by = "population_estimate", ascending=False)
    return Top15.index[2]

answer_eight()


# ### Question 9 (6.6%)
# Create a column that estimates the number of citable documents per person. 
# What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# 
# *This function should return a single number.*
# 
# *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*

# In[233]:


def answer_nine():
    Top15 = answer_one()
    Top15["population_estimate"] = Top15["Energy Supply"] / Top15["Energy Supply per Capita"]
    Top15["citable_documents_per_person"] = Top15["Citations"] / Top15["population_estimate"]
    
    correlation = Top15["citable_documents_per_person"].corr(Top15['Energy Supply per Capita'], method="pearson")
    return correlation

answer_nine()


# In[234]:


# def plot9():
#     import matplotlib as plt
#     %matplotlib inline
    
#     Top15 = answer_one()
#     Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
#     Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
#     Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


# In[235]:


# plot9() # Be sure to comment out plot9() before submitting the assignment!


# ### Question 10 (6.6%)
# Create a new column with a 1 if the country's % Renewable value is at or above the median for all countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# 
# *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*

# In[250]:



def answer_ten():
    import numpy as np
    Top15 = answer_one()
    median_renewable = Top15["% Renewable"].median()
    Top15["renewable_above_median"] = np.where(Top15["% Renewable"] >= median_renewable, 1, 0)
    Top15.sort_index(by="Rank", ascending=True)
    return Top15["renewable_above_median"]
    
answer_ten()


# ### Question 11 (6.6%)
# Use the following dictionary to group the Countries by Continent, then create a dateframe that displays the sample size (the number of countries in each continent bin), and the sum, mean, and std deviation for the estimated population of each country.
# 
# ```python
# ContinentDict  = {'China':'Asia', 
#                   'United States':'North America', 
#                   'Japan':'Asia', 
#                   'United Kingdom':'Europe', 
#                   'Russian Federation':'Europe', 
#                   'Canada':'North America', 
#                   'Germany':'Europe', 
#                   'India':'Asia',
#                   'France':'Europe', 
#                   'South Korea':'Asia', 
#                   'Italy':'Europe', 
#                   'Spain':'Europe', 
#                   'Iran':'Asia',
#                   'Australia':'Australia', 
#                   'Brazil':'South America'}
# ```
# 
# *This function should return a DataFrame with index named Continent `['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*

# In[258]:


def answer_eleven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
    
    Top15["population"] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    
    # rename the dataframe with the provided ContinentDictionary
    Top15 = Top15.rename(index=ContinentDict)
    Top15 = Top15.reset_index()

    # list of aggregate functions
    functions = ['size', 'sum', 'mean', 'std']
    
    # group by 'Country', aggregate using the list of functions
    df = Top15[['Country','population']].groupby('Country').agg(functions)

    return df

answer_eleven()


# ### Question 12 (6.6%)
# Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# 
# *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*

# In[268]:


def answer_twelve():
    import numpy as np
    Top15 = answer_one()
    Top15["bin"] = pd.cut(Top15["% Renewable"], 5)
    ContinentDict  = {'China':'Asia', 
              'United States':'North America', 
              'Japan':'Asia', 
              'United Kingdom':'Europe', 
              'Russian Federation':'Europe', 
              'Canada':'North America', 
              'Germany':'Europe', 
              'India':'Asia',
              'France':'Europe', 
              'South Korea':'Asia', 
              'Italy':'Europe', 
              'Spain':'Europe', 
              'Iran':'Asia',
              'Australia':'Australia', 
              'Brazil':'South America'}
    Top15 = Top15.rename(index=ContinentDict)
    Top15 = Top15.reset_index()
    grouped = Top15.groupby(['Country', 'bin'])
    
    return grouped.size()

answer_twelve()


# ### Question 13 (6.6%)
# Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# 
# e.g. 317615384.61538464 -> 317,615,384.61538464
# 
# *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*

# In[269]:


def answer_thirteen():
    Top15 = answer_one()
    Top15["population"] = Top15['Energy Supply']/Top15['Energy Supply per Capita']
    Top15["population"] = Top15["population"].apply(lambda x:format(x, ","))
    return Top15["population"]
    
answer_thirteen()


# ### Optional
# 
# Use the built in function `plot_optional()` to see an example visualization.

# In[240]:


def plot_optional():
    import matplotlib as plt
    get_ipython().magic('matplotlib inline')
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter', 
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'], 
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")


# In[241]:


#plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!

