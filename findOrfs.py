#!/usr/bin/env python3
# Name: Dami Ibrahim(oaibrahi)
# Group Members: None
from sequenceAnalysis import FastAreader
from sequenceAnalysis import OrfFinder
''' 
This program analyzes a FASTA formatted file of sequence DNA and finds the ORFs that are at least 100 nucleotides long 
then outputs formatted data to a text file using STDOUT
'''
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
            self.parser = argparse.ArgumentParser(description = 'Program prolog - a brief description of what this thing does',
                                                 epilog = 'Program epilog - some other stuff you feel compelled to say ',
                                                 add_help = True, #default is True
                                                 prefix_chars = '-',
                                                 usage = '%(prog)s [options] -option1[default] <input >output'
                                                 )
            self.parser.add_argument('-lG', '--longestGene', action = 'store', nargs='?', const=True, default=False, help='longest Gene in an ORF')
            self.parser.add_argument('-mG', '--minGene', type=int, choices= (0,100,200,300,500,1000), default=100, action = 'store', help='minimum Gene length')
            self.parser.add_argument('-s', '--start', action = 'append', default = ['ATG'],nargs='?',
                                    help='start Codon') #allows multiple list options
            self.parser.add_argument('-t', '--stop', action = 'append', default = ['TAG','TGA','TAA'],nargs='?', help='stop codon') #allows multiple list options
            self.parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
            if inOpts is None :
                self.args = self.parser.parse_args()
            else :
                self.args = self.parser.parse_args(inOpts)

def main():
    '''
    Find some genes and sorts through the ORF sizes and then outputs the frames depending on the test file.
    '''
    myReader = FastAreader() #Reads from STDIN
    CL = CommandLine()
    for head, seq in myReader.readFasta():
        print(head)

        myOrf = OrfFinder(seq, CL.args.start, CL.args.stop, longestGene=CL.args.longestGene, minOrf=CL.args.minGene)

        printList1 = myOrf.findOrfs(gene=1) #positive strand
        myOrf.rc(seq)
        printList2 = myOrf.findOrfs(gene=-1)#negative strand

        finalList = printList1 + printList2
        finalList.sort(key=lambda item : (item[3], -item[1]), reverse=True)#sorts by decreasing ORF size

        for frame in finalList: #finds frames that haven been sorted in the finalList
            seqFrame = frame[0]; start = frame[1]; stop = frame[2]; len = frame[3]
            print('{:+d} {:>5d}..{:>5d} {:>5d}'.format(seqFrame, start, stop, len)) #prints output

    #print(CL.args)

if __name__ == "__main__":
    main()#running from command line
