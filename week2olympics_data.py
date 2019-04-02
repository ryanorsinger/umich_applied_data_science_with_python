import pandas as pd

df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# Question 1 - Which country has won the most gold medals in summer games?
def answer_one():
    return df["Gold"].argmax()

# Question 2 - Which country had the biggest difference between their summer and winter gold medal counts?
def answer_two():
    return  (df["Gold"] - df["Gold.1"]).abs().argmax()

### Question 3
# Which country has the biggest difference between their summer gold medal counts and winter gold medal counts relative to their total gold medal count? 
# (Summer Gold - Winter Gold) / TotalGold
# Only include countries that have won at least 1 gold in both summer and winter.
def answer_three():
    golds = df[(df['Gold.1'] > 0) & (df['Gold'] > 0)] # countries with > 0 in both winter and summer
    diff = (golds["Gold"] - golds["Gold.1"]).abs() # difference between summer and winter
    ratios = diff / golds["Gold.2"]
    return ratios.argmax()


# Write a function that creates a Series called "Points" 
# which is a weighted value where each gold medal (Gold.2) counts for 3 points, 
# silver medals (Silver.2) for 2 points, and bronze medals (Bronze.2) for 1 point. 
# The function should return only the column (a Series object) which you created, 
# with the country names as indices.
# This function should return a Series named `Points` of length 146

# make a series of zeros 

def answer_four():
    points = np.zeros(df.ID.count())
    points += df['Gold.2'] * 3
    points += df['Silver.2'] * 2
    points += df['Bronze.2']     
    return pd.Series(points, index=df.index)
