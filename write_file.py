# TODO Pelican exercise
# open a file to write to - if doesn't exist already - will be created by 'w'
output = open('pelican.txt', 'w')
# write a line - you must include line breaks
chars_written = output.write('A wonderful bird is the pelican\n')
chars_written2 = output.write('His bill holds more than his belican\n')
# create a list of lines - include line breaks
lines = ['He can take in his beak,\n', 'Enough food for a week,\n', "But I'm damned if I see how the helican.\n"]
output.writelines(lines)
output.close()



