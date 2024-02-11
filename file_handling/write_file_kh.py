# used python to create my file but commented out as once created it then errored after
# create = open('pelican_katy.txt', 'x')
# used w - creates and allows write of file but will get overwritten each time file created
output = open('pelican_katy.txt', 'w')

new_bird = output.write('A wonderful bird is the pelican.\n')
print(new_bird)

bill = output.write('His bill holds more than his belican.\n')
print(bill)

lines = ["He can take in his beak,\n", "Enough food for a week, \n", "But I'm damned if i see how the helican.\n"]
output.writelines(lines)
# closed the file to stop it continuing to run
output.close()
# for line in open('pelican_katy.txt', 'r'):
#     print(line, end="")
# opened the file in read to be able to then write the contents of the file to the output
pelican = open('pelican_katy.txt', 'r')
print(pelican.read())
output.close()