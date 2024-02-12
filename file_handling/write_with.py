# with is the safest way to open files as closes files on error
# creating the file in write mode
# with is a statement
with open('pelican.txt','w') as output:
    output.write('A wonderful bird is the pelican.\n')
    output.write('His bill holds more than his belican.\n')
    output.writelines(["He can take in his beak,\n", "Enough food for a week, \n", "But I'm damned if i see how the helican.\n"])
# as file is closed, we reopen in read mode to read the file and print the lines from the file
with open('pelican.txt', 'r') as file:
    for line in file:
        print(line[:-1])