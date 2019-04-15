import pandas as pd
import numpy as np

state_names = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


def drop_matching_rows(df, column, values):
    """
        Returns a dataframe excluding rows where a column value exists in the list of provided values
        This is kind of like a reverse .filter method
    """
    return df[df[column].apply(lambda x:x not in values)]

# def get_before_delimeter(s):
def get_string_before_delimiter(string, delimiter):
    """
        Returns contents of a string before a given delimiter
        Example: get_string_before_delimiter("banana-kiwi", "-") returns "banana"
    """
    if delimiter in string:
        return (string[:string.index(delimiter)]).strip()
    else:
        return string
    
def get_before_paren(s):
    return get_string_before_delimiter(s, "(")

def get_before_bracket(s):
    return get_string_before_delimiter(s, "[")

def get_after_delimiter(string, delimiter):
    """ Returns the string contents after the first occurance of the provided delimiter
        Example: get_after_delimiter("This, that, and the other", ",") returns "that, and the other"
    """
    if delimiter in string:
        return string[string.index(delimiter) + 1:].strip()
    else:
        return string


def get_after_comma(s):
    """
        Returns the string contents after the first comma
        Example: get_after_comma('This, that, and the other') returns 'that, and the other'
    """
    return get_after_delimiter(s, ",")

def clean_university_towns(df):
    # Strip out the parens and brackets
    df["towns"] = df["towns"].apply(get_before_paren).apply(get_before_bracket)
    
    # Remove anything up to and including the "," then trim
    df["towns"] = df["towns"].apply(get_after_comma)

    # Remove state names
    # df = df[df["towns"].apply(lambda x:x not in state_names)]
    df = drop_matching_rows(df, "towns", state_names)
    return df   
    
    
def get_university_towns():
    # read raw data and provide table header
    df = pd.read_table('university_towns.txt', names=["towns"])
    df = clean_university_towns(df)
    return df


df = get_university_towns()
print(df)