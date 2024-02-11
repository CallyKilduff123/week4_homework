# getting the contents of the whole file
lym = open('pelican_katy.txt', 'r').read()
# printing the whole file
print(f"Birds birds birds:\n{lym}")
# confirming the type is a string
print(type(lym))
# putting the string from the file into a list
lym_as_list = open('pelican_katy.txt', 'r').read().splitlines()
# printing the list and the length of the list
print(f"A list of birds:\n{lym_as_list}, \n {len(lym_as_list)}")
# printing the contents of the file removing blank lines
for line in open('pelican_katy.txt', 'r'):
    # removing new line in a file
    print(line[:-1])