#!/usr/bin/env python3
# Name: Dami Ibrahim(oaibrahi)
# Group Members: Savi Dhoat
'''Program docstring: Calculates composition statistics, relative codon usage, and amino acid composition. '''
class OrfFinder:
    '''
    Defines the init, findOrfs, and reverse compliment methods and their attributes.
    '''
    def __init__(self, seq, start, stop, minOrf, longestGene=True):
        '''
        Captures and defines self.seq, self.stop, self.start, self.minOrf, self.longestGene that will be used in the findOrfs and main methods.
        '''
        self.seq = seq
        self.stop = set(stop); self.start = set(start)
        self.minOrf = minOrf
        self.longestGene = longestGene

    def findOrfs(self, gene):
        '''
        Find genes in all three frames.
        '''
        finalList = []
        startPos = [0]
        for seqFrame in range(3): #iterates through the 3 frames
            for i in range(seqFrame, len(self.seq),3):
                codon = self.seq[i:i+3]
                if codon in self.start:
                    startPos.append(i)

                elif codon in self.stop: #iterates through the index of start codons and creates genes
                    for start in startPos:
                        orfLen = (i + 3) - start
                        if orfLen>= self.minOrf:
                            if gene == True:
                                gene = [seqFrame+1, start+1, i+3, orfLen] #Calculation for codon list
                                finalList.append(gene)
                            else:
                                gene = [(seqFrame*-1) -1, len(self.seq)-i+4, len(self.seq)-start, orfLen]
                                finalList.append(gene)

                    startPos = [] #clear start codon list

            for start in startPos: #accounts for dangling starts and stops
                orfLen = len(self.seq) - start
                lag = self.seq[start:len(self.seq)]
                if orfLen >= self.minOrf:
                    gene = [seqFrame + 1, start + 1, len(self.seq), orfLen, lag]
                    finalList.append(gene)
                else:
                    gene = [((-seqFrame + 1 )* -1), 1, len(self.seq)-start, orfLen, lag]
                    finalList.append(gene)
            startPos = [0]
        return finalList
    def rc(self, seq):
        ''' Takes the reverse and compliment of the DNA sequence'''
        seq = seq.replace('A', 'T').replace('T','A').replace('C','G').replace('G','C')[::-1]
        return seq
class NucParams :
    '''
    Contains the rna codon table and dna codon table. Defines init, addSequence, aaComposition, nucComposition,
    codonCompisition, and nucCount
    methods and its attributes.
    '''
    rnaCodonTable = {

        # RNA codon table

        # U

        'UUU' : 'F', 'UCU' : 'S', 'UAU' : 'Y', 'UGU' : 'C',  # UxU

        'UUC' : 'F', 'UCC' : 'S', 'UAC' : 'Y', 'UGC' : 'C',  # UxC

        'UUA' : 'L', 'UCA' : 'S', 'UAA' : '-', 'UGA' : '-',  # UxA

        'UUG' : 'L', 'UCG' : 'S', 'UAG' : '-', 'UGG' : 'W',  # UxG

        # C

        'CUU' : 'L', 'CCU' : 'P', 'CAU' : 'H', 'CGU' : 'R',  # CxU

        'CUC' : 'L', 'CCC' : 'P', 'CAC' : 'H', 'CGC' : 'R',  # CxC

        'CUA' : 'L', 'CCA' : 'P', 'CAA' : 'Q', 'CGA' : 'R',  # CxA

        'CUG' : 'L', 'CCG' : 'P', 'CAG' : 'Q', 'CGG' : 'R',  # CxG

        # A

        'AUU' : 'I', 'ACU' : 'T', 'AAU' : 'N', 'AGU' : 'S',  # AxU

        'AUC' : 'I', 'ACC' : 'T', 'AAC' : 'N', 'AGC' : 'S',  # AxC

        'AUA' : 'I', 'ACA' : 'T', 'AAA' : 'K', 'AGA' : 'R',  # AxA

        'AUG' : 'M', 'ACG' : 'T', 'AAG' : 'K', 'AGG' : 'R',  # AxG

        # G

        'GUU' : 'V', 'GCU' : 'A', 'GAU' : 'D', 'GGU' : 'G',  # GxU

        'GUC' : 'V', 'GCC' : 'A', 'GAC' : 'D', 'GGC' : 'G',  # GxC

        'GUA' : 'V', 'GCA' : 'A', 'GAA' : 'E', 'GGA' : 'G',  # GxA

        'GUG' : 'V', 'GCG' : 'A', 'GAG' : 'E', 'GGG' : 'G'  # GxG

    }

    dnaCodonTable = {key.replace('U', 'T') : value for key, value in rnaCodonTable.items()}

    def __init__(self) :
        '''
        Captures and defines the self.nuc, self.aaComp, self.nucComp, and self.codonComp dictionaries that can be used
        later in the other methods.
        '''
        seq = 'ACTGUN'
        self.nuc = seq
        self.aaComp = self.aaComp = {i:0 for i in NucParams.rnaCodonTable.values()} #retrives the single letter amino acid codes
        self.nucComp = {nuc : 0 for nuc in self.nuc}
        self.codonComp = {codon : 0 for codon in NucParams.rnaCodonTable.keys()} #retrives the codons in the rnaCodonTable

    def validCodon(self, codon) :
        '''
        Checks for valid codons and gets rid of ones that are invalid.
        '''
        for n in codon :
            if n == 'A' or n == 'C' or n == 'T' or n == 'G' or n == 'U' :
                continue
            else :
                return False
        return True

    def addSequence(self, thisSequence) :
        '''
        Update all the dictionaries from init method to accept additional sequences from the {ACTGUN} alphabet
        '''
        thisSequence = thisSequence.upper()
        # print(thisSequence)
        for nuc in thisSequence:
            if nuc in self.nucComp: # Check if it's in self.nucComp dictionary
                self.nucComp[nuc] += 1
        # print(self.nucComp)
        thisSequence = thisSequence.replace("T", "U") # change any DNA sequence to RNA for aa and codon composition
        thisSequence = thisSequence.replace(' ', '') # account for the spaces in the sequences

        protein = []
        numCodon = len(thisSequence) // 3 # count codons

        for i in range(0, numCodon) :
            start = i * 3
            stop = start + 3
            codon = thisSequence[start :stop]
            if self.validCodon(codon) : # check if codon is valid
                if codon in self.codonComp :
                    self.codonComp[codon] += 1
                    protein.append(self.rnaCodonTable[codon])
                if codon in NucParams.rnaCodonTable :
                    aa = NucParams.rnaCodonTable[codon]
                    self.aaComp[aa] += 1

    def aaComposition(self) :
        '''
        Returns all 20 single letter amino acid code dictionary
        '''
        return self.aaComp

    def nucComposition(self) :
        '''
        Returns a dictionary of counts of valid nucleotides found in the analysis.
        '''
        return self.nucComp

    def codonComposition(self) :
        '''
        Returns the codon keys from the rnaCodonTable and stores codons in RNA format with their counts
        '''
        return self.codonComp

    def nucCount(self) :
        '''
        Returns an integer value, summing every valid nucleotide found
        '''
        count = 0
        for n in self.nuc :
            count += self.nucComp[n]
        return count


class ProteinParam :
    '''Defines the init, aaCount, aaComposition, pI, charge, molar extinction, mass extinction, and molecular weight methods.
    Also contains the attributes aa2mw, mwH2O, aa2abs280, aa2chargePos, aa2chargeNeg, aaNterm, and aaCterm that can be called and used later in the different
    methods.
    '''
    # These tables are for calculating:
    #   molecular weight (aa2mw), along with the mol. weight of H2O (mwH2O)
    #   absorbance at 280 nm (aa2abs280)
    #   pKa of positively charged Amino Acids (aa2chargePos)
    #   pKa of negatively charged Amino acids (aa2chargeNeg)
    #   and the constants aaNterm and aaCterm for pKa of the respective termini
    # Feel free to move these to appropriate methods as you like

    # As written, these are accessed as class attributes, for example:
    # ProteinParam.aa2mw['A'] or ProteinParam.mwH2O
    aa2mw = {
        'A' : 89.093, 'G' : 75.067, 'M' : 149.211, 'S' : 105.093, 'C' : 121.158,
        'H' : 155.155, 'N' : 132.118, 'T' : 119.119, 'D' : 133.103, 'I' : 131.173,
        'P' : 115.131, 'V' : 117.146, 'E' : 147.129, 'K' : 146.188, 'Q' : 146.145,
        'W' : 204.225, 'F' : 165.189, 'L' : 131.173, 'R' : 174.201, 'Y' : 181.189
    }
    mwH2O = 18.015
    aa2abs280 = {'Y' : 1490, 'W' : 5500, 'C' : 125}

    aa2chargePos = {'K' : 10.5, 'R' : 12.4, 'H' : 6}
    aa2chargeNeg = {'D' : 3.86, 'E' : 4.25, 'C' : 8.33, 'Y' : 10}
    aaNterm = 9.69
    aaCterm = 2.34

    def __init__(self, protein) :
        '''
        To initialize the protein object and create a dictionary to operate the protein parameter methods more efficiently.
        '''
        self.aaDict = {}
        self.protein = protein
        for aa in 'ACDEFGHIKLMNPQRSTVWY' :  # initialize aaDict
            self.aaDict[aa] = 0
        for aa in protein :
            if aa in self.aaDict :  # To make sure the specific amino acid is in the table
                self.aaDict[aa] += 1

    def aaCount(self) :
        ''' Returns the single integer count of the valid amino acids'''
        return sum(self.aaDict.values())

    def normalpI(self) :
        ''' Finds and returns, using the charge method, the particular pH that yields a net charge of 0 or the one closest to 0.'''
        bestCharge = 10000
        bestpH = 7
        for pH100 in range(0, 1401) :
            pH = pH100 / 100
            curCharge = abs(self._charge_(pH))
            if curCharge < bestCharge :
                bestCharge = curCharge
                bestpH = pH
        return bestpH

    def pI(self, precision=2) :  # extra credit pI
        '''Finds the average of the high and low pH and returns the value '''
        lowpH = 0
        highpH = 14
        midpH = (highpH + lowpH) / 2
        while (highpH - lowpH) > (10 ** (-1 * precision)) :
            midpH = (highpH + lowpH) / 2  # average between high and low pH
            if self._charge_(midpH) > 0 :
                lowpH = midpH
            else :
                highpH = midpH
        return midpH

    def aaComposition(self) :
        '''Returns the aaDict dictionary created in the init method that includes all 20 amino acids.'''
        return self.aaDict

    def _charge_(self, pH) :
        '''Calculates the net charge at a particular pH'''

        def nCharge(pka) :
            '''Calculates the positive charge at a particular pH'''
            return (10 ** pka) / (10 ** pka + 10 ** pH)

        def cCharge(pka) :
            '''Calculates the negative charge at a particular pH'''
            return (10 ** pH) / (10 ** pka + 10 ** pH)

        netCharge = nCharge(ProteinParam.aaNterm) - cCharge(ProteinParam.aaCterm)
        for aa, pka in ProteinParam.aa2chargePos.items() :
            netCharge += float(self.aaDict.get(aa)) * nCharge(pka)
        for aa, pka in ProteinParam.aa2chargeNeg.items() :
            netCharge -= float(self.aaDict.get(aa)) * cCharge(pka)

        return (netCharge)

    def molarExtinction(self) :
        ''' Calculates the extinction coefficient using the amino acid composition'''
        x = 0
        y = 0
        z = 0
        co_myAAdict = {key : value for key, value in self.aaDict.items()}
        for i in self.aaDict :
            if (co_myAAdict.get(i) >= 1) and (i == 'Y') :  # Tyrosine = Y
                x = co_myAAdict.get(i) * 1490
            if (co_myAAdict.get(i) >= 1) and (i == 'W') :  # Tryptophan = W
                y = co_myAAdict.get(i) * 5500
            if (co_myAAdict.get(i) >= 1) and (i == 'C') :  # Cysteine = C
                z = co_myAAdict.get(i) * 125
        return (x + y + z)

    def massExtinction(self) :
        '''Calculate mass extinction by dividing the molecular weight by the molar extinction '''
        myMW = self.molecularWeight()
        return self.molarExtinction() / myMW if myMW else 0.0

    def molecularWeight(self) :
        '''Calculates the molecular weight by summing up the weights of each individual amino acid minus water'''
        totalMass = 0
        for aa in self.protein :
            # print(aa, '=', ProteinParam.aa2mw.get(aa))
            totalMass += (ProteinParam.aa2mw.get(aa)) - (ProteinParam.mwH2O)  # MWaa - MWH2O
            # print("totalMass = ", totalMass)
        return ProteinParam.mwH2O + totalMass


import sys


class FastAreader :


    def __init__(self, fname='') :

        '''contructor: saves attribute fname '''

        self.fname = fname

    def doOpen(self) :

        if self.fname == '' :

            return sys.stdin

        else :

            return open(self.fname)

    def readFasta(self) :

        header = ''

        sequence = ''

        with self.doOpen() as fileH :

            header = ''

            sequence = ''

            # skip to first fasta header

            line = fileH.readline()

            while not line.startswith('>') :
                line = fileH.readline()

            header = line[1 :].rstrip()

            for line in fileH :

                if line.startswith('>') :

                    yield header, sequence

                    header = line[1 :].rstrip()

                    sequence = ''

                else :

                    sequence += ''.join(line.rstrip().split()).upper()

        yield header, sequence


# myReader = FastAreader ('testTiny.fa');

# for head, seq in myReader.readFasta() :

#     print (head,seq)
