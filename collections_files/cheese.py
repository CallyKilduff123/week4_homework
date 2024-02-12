# list of three items in the list
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# adding to the right side as default
# character added individually
cheese += 'Oke'
print(cheese)
# adding multiple items to the right hand side
# print(cheese.extend(['Babybel', 'Baron Bigod', 'Jarlsberg', 'Gorgonzola']))
print(cheese)
# inserting item at the 5th index
cheese.insert(5,'Wild Garlic Cornish Yarg')
print(cheese)
print(len(cheese))
# sorting by the strings
cheese.sort()
print(cheese[0:5])
# including the cheese at index 3
print(f"I love {cheese[3]}.")
# including the cheese at index 4
print(f"Oh i do like a bit of {cheese[4]}")
