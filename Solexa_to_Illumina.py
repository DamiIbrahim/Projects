'''
Savi Dhoat & Dami Ibarahim
Professor David Bernick
BME 160
References:
David Bernick
Derfel

Notes:Translating from solexa to illumina; illumina B style requires that you modify the sequence and quality score;
Precompute all 40 scores using log
and exponentiation and turn it into a dictionary for the translation; Reading q scores from an existing file and writing
out q scores using a
translation dictionary; The data source used is the ASCII table'''
import sys
class FastQreader :
    def __init__(self, fname='') :
        '''contructor: saves attribute fname '''
        self.fname = fname

    def doOpen(self) :
        if self.fname == '' :
            return sys.stdin
        else :
            return open(self.fname)

    def readFastq(self) :
        header = ''
        sequence = ''
        with self.doOpen() as fileH :
            startingLine = 0
            header = ''
            sequence = ''
            qualHeader = ''
            qualScore = ''
            # skip to first fastq header
            for line in fileH :
                if line.rstrip() :
                    startingLine += 1  # if a new line is detected
                    actualLine = startingLine % 4  # modded by 4 because there are 4 lines, CITATION: DERFEL, BME 160.

                    if actualLine == 1 and line.startswith(
                            '@') :  # 1 mod 4 =1, this means it's the first line, which is the first header line of the fasta, it must also include the @ sign
                        header = line[1 :].rstrip()
                    elif actualLine == 2 :  # 2 mod 4 =2, this means it's the second line, which is the sequence line of the fasta
                        sequence = line.rstrip()
                        sequence = sequence.upper()
                        sequence = sequence.replace('.', 'N').replace('*', 'N').replace('n', 'N')
                    elif actualLine == 3 and line.startswith(
                            '+') :  # 3 mod 4 =3, this means it's the third line, which is the second header line of the fasta, it must also include the + sign
                        qualHeader = line[1 :].rstrip()
                    elif actualLine == 0 :  # 4 mod 4 =0, this means it's the fourth line, which is the quality score line of the fasta
                        qualScore = line.rstrip()
                    yield header, sequence, qualHeader, qualScore


class CommandLine() :
    '''
    Handle the command line, usage and help requests.
    CommandLine uses argparse, now standard in 2.7 and beyond.
    it implements a standard command line argument parser with various argument options, a standard usage and help.

    attributes:
    all arguments received from the commandline using .add_argument will be
    avalable within the .args attribute of object instantiated from CommandLine.
    For example, if myCommandLine is an object of the class, and requiredbool was
    set as an option using add_argument, then myCommandLine.args.requiredbool will
    name that option.
    '''

    def __init__(self, inOpts=None) :
        '''
        Implement a parser to interpret the command line argv string using argparse.
        '''

        import argparse
        self.parser = argparse.ArgumentParser(
            description='Program prolog - a brief description of what this thing does',
            epilog='Program epilog - some other stuff you feel compelled to say ',
            add_help=True,  # default is True
            prefix_chars='-',
            usage='%(prog)s [options] -option1[default] <input >output'
            )
        self.parser.add_argument('-P33in', '--PHRED33input', action='store', nargs='?', const=True, default=False)
        self.parser.add_argument('-P64in', '--PHRED64input', action='store', nargs='?', const=True, default=False)
        self.parser.add_argument('-P64Bin', '--PHRED64Binput', action='store', nargs='?', const=True, default=False)
        self.parser.add_argument('-P64SOLin', '--PHRED64SOLinput', action='store', nargs='?', const=True, default=False)
        self.parser.add_argument('-P33out', '--PHRED33output', action='store', nargs='?', const=True, default=False)
        self.parser.add_argument('-P64out', '--PHRED64output', action='store', nargs='?', const=True, default=False)
        if inOpts is None :
            self.args = self.parser.parse_args()
        else :
            self.args = self.parser.parse_args(inOpts)


class Translator() :
    '''Mapping between the different inputs and outputs.'''

    def PHRED64inPHRED33out(self, qualScore) : # done
        '''Takes the PHRED64input and maps it to the default PHRED33output'''
        newScore = ''
        for char in qualScore :
            rawScore = ord(char) - 31#gets number from ascii table and adds 31
            newScore += chr(rawScore)#converts that number to its corresponding unicode character
        return (newScore)

    def PHRED33inPHRED64out(self, qualScore) :  # done
        '''Takes PHRED33input and maps it to PHRED64output'''
        newScore = ''
        for char in qualScore :
            rawScore = ord(char) + 31
            newScore += chr(rawScore)
        return (newScore)

    def PHRED64SOLinPHRED64out(self, qualScore) :
        '''Takes the PHRED64 with solexa interpretation of Q score and maps it to PHRED64output'''
        solexaQ = {-5 : 1, -4 : 1, -3 : 2, -2 : 2, -1 : 3, 0 : 3, 1 : 4, 2 : 4, 3 : 5, 4 : 5,
                   5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 : 10, 10 : 10, 11 : 11, 12 : 12, 13 : 13, 14 : 14, 15 : 15,
                   16 : 16, 17 : 17, 18 : 18, 19 : 19, 20 : 20, 21 : 21, 22 : 22, 23 : 23, 24 : 24, 25 : 25,
                   26 : 26, 27 : 27, 28 : 28, 29 : 29, 30 : 30, 31 : 31, 32 : 32, 33 : 33, 34 : 34, 35 : 35,
                   36 : 36, 37 : 37, 38 : 38, 39 : 39, 40 : 40
                   }
        # these values are from solexa to phred
        asciiQ = {59 : -5, 60 : -4, 61 : -3, 62 : -2, 63 : -1, 64 : 0, 65 : 1, 66 : 2, 67 : 3, 68 : 4, 69 : 5, 70 : 6,
                  71 : 7, 72 : 8,
                  73 : 9, 74 : 10, 75 : 10, 76 : 11, 77 : 12, 78 : 13, 79 : 14, 80 : 15, 81 : 16, 82 : 17, 83 : 18,
                  84 : 19, 85 : 20,
                  86 : 21, 87 : 22, 88 : 23, 89 : 24, 90 : 25, 91 : 26, 92 : 27, 93 : 28, 94 : 29, 95 : 30, 96 : 31,
                  97 : 32, 98 : 33, 99 : 34,
                  100 : 35, 101 : 36, 102 : 37, 103 : 38, 104 : 39, 105 : 40}
        # these values are solexa to ascii table

        newScore = ''

        for char in qualScore :
            asciiScore = ord(char) #gets number from ascii table
            solexaScore = asciiQ[asciiScore] #converts number to solexa Q score
            newScore += chr(solexaQ[solexaScore] + 31) #converts solexa Q score to character

        return (newScore)

    def PHRED64SOLinPHRED33out(self, qualScore) :
        '''Takes the PHRED64 with solexa interpretation of Q score and maps it to PHRED33output'''
        solexaQ = {-5 : 1, -4 : 1, -3 : 2, -2 : 2, -1 : 3, 0 : 3, 1 : 4, 2 : 4, 3 : 5, 4 : 5,
                   5 : 6, 6 : 7, 7 : 8, 8 : 9, 9 : 10, 10 : 10, 11 : 11, 12 : 12, 13 : 13, 14 : 14, 15 : 15,
                   16 : 16, 17 : 17, 18 : 18, 19 : 19, 20 : 20, 21 : 21, 22 : 22, 23 : 23, 24 : 24, 25 : 25,
                   26 : 26, 27 : 27, 28 : 28, 29 : 29, 30 : 30, 31 : 31, 32 : 32, 33 : 33, 34 : 34, 35 : 35,
                   36 : 36, 37 : 37, 38 : 38, 39 : 39, 40 : 40
                   }
        # these values are from solexa to phred
        asciiQ = {59 : -5, 60 : -4, 61 : -3, 62 : -2, 63 : -1, 64 : 0, 65 : 1, 66 : 2, 67 : 3, 68 : 4, 69 : 5, 70 : 6,
                  71 : 7, 72 : 8, 73 : 9, 74 : 10, 75 : 10, 76 : 11, 77 : 12, 78 : 13, 79 : 14, 80 : 15, 81 : 16,
                  82 : 17, 83 : 18, 84 : 19, 85 : 20, 86 : 21, 87 : 22, 88 : 23, 89 : 24, 90 : 25, 91 : 26, 92 : 27,
                  93 : 28, 94 : 29, 95 : 30, 96 : 31, 97 : 32, 98 : 33, 99 : 34, 100 : 35, 101 : 36, 102 : 37,
                  103 : 38, 104 : 39, 105 : 40
                  }
        # these values are solexa to ascii table

        newScore = ''

        for char in qualScore :
            asciiScore = ord(char)
            solexaScore = asciiQ[asciiScore]
            newScore += chr(solexaQ[solexaScore] + 64)

        return (newScore)

    def P64BinPHRED33out(seq, qualScore) :  # done
        '''Takes PHRED64 with B offset in quality values and maps it to PHRED33output'''
        Bin = {'B' : 66, 'C' : 67, 'D' : 68, 'E' : 69, 'F' : 70, 'G' : 71, 'H' : 72, 'I' : 73, 'J' : 74, 'K' : 75,
               'L' : 76, 'M' : 77, 'N' : 78, 'O' : 79, 'P' : 80, 'Q' : 81, 'R' : 82, 'S' : 83, 'T' : 84, 'U' : 85,
               'V' : 86, 'W' : 87, 'X' : 88, 'Y' : 89, 'Z' : 90, '[' : 91, '\\' : 92, ']' : 93, '^' : 94, '_' : 95,
               '`' : 96, 'a' : 97, 'b' : 98, 'c' : 99, 'd' : 100, 'e' : 101, 'f' : 102, 'g' : 103, 'h' : 104, 'i' : 105,
               'j' : 106
               }

        # if 'B' in qualScore:
        # countB = qualScore.count("B") #takes count of B
        # qualScore = qualScore[0:len(qualScore)-countB] + countB*'N' #takes the quality score and gets rid of all the Bs and replaces with Ns
        # return qualScore

        # else:
        # return qualScore

        newScore = ''

        for char in qualScore :
            rawScore = Bin[char] - 31 #Gets integer from Bin dictionary substracts 31
            newScore += chr(rawScore) #converts that number to its corresponding character

        return (newScore)

    def P64BinPHRED64out(seq, qualScore) :  # done
        '''Takes PHRED64 with B offset in quality values and maps it to PHRED64output'''
        Bin = {'B' : 66, 'C' : 67, 'D' : 68, 'E' : 69, 'F' : 70, 'G' : 71, 'H' : 72, 'I' : 73, 'J' : 74, 'K' : 75,
               'L' : 76, 'M' : 77, 'N' : 78, 'O' : 79, 'P' : 80, 'Q' : 81, 'R' : 82, 'S' : 83, 'T' : 84, 'U' : 85,
               'V' : 86, 'W' : 87, 'X' : 88, 'Y' : 89, 'Z' : 90, '[' : 91, '\\' : 92, ']' : 93, '^' : 94, '_' : 95,
               '`' : 96, 'a' : 97, 'b' : 98, 'c' : 99, 'd' : 100, 'e' : 101, 'f' : 102, 'g' : 103, 'h' : 104, 'i' : 105,
               'j' : 106
               }

        newScore = ''

        for char in qualScore :
            rawScore = Bin[char]
            newScore += chr(rawScore)

        return (newScore)


def main(inFile='') :
    '''Establishes different inputs and outputs and ultimately prints out the updated FastQ file.'''
    # CITATION: MAIN METHODOLOGY APPROACH BY PROFESSOR DAVID BERNICK.

    myReader = FastQreader(inFile)
    thisCommandLine = CommandLine()
    myTranslator = Translator()
    #Using command line options to assign each input and output
    P33input = thisCommandLine.args.PHRED33input
    P64input = thisCommandLine.args.PHRED64input
    P64Binput = thisCommandLine.args.PHRED64Binput
    P64SOLinput = thisCommandLine.args.PHRED64SOLinput
    P33output = thisCommandLine.args.PHRED33output
    P64output = thisCommandLine.args.PHRED64output

    if P33input and P33output :  # P33 to P33
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            print('@' + header)  # @ symbol manually added in
            print(seq)
            print('+' + qualHeader)  # + symbol manually added in
            print(qualScore)
    if P64input and P64output :  # P64 to P64
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(qualScore)
    if P33input and P64output :  # P33 to P64
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            newQSeq = myTranslator.PHRED33inPHRED64out(qualScore)#calling function from translator class
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(newQSeq)
    if P64input and P33output :  # P64 to P33
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            newQSeq = myTranslator.PHRED64inPHRED33out(qualScore)
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(newQSeq)
    if P64Binput and P33output :  # P64B to P33
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            newQSeq = myTranslator.P64BinPHRED33out(qualScore)
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(newQSeq)
    if P64Binput and P64output :  # P64B to P33
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            newQSeq = myTranslator.P64BinPHRED64out(qualScore)
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(newQSeq)
    if P64SOLinput and P64output :  # P64SOLEXA to P33
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            newQSeq = myTranslator.PHRED64SOLinPHRED64out(qualScore)
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(newQSeq)
    if P64SOLinput and P33output :  # P64SOLEXA to P33
        for header, seq, qualHeader, qualScore in myReader.readFastq() :
            newQSeq = myTranslator.PHRED64inPHRED33out(qualScore)
            print('@' + header)
            print(seq)
            print('+' + qualHeader)
            print(newQSeq)


if __name__ == "__main__" :
    main('Galaxy1.solexa.fastq')

