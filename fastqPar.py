aa_dict = {'Met':['ATG'], 'Phe':['TTT', 'TTC'], 'Leu':['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'], 'Cys':['TGT', 'TGC'], 'Tyr':['TAC', 'TAT'], 'Trp':['TGG'], 'Pro':['CCT', 'CCC', 'CCA', 'CCG'], 'His':['CAT', 'CAC'], 
'Gln':['CAA', 'CAG'], 'Arg':['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'Ile':['ATT', 'ATC', 'ATA'], 'Thr':['ACT', 'ACC', 'ACA', 'ACG'], 
'Asn':['AAT', 'AAC'], 'Lys':['AAA', 'AAG'], 'Ser':['AGT', 'AGC', 'TCT', 'TCC', 'TCA', 'TCG'], 'Val':['GTT', 'GTC', 'GTA', 'GTG'], 
'Ala':['GCT', 'GCC', 'GCA', 'GCG'], 'Asp':['GAT', 'GAC'], 'Glu':['GAA', 'GAG'], 'Gly':['GGT', 'GGC', 'GGA', 'GGG'], '*':['TAA','TAG','TGA']}

#the header entered by the user is searched for  
def headerChoice(userHeader,header1ANDseq):
    if userHeader in header1ANDseq:
        values = header1ANDseq[userHeader]
        #header and associated sequence is returned to be used in later function 
        return values 

#the reading frame from user input is used to modify the sequence 
def readingFrame(values, userRFrame):
        #if 0 is entered, reading begins at the first character
	if userRFrame == 0:
		values = values
        #if 1 is entered, reading begings at the second character
	elif userRFrame == 1:
		values = values[1:]
        #if 2 is entered, reading begings at the third character
	elif userRFrame == 2:
		values == values[2:]
    #modified sequence is returned 
	return values

#amino acid count function 
def part1(values):
    d = {}
    #the length of the sequence is taken and the range is established 
    for b in range (len(values)):
        #codon is established for every three characters
        codon = values[b:b+3]
        #the amino acid dictionary is searched through to find the codon's corresponding amino acid 
        for aa, codons in aa_dict.items():
            #when the codon is found in the dictionary, it's corresponding amino acid count is added to
            if codon in codons and aa in d.keys(): 
                d[aa] += 1
            elif codon in codons:
                d[aa] = 1
    #returns the final amino acid count 
    return (d)

#function to trim at specific quality score 
def part2(bases,qualScore,cutHere):
    s = []
    d = []
    count = 0

    #calls on the quality score list 
    for i in qualScore:
        #built in fuction for quality scores
        y = ord(i) - 64
        s.append(y)

    for b in range(len(s)):
        count +=1
        #sets up window to be four characters
        windowQual = s[b:b+4]
        #takes the average of the scores in the window
        average = sum(windowQual)/len(windowQual)
        #if the average score is greater than or equal to cutoff value, the window is kept
        if average>= int(cutHere):
            d.append(average)
        else:
            break
    #opens a file
    newFile = open('trimmed.fastq', 'a')

    #the bases are trimmed at the character associated with the final count variable
    result = bases[0:count]
    #the trimmed bases are added to the new file that was opened
    newFile.write(result + ', ')

    #the quality score characters are trimmed at the character associated with the final count variable
    result2 = qualScore[0:count]
    #the trimmed quality scores are added to the new  file 
    newFile.write(result2)

    #both the trimmed sequence and quality scores are returned 
    final = bases[0:count],qualScore[0:count]
    return (final)

def main():
	#opens up the given file
    with open("2v2.fastq", "r")  as file:
        #reads the file 
        lines = file.readlines()
    #sets up empty lists to use
    header1 = []
    seqLst = []
    plusHHeadLst = []
    qualLst = []

    for line in lines:
        line = line.rstrip()
        #if the line starts with an @, it is added to the header list
        if line.startswith("@"):
            header1.append(line)
        #if the line starts with a base, it is added to the sequence list
        if line.startswith("A") or line.startswith("T") or line.startswith("G") or line.startswith("C"):
            seqLst.append(line)
        #if the line starts with a +, it is added to the second header list
        if line.startswith("+"):
            plusHHeadLst.append(line)
        #if the line starts with e g or d, it is added to the quality score list 
        if line.startswith("e") or line.startswith("g") or line.startswith("d"):
            qualLst.append(line)

    #combines the two lists into one dictionary 
    header1ANDseq = dict(zip(header1,seqLst))
    seqANDqualscore = zip(seqLst,qualLst)
    data = dict(zip(header1,seqANDqualscore))

    #the function is put into a loop 
    while 1: 
        try:
            #has user choose what to do 
            print("Would you like to (1) generate an amino acid count from a sequence of your choosing or (2) trim the nucleotide sequence of your choosing based on the quality score?")
            option = int(input("Please enter 1 or 2 \n"))

            #amino acid count for each codon 
            if option == 1: 
                print("Please enter a FASTQ record you would like to work with.")
                userHeader = input("Enter the whole header, beinging with the '@' symbol.\n")
                #calls on the fuciton for header search 
                values = headerChoice(userHeader,header1ANDseq)
                userRFrame = int(input("Please specify the reading frame. Enter 0, 1, or 2. \n"))
                values = readingFrame(values, userRFrame)
                codonD = part1(values)
                #prints out final codon count 
                print(codonD)

            #quality score trimming 
            if option == 2: 
                print("Please enter a FASTQ record you would like to work with.")
                headerUser = input("Enter the whole header, beinging with the '@' symbol.\n")
                #associates user header with the header, quality score, and sequence from the dictionary
                seqScore = data[headerUser]
                #the bases are established to be in the first position
                bases = str(seqScore[0])
                #quality scores are establised to be in the second position 
                qualScore = str(seqScore[1])
                cutHere = int(input("Please input a score cutoff. Make sure the value is between 0 and 42.\n"))
                qual = part2(bases,qualScore,cutHere)
                #prints the trimmed sequence from the function 
                print(qual)
                #runs if the user doesn't input thhe correct value 
                print("Sorry, your input could not be read. Please follow the prompt and try again. ")
            
            else: 
                raise ValueError 
        #if an error is found in the try block, the except block is ran
        except ValueError:
            print("Please only enter '1' or '2' when asked.")


if __name__ == "__main__":
	main()
