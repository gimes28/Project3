from collections import Counter 
import socket
import os
import glob
from pathlib import Path

#docker run -it -v C:/School/"Spring 2024"/"INTRO TO CLOUD COMPUTING 5165"/Homework3/home:/home homework3_image

dataDir = os.path.dirname(os.path.realpath(__file__))
parentPath = Path(dataDir).parent
dataPath = str(parentPath)+"/home/data"
os.chdir(dataPath)
myFiles = glob.glob('*.txt')

def WordCount(fileName):
    with open(fileName, 'r') as file:
        line = file.read()
        line.lower()
        line.split()
        wordCount = len(line)
    file.close()
    return wordCount

def FreqWord(fileName):
    with open(fileName, 'r') as file:
        line = file.read()
        wordFreq = Counter(line.lower().split())
    file.close()
    words = wordFreq.most_common(3)
    return words
    
def main():
    outputFile = "../output/results.txt"
    with open(outputFile, 'w') as file:
        file.write("Files in home/data are : ")
        file.write('\n')
        numWordsTotal = 0
        for x in myFiles :
            file.write(x)
            file.write('\n')
            numWordsTotal += WordCount(x)
        file.write("Total number of words: ")
        file.write(str(numWordsTotal))
        for x in myFiles :
            if x == "IF.txt":
                file.write("\n3 most frequent words from IF: ")    
                file.write(str(FreqWord(x)))

        file.write("\n")
        file.write(socket.gethostbyname(socket.gethostname()))
    file.close()

if __name__ == "__main__":
    main()