
# TODO - write code to copy text from the GP letter to the patient letter

# create patient letter to write to (originally used 'w' but didn't pull through grammar changes from GP letter)
output = open('cataract_surgery_patient.txt', 'a')

# copy the GP letter content to the patient letter
# The with statement is used to wrap the execution of a block of code.
# It ensures that these setup and cleanup tasks are done automatically.
# open GP letter to read as source, and newly created patient letter as destination to write to
# use for loop to read each line in the GP letter and write into patient letter
with open('cataract_surgery_GP.txt', 'r') as source_file, open('cataract_surgery_patient.txt', 'w') as destination_file:
    for line in source_file:
        destination_file.write(line)

# source_file = open('cataract_surgery_GP.txt', 'r')
# destination_file = open('cataract_surgery_patient.txt', 'a')
# for line in source_file:
#     destination_file.write(line)
# when I run this code instead with dest file as 'w' - the changes below don't pull through
# if I just open the destination file as 'a' here - it repeats letters at the end every time it runs


# TODO - write code to swap 'Phacoemulsification + IOL' to 'Cataract Surgery' in the patient letter

# Define the original and switched terms
# medical term = phaco, patient term = cataract surgery
medical_term = 'Phacoemulsification + IOL'
patient_term = 'Cataract Surgery'
# # Open the patient letter for reading and slurp the content
content = open('cataract_surgery_patient.txt', 'r').read()
# # Replace the medical term with the patient term
modified_content = content.replace(medical_term, patient_term)
# Open the file for writing and write the modified content
new_content = open('cataract_surgery_patient.txt', 'w')
new_content.write(modified_content)

output.close()

