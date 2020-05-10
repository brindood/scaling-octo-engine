# Python Nth col grabber Inf Runs
import os.path
from os import path

def __main__():
    cont = input("Enter \'1\' to end prog")
    while(cont != '1'):
        colGrab  = int(input("ColGrab: "))
        fileGrab = input("FileGrab: ")
        outFile  = input("OutputFile: ")
        try:
            f = open(fileGrab, "r")
            #  f = open("REDACTEDTESTFILE.txt", "r")
        except:
            print(fileGrab + "Not in pwd")
            print("Pwd: " + str(getcwd()))
            exit(1)
        
        if(path.exists(outFile)):
            choice = input(outFile + " will be overwritten. Ok? y/n")
            if(choice == "y"):
                fW = open(outFile, "w")
            else:
                print("One chance:\n")
                outFile  = input("New OutputFile: ")
                fW = open(outFile, "w")
            
        counter = 0
        for line in f:
            counter += 1
            splittemp = line.split(",")
            try:
                print(splittemp[colGrab] + "\n")
                fW.write(splittemp[colGrab] + "\n")
            except:
                print(str(counter) + " Line does not have value in column " + str(colGrab))

        f.close()
        fW.close()
        print("Done. If successful data in " + outFile)
        cont = input("Enter \'1\' to end prog")
    print("Prog quitting")
    exit(0)

if( __name__ == "__main__"):
    __main__()

