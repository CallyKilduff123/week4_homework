# TODO - win the lotto

import random

# collection = set to ensure unique numbers
# create an empty set called lotto
# while loop - iterating over the set,
# whilst the set contains < 6 integers -->
# generate a random integer between 1 and 50 and add it to the set
# until it contains 6 unique integers
# random.randit = function from 'random' module that generates a random integer
lotto = set()
while len(lotto) < 6:
    lotto.add(random.randint(1, 50))
print(f"Winning numbers: {lotto}")


# Other options using lists and tuples:

# tuple
# random.sample selects unique elements from a sequence or set
# range defines the sequence between 1 and 51 (end+1)
# it samples 6 random items in that range
lotto_1 = random.sample(range(1, 51), 6)
print(f"Winning numbers: {lotto_1}")

# list - mutable - not unique numbers
# for _ in range(6): List Comprehension is a concise way to create lists in Python.
# It can be used to apply an expression to each item in an iterable (e.g. list or range)
# construct a new list based on the results. The basic syntax is [expression for item in iterable].
# This iterates 6 times because range(6) = 0 to 5.
# '_' = variable name when actual value is not needed.
lotto_2 = [random.randint(1, 50) for _ in range(6)]
print(f"Winning numbers: {lotto_2}")

