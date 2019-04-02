import pandas as pd

# For the purchase records from the pet store, how would you get a list of all items which had been purchased (regardless of where they might have been purchased, or by whom)?

purchase_1 = pd.Series({'Name': 'Jane',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
purchase_4 = pd.Series({'Name': 'Quincy',
                        'Item Purchased': 'Lizard Bath Wash',
                        'Cost': 15.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3, purchase_4], index=['Store 1', 'Store 1', 'Store 2', 'Store 2'])


# Exercise 1 - Write the code necessary to get a list of all items which had been purchased (regardless of where they might have been purchased, or by whom)?

df['Item Purchased']

# Exercise 2 - Write the code necessary to get a list of the names for every purchaser

df['Name']

# Exercise 3 - Write the code to obtain all data for purchases from Store 1
df.loc['Store 1']


# Exercise 4 - Write the code to get the only the cost from Store 1 purchases
df.loc['Store 1', 'Cost']

# Exercise 5 - Write the code to get the items purchased at Store 2
df.loc['Store 2', 'Item Purchased']


##  BE CAREFUL about references
costs = df['Cost']
costs *= 2 
print(df['Cost']) # the reference created in line 41 and the operation on line 42 altered the original data in the DataFrame


#### given the following data,
# Write a query to return all of the names of people who bought products worth more than $3.00.

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df['Name'][df['Cost'] > 3] # returns the names of all people who bought products costing more than 3 dollars.




