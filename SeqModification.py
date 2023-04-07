
#def indicates that it is a function definition
def partA(gcCount): 
    #sets teh variable count = to 0 so it can be added to 
    count = 0
    for i in gcCount:
        #looks for all indications of G and C
        if i == "G" or i =="C":
                #adds 1 to the count variable when a G/C is found 
                count = count + 1 
    #returns the number of G/C bases
    return count 

#built-in random variable generator 
import random 

def partB(seq):
    #reads the file 
    seq1 = seq.read()
    #puts it into lowercase
    seq1 = seq1.lower()
    bases = ['A','T','C','G']
    num = input("Please input an integer ")
    num = int(num)
    for i in range(num):
        #determines a random postion in the file of bases and then replaces the base with a random base
        ranPosition = random.randint(0, len(seq1)-1)
        print("The nucleotide at the random postion " + str(ranPosition) + " was replaced")
        baseFin = random.choice(bases)
        seq2 = seq1[:ranPosition] + baseFin + seq1[ranPosition +1:]
    #returns thhe modified file 
    return(seq2) 

def main():
    seqGC = input('Please enter a sequence of bases. The G and C bases will be counted.')
    finCount = partA(seqGC)
    #str() converts the integer from the input to a string 
    print("The GC count is " + str(finCount))
    fileName = input("Please enter a file name ")
    #will try to open the file name thhat was input
    try:
        seq = open(fileName)
    #if the file cannot be opened the the print statement will run
    except:
        print("File cannot be read. Please try again.")
        exit()
    seq2 = partB(seq)
    print(seq2)


if __name__ == "__main__":
	main()
