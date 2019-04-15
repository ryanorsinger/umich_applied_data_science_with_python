import pandas as pd

def get_data():
    df = pd.read_excel("./gdplev.xls")

    df = df[["Unnamed: 4", "Unnamed: 6"]]
    
    column_renames = {
        'Unnamed: 4': "quarters",
        "Unnamed: 6": "gdp"
    }

    df = df.rename(index=int, columns=column_renames)


    # we only care ab  out quarters starting with 2001Q1
    # get the starting index
    start_index = df[df["quarters"] == "2000q1"].index[0]

    # slice out only the data we want
    df = df[start_index:]

    df.reset_index(drop=True, inplace=True)
    return df

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    
    return df

df = get_data()

