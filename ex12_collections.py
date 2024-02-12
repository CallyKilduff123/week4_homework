# TODO - QUESTION 1a: add Oke to the end of the list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# cheese += 'Oke' --> iterates over each character and passes in individually because it's a string

# adding to LHS
# 1. add to LHS position: use a slice with no start value and end value 0 so list is placed on LHS
cheese[:0] = ['A list of cheese:']

# Adding to RHS /end of the list (or specified position)
# 2. .append method for 1 item added only
cheese.append('Oke1')
# 3. list += [list] overloading +
cheese += ['Oke2']
# 4. Adding a slice to start and end at a specified position
cheese[6:6] = ['Oke3']
# 5. insert at a certain point - insert at position 2, object x
cheese.insert(-1, 'Oke4')
# 6. extending (adding a list to RHS)
# add a list - do not add strings or will pass in O, k, e as above
cheese.extend(['Oke5'])
cheese.extend(['Oke6', "I'm full!"])
# this always puts it second last in the list - as the end position is end +1
cheese.insert(-1, 'Oke7')

print(cheese)

# EXTRA
# indexing L --> R: finding the position of an item
print(f"The position of Oke5 is:", cheese.index('Oke5'))

print('\n', 50 * "*", '\n')

# TODO QUESTION 1b: add 2 items to the end of the list with a single command

name = ['Caroline']
# concatenate name plus list of new names
# does not alter the content of the variable 'name'
print(name + ['Yes I have a boring name', 'Kilduff'])

print('\n', 50 * "*", '\n')

# extend modifies the list but returns 0 - need to print AFTER extending
name.extend(['Yes I have a boring name', 'Kilduff'])
print(name)
# print(name.extend(['Laura Stephanie', 'Kilduff']), name[0:3])

print('\n', 50 * "*", '\n')

# Turn a list into a string:
# Join the list elements into a single string separated by spaces
fullname = ' '.join(name)
print(fullname)

print('\n', 50 * "*", '\n')


# TODO QUESTION 2 - explain the output

tup = 'Hello'
print(type(tup))
print(len(tup))
# tup is a string with the value 'Hello'
# print the length of the string (ie no. characters in Hello = 5)
# python iterates over each character and treats them separately

tup = 'Hello',
print(type(tup))
print(len(tup))
# tup is now a tuple with a single item
# print the length of the tuple (ie 1 item)
# python iterates over each ITEM (as commas separate items in tuple)
# the 5 characters in Hello are treated as 1 item as it is a tuple not a string