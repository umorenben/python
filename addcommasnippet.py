#PROGRAM TO ONLY ADD COMMA TO END OF LINES IN A TEXT FILE
#STEPS TO RUN SUCCESSFULLY
#1. Ensure the file and this code file are in the same directory or folder
#2. Change 'cdla.csv' file name to your own file name
#3. Change 'cdlaNew.csv' file name to your desire new file name
#4. Run the program


mycommalist = list() #New list to add sorted list from file
###read in myfile from file
filename = 'cdla.csv'
with open (filename) as fin:
    for line in fin:
        if ',' in line:
            mycommalist.append(line.strip()) #Add to mycommalist without comma
        else:
            mycommalist.append(line.strip() + ',')#Add to mycommalist with comma

###write sorted myfile to file
filename = 'cdlaNew.csv'
with open (filename, 'w') as fout:
    for commalist in mycommalist:
        fout.write (commalist + '\n')


#PRINT OUT FOR COMPLETE RUNNING OF PROGRAM
print ("The Program was completeed successfully.\n\nPlease check your file")
