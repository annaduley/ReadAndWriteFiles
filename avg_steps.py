import csv


#open files
infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')


#set up files
csvfile = csv.reader(infile,delimiter=',')
next(csvfile) #this skips the first line

outfile.write("Month, Average Steps\n")


#create variables
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
count = 0
total = 0
prev = 1
month = 0 
average =0 


#loop through one month at a time
while month < 12:
    for line in csvfile:
        if int(line[0]) == prev: #change to while when it works
            count += 1
            total += int(line[1])

        else:
            average = total/count
            outfile.write(months[month])
            outfile.write(': ')
            outfile.write(str(average))
            outfile.write('\n')
            total = 0
            average = 0
            month+=1
            prev = line[0]



        # prev = line[0]




outfile.close()
infile.close()