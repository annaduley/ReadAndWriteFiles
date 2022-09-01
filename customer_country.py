import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')
next(csvfile) #this skips the first line


outfile = open('customer_country.csv','w')

count =0

outfile.write("Full Name, Country\n")
for record in csvfile:
    outfile.write(record[1])
    outfile.write(' ')
    outfile.write(record[2])
    outfile.write(', ')
    outfile.write(record[4])
    outfile.write('\n')
    count+=1

outfile.write('Total Customers: ')
outfile.write(str(count))

outfile.close()
infile.close()