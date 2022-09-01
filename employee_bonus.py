import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile,delimiter=',')
next(csvfile) #this skips the first line

for record in csvfile:
    print('\nEmployee: ', record[1], record[2])
    bonus = record[3] + record[4]
    print('Total Pay: ', bonus,'\n')
    input('Press ENTER to continue')
    


infile.close()
