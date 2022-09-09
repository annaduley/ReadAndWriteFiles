import csv


#open files
infile = open('steps.csv','r')
outfile = open('avg_steps.csv','w')


#set up files
csvfile = csv.reader(infile,delimiter=',')
next(csvfile) #this skips the first line


#create variables
months = ['Month, Average Steps','January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
count = 0
total = 0
prev = 0
month = 0 
average =0 


#loop through one month at a time
for line in csvfile:

    if int(line[0]) == prev: #change to while when it works
        count += 1 
        total += int(line[1])
    else:
        if month<13:
            count+=1
            average = total/count
            outfile.write(months[month])
            outfile.write(': ')
            outfile.write(str(average))
            outfile.write('\n')
            count=0
            total = int(line[1])
            average = 0
            month+=1
            prev += 1



count+=1
average = total/count
outfile.write(months[month])
outfile.write(': ')
outfile.write(str(average))
outfile.write('\n')


outfile.close()
infile.close()