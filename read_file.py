# TODO use open and read methods to slurp the entire contents of pelican.txt
# Slurping 1: open song and read entire file in one (down it)
poem = open('pelican.txt', 'r').read()
print(f"Pelican Poem:\n{poem}")
# returns data as a string

# TODO read the file into a list and output the number of items in the list
# counts the number of lines in the poem - each line is a new item
pelican_list = open('pelican.txt', 'r').readlines()
print(f"Pelican poem contains: {len(pelican_list)} lines")
# or:
pelican_as_list = open('pelican.txt', 'r').read().splitlines()
print(f"Pelican poem contains: {len(pelican_as_list)} lines")
# this is counting lines not words!

# counts the number of words in the poem - each word is an item
# use for loop to iterate over poem and use split method to split into words
# use length function to count the number of words
wordcount = 0
for line in pelican_list:
    words = line.split()
    wordcount += len(words)
print("Words:", wordcount)


# TODO use a loop to print the contents of the file, excluding spaces at the end of lines
# Use file object iterator 'for loop' to iterate over rows & hold each line as it is processed
for line in open('pelican.txt', 'r'):
    # get rid of 'new line' in file i.e. last character at the end of the line
    print(line[:-1])



