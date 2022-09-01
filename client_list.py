def main():
    infile = open('clients.txt','r')
    num = 1
    for list in infile:
        print(num, ". ", list.rstrip('\n'),sep='')
        num+=1
    infile.close()

main()