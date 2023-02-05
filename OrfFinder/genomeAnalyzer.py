#!/usr/bin/env python3
# Name: Dami Ibrahim(oaibrahi)
# Group Members: Savi Dhoat
'''Program docstring: This program will prepare the summaries and present the final data'''
import sequenceAnalysis #Allows me to call all the classes and methods from this program

def main() :
    '''
    This main method will calculate the sequence length, gc content and codon frequency and print out all the final information
    '''
    myReader = sequenceAnalysis.FastAreader()
    npo = sequenceAnalysis.NucParams() #assigning npo to the NucParams class so I can use it later to call in different methods
    allSeqs = ''
    for head, seq in myReader.readFasta() :
        npo.addSequence(seq)
        allSeqs += seq
    nucCount = npo.nucCount()
    seqLen = nucCount / 1000000 #Calculate Sequence length
    print('sequence length = ', '%2.2f' % seqLen, 'Mb\n')
    #Calculating GC content
    gContent = npo.nucComposition()['G']
    cContent = npo.nucComposition()['C']
    if nucCount == 0 :
        print("GC content = 0")
    else :
        GCcontent = ((gContent + cContent) / nucCount) * 100 #Calculates GC percentage
        print("GC content = ", "%2.1f" % GCcontent, "%\n")
    AAs = list(npo.aaComposition().keys())
    AAs.sort() #Makes a list of all the codons in the rnaCodonTable and sorts them by alphabetical order
    # print(AAs)
    codonComp = npo.codonComposition()
    # print(codonComp)
    aaComp = npo.aaComposition()
    # print(aaComp)
    for aa in AAs :#find all codons with that amino acid
        codons = [i for i, j in npo.rnaCodonTable.items() if j == aa]
        codons.sort()
        # print(codons)
        for n in codons :#for loop to print codons in a dictionary
            numCodon = codonComp[n]
            totalAA = aaComp[aa]
            # print(totalAA)
            if totalAA == 0 :
                freq = 0
            else :
                freq = (numCodon / totalAA) * 100 #Calculates codon frequency

            print('{:s} : {:s}' '{:5.1f} ({:6d})'.format(n, aa, freq, numCodon))


if __name__ == '__main__' :
    main()











