# TODO - create a letter to a GP in a txt file

# create a new file to write to = 'w'
# if open as 'a' - it will repeat the lines every time you run the code
# insert text using the output.write method and the list method (as with pelican)
# use writelines method to write the list beneath the previous outputs
# DONT FORGET TO CLOSE THE FILE

output = open('cataract_surgery_GP.txt', 'w')

dear_dr = output.write('Dear Dr GP\n\n')
re_patient = output.write('Re: Raffy Dog. DOB 10/06/2010. MRN 123234435\n\n')
procedure_type = output.write('Planned Procedure: Phacoemulsification + IOL\n\n')
lines = ["""Raffy Dog attended clinic today. He has been experiencing glare at night and difficulty reading.
Having been counselled on the risks and benefits of the procedure, and offered all options, including doing nothing,
Raffy Dog has decided to proceed with surgery.\n\nKind regards,\n\nDr Ophthalmology"""]

output.writelines(lines)
output.close()


