# Formatting strings, yo
sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}

sales_statement = '{} bought {} item(s) at a price of {} each for a total of {}'

print(sales_statement.format(sales_record['person'],
                             sales_record['num_items'],
                             sales_record['price'],
                             sales_record['num_items']*sales_record['price']))

# How to open a CSV
import csv

%precision 2 # sets precision

with open('mpg.csv') as csvfile:
    cars = list(csv.DictReader(csvfile))

cars[:3] # The first three dictionaries in our list.

# Each line looks like this:
# OrderedDict([('', '1'),
#              ('manufacturer', 'audi'),
#              ('model', 'a4'),
#              ('displ', '1.8'),
#              ('year', '1999'),
#              ('cyl', '4'),
#              ('trans', 'auto(l5)'),
#              ('drv', 'f'),
#              ('cty', '18'),
#              ('hwy', '29'),
#              ('fl', 'p'),
#              ('class', 'compact')])

# Exercise: find the average cty fuel economy across all cars. sum(float(d['cty']) for d in mpg) / len(mpg)
# my initial implementation
# number_of_cars = len(mpg)
# total = 0
# for vehicle in mpg:
#     total += float(vehicle['cty'])
# total / number_of_cars
sum(float(v['cty']) for v in cars) / len(cars)

# Exercise: find the average hwy fuel economy across all cars.
sum(float(v['hwy']) for v in cars) / len(cars)

# Exercise: use `set` to return the unique values for the classes of vehicles in the dataset
set(v['class'] for v in cars)

# Exercise: use `set` to return the unique values for the manufacturer of vehicles in the dataset
set(v['manufacturer'] for v in cars)

# Exercise: use `set` to return the unique values for the transmission types for vehicles in the dataset
set(v['trans'] for v in cars)

# Exercise: use `set` to return the unique values for the number of cylinders the cars in our dataset have. # cylinders = set(d['cyl'] for d in mpg)
set(v['cyl'] for v in cars)

# Group the cars by number of cylinder, then find the average cty mpg for each group.
cylinders = set(v['cyl'] for v in cars)

def city_mpg_by_cylinder(cars, cyl):
    total = 0
    count = 0
    for car in cars:
        if(car['cyl']) == cyl:
            total += float(car['cty'])
            count += 1
    return total / count

output = {}
for c in cylinders:
    output[c] = city_mpg_by_cylinder(c)
output

# Find the average hwy mpg for each class of vehicle in our dataset.
vehicle_classes = set(v['class'] for v in cars)

hwyMPGByVehicleClass = []
for c in vehicle_classes:
    summpg = 0
    classcount = 0
    for d in mpg:
        if(d['class']) == c:
            summpg += float(d['hwy'])
            classcount +=1
    hwyMPGByVehicleClass.append((c, summpg / classcount))

hwyMpgByVehicleClass.sort(key=lambda x: x[1])

# Group the cars by manufacturer, then find the average cty mpg for each group.

# Group the cars by class of vehicle, then find the average hwy mpg for each group.

# Group the cars by transmission, then find the average hwy mpg for each group.

#### 
# Exercise 1:
# use list(map(func, collection)) to produce titles and only last names for each professor
# Output = ["Dr. Brooks", "Dr. Collins-Thompson", etc...]
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return # you fill this in 
    # title = person[:3]
    # last_name = person.split()[-1]
    # return title + " " + last_name

list(map(split_title_and_name, people))


# Exercise 2: Take this function and convert it into a list comprehension
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

# times_tables() == [???]
[i * j for j in range(10) for i in range(10)]


# Exercise 3:
# The user ids are each one letter followed by one numbers (e.g. a4). 
# Your task at such an organization might be to hold a record on the billing activity for each possible user.
# Write an initialization line as a single list comprehension which creates a list of all possible user ids. 
# Assume the letters are all lower case.
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [digit + letter for digit in digits for letter in lowercase]


# Exercise 4:
# The user ids are all two letters followed by two numbers (e.g. aa43). 
# Your task at such an organization might be to hold a record on the billing activity for each possible user.
# Write an initialization line as a single list comprehension which creates a list of all possible user ids. 
# Assume the letters are all lower case.
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

