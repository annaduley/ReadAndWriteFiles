def main():
    infile = open('philosophers.txt','r')

    print(infile.readline().rstrip('\n'))
    print(infile.readline().rstrip('\n'))
    print(infile.readline().rstrip('\n'))


    infile.close()

main()

