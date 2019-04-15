import pandas as pd
import numpy as np
# iterate through list
# identify state names
# clean state name and add to list
# clean each town row and .append(state, town)
# go until next state name

# read raw data and provide table header
def get_raw():
    return pd.read_table('university_towns.txt', names=["towns"])

def get_after_comma(string):
    if "," in string:
        return string[string.index(",") + 1:].strip()
    else:
        return string

def get_before_paren(string):
    if "(" in string:
        return string[:string.index("(")].strip()
    else:
        return string

def clean_town(string):
    return get_after_comma(get_before_paren(string))


def is_state(input):
    return '[edit]' in input

def clean_state(string):
    if is_state(string):
        return string[:string.index("[")].strip()
    else:
        return string


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )'''

    data = []
    state = None
    town = None
    df = get_raw()
    for row in df["towns"]:
        if(is_state(row)):
            state = clean_state(row)
        else:
            town = clean_town(row)
            data.append([state, town])    

    return pd.DataFrame(data, columns=["State", "RegionName"])


x = get_list_of_university_towns()
print(x)