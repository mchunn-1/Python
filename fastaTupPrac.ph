
def fastaParser():
    #sets up dictionary 
    d = {}

    #will open teh file 
    with open("tuples.fa") as fh:

        key = ""
        for line in fh:
            line = line.strip()
            #if the like starts with > then it will be striped off 
            if line.startswith(">"):
                key = line.lstrip(">")
                if key in d.keys():
                    key = key + "-1"
                d[key] = ""
            else: 
                d[key] = d[key] + line

    return (d)

def baseA(d): 

    for x in d.values():
        lstS = list(x)
        #sets the variable count = to 0 so it can be added to
        aCount=0
        bCount=0
        for i in lstS:
            #looks for all indications of A
            if i == "A":
                aCount = aCount + 1
            #anything other than an A is counted to the other variable 
            else:
                bCount = bCount + 1
            #both of the variables are added
            total = float(aCount) + float(bCount)
            #finds the percent of A
            num = (aCount / total) 
            per = num * 100
        
        seqPer = [x, per]
        #seqPer.sort(key=lambda percent:percent[0])     
        print(seqPer)

def baseT(d): 

    for x in d.values():
        lstS = list(x)
        aCount=0
        bCount=0
        for i in lstS:
            if i == "T":
                aCount = aCount + 1
            else:
                bCount = bCount + 1
            total = float(aCount) + float(bCount)
            num = (aCount / total) 
            per = num * 100
        
        seqPer = [x, per]
        #seqPer.sort(key=lambda percent:percent[0])     
        print(seqPer)

def baseG(d): 

    for x in d.values():
        lstS = list(x)
        aCount=0
        bCount=0
        for i in lstS:
            if i == "G":
                aCount = aCount + 1
            else:
                bCount = bCount + 1
            total = float(aCount) + float(bCount)
            num = (aCount / total) 
            per = num * 100
        
        seqPer = [x, per]
        #seqPer.sort(key=lambda percent:percent[0])     
        print(seqPer)

def baseC(d): 

    for x in d.values():
        lstS = list(x)
        aCount=0
        bCount=0
        for i in lstS:
            if i == "C":
                aCount = aCount + 1
            else:
                bCount = bCount + 1
            total = float(aCount) + float(bCount)
            num = (aCount / total) 
            per = num * 100
        
        seqPer = [x, per]
        #seqPer.sort(key=lambda percent:percent[0])     
        print(seqPer)
		

def main():
    d = fastaParser() 
    #sets up a list
    lst = []

    for key,val in d.items():
        #appends the key and value to the list
        lst.append((key,val,))
    
    #sorts the sequences by length
    seqLen = sorted(lst,key = lambda tup: tup[1])
    print ("seq in order by length\n" + str(seqLen))
   
    print("original seq\n" + str(lst))
    
    #has the user choose a base and takes the input 
    userChoice = input("Please chose a base you would like to sort the sequnece by. Enter A, G, T or G " )
    if userChoice == "A":
        #calls the function 
        acount = (baseA(d))
        print(acount)
    
    elif userChoice =="T":
        tcount = (baseG(d))
        print(tcount)

    elif userChoice =="G":
        gcount = (baseG(d))
        print(gcount)

    elif userChoice =="C":
        ccount = (baseG(d))
        print(ccount)

    #if something besides the 4 bases is enter
    else: 
        print("please try again")

if __name__ == '__main__':
    main() 
