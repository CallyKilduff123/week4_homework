# importing module random
import random
# Initial attempt
# creating an empty list that the random numbers can be added to
# lotto_numbers = []
# for index in range(0, 6):
#     lotto_numbers.append(random.randrange(start=0, stop=50, step=1))
#     to remove duplicates turning the list into a set
#     lotto_numbers = list(lotto_numbers)

# Amended code following chat with Cally
# iterating over the numbers in the range from index 0 and finishing at index 6
lotto_numbers = set()
for index in range(0, 6):
    # adding the random numbers generated into the empty list
    # function for integers returning a randomly selected element from
    # specifying the starting number 0 stopping number 50 & moving on 1 number at a time
    lotto_numbers.add(random.randrange(start=0, stop=50, step=1))
# once the number of numbers n the list is equal to 6 - prints out the list of numbers
if len(lotto_numbers) == 6:
    print(f"Here's your lotto numbers: {lotto_numbers} ")
