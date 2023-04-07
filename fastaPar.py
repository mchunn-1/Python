def fastaParser():

    with open("seqs.fa") as fh:

        header = ""
        #header = None
        sequence = ""
        for line in fh:

            line = line.strip()
            
            if line.startswith(">"):
                #if header: 
                if len(header) > 0:
                    #only greater than 0 if youve already read a header line in... 
                    yield (header,sequence)
                    sequence = ""
            
                header = line.lstrip('>')

                #line is a header
                header = line.lstrip(">")
            
            else:
                #line is a sequence line
                sequence += line.strip()
        #need this bc if not the last seq wont be printed bc the trigger for yield above is theh next >... there is not next for the last seq
        yield(header,sequence)
               

def main():

    for seqName,seq in fastaParser():
        print(seqName)
        print(seq)

if __name__ == '__main__':
    main() 
