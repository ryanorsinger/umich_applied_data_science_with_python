import numpy as np
import pandas as pd

census_df = pd.read_csv('census.csv')


# Exercise 1 - Which state has the most counties in it? 
# (hint: consider the sumlevel key carefully!
# You'll need this for future questions too...)
# More simply, Which column A value has the most column B values associated w/ it?
# strip out rows where COUNTY=0
# this function should return a single string


counties = census_df[census_df.COUNTY > 0] # only counties list

group_by_state = counties.groupby('STNAME').count()
most_counties = group_by_state.COUNTY.argmax()

# Exercise 2 = **Only looking at the three most populous counties for each state**, what are the three most populous states (in order of highest population to lowest population)? Use `CENSUS2010POP`.
#*This function should return a list of string values.*
# answer is: ["California", "Texas", "Illinois"] b/c 37, 22, and 12 million people, in that order

highest_population_counties = counties.sort_values(by="CENSUS2010POP", ascending=False)[0:3]

# these are just the states
df[df.SUMLEV != 50].head()

# sum up all the 