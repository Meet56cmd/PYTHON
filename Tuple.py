# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of sisters and brothers
sisters = ('Maggie', 'Mini')
brothers = ('Rishab', 'Sundar')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
num_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother
family_members = ('Father', 'Mother') + siblings

# Print the results
print("Empty Tuple:", empty_tuple)
print("Sisters Tuple:", sisters)
print("Brothers Tuple:", brothers)
print("Siblings Tuple:", siblings)
print("Number of Siblings:", num_siblings)
print("Family Members Tuple:", family_members)

# Unpack siblings and parents from family_members
siblings_unpack, *parents_unpack = family_members

# Create fruits, vegetables, and animal products tuples
fruits = ('Apple', 'Banana', 'Orange')
vegetables = ('Carrot', 'Broccoli', 'Spinach')
animal_products = ('Chicken', 'Beef', 'Eggs')

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_tp) // 2
sliced_middle_tp = food_stuff_tp[middle_index - 1 : middle_index + 1]
sliced_middle_lt = food_stuff_lt[middle_index - 1 : middle_index + 1]

# Slice out the first three items and the last three items from food_staff_lt list
sliced_first_last_lt = food_stuff_lt[:3] + food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in the tuple
# Check if 'Estonia' is a nordic country
nordic_countries = ('France', 'Switzerland', 'Finand', 'Norway', 'Denmark')

estonia_check = 'Estonia' in nordic_countries

# Check if 'Iceland' is a nordic country
iceland_check = 'Iceland' in nordic_countries

# Print the results
print("Unpacked Siblings:", siblings_unpack)
print("Unpacked Parents:", parents_unpack)
print("Fruits Tuple:", fruits)
print("Vegetables Tuple:", vegetables)
print("Animal Products Tuple:", animal_products)
print("Food Stuff Tuple:", food_stuff_tp)  # This line will raise an error since food_stuff_tp was deleted
print("Food Stuff List:", food_stuff_lt)
print("Sliced Middle from Tuple:", sliced_middle_tp)
print("Sliced Middle from List:", sliced_middle_lt)
print("Sliced First and Last from List:", sliced_first_last_lt)
print("'Estonia' in Nordic Countries:", estonia_check)
print("'Iceland' in Nordic Countries:", iceland_check)