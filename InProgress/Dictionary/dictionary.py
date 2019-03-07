import requests
from bs4 import BeautifulSoup
import re

f= open("WordList.txt","r")
contents = f.readlines()

def writeDef(definition):
    fText = re.sub(r"<.*?>", "", definition)
    fText = re.sub(r"([b-n]\.\s\s)", r"\n\t   \1", fText)
    with open("Result.txt", "a") as resultFile:
        resultFile.write("\n\t"+fText)

for content in contents:
    word = content.strip()
    data = requests.get('https://www.thefreedictionary.com/{}'.format(word))
    soup = BeautifulSoup(data.text, 'html.parser')
    with open("Result.txt", "a") as wordFile:
        wordFile.write("\n-"+word)
    if len(soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-list")) != 0:
        dsList = [soup.select("#Definition section[data-src='hm'] .pseg .ds-list:nth-of-type(1)"),soup.select("#Definition section[data-src='hm'] .pseg .ds-list:nth-of-type(2)")]
        for Meaning in dsList:
            if len(Meaning) !=0:
                Meaning = str(Meaning[0])
                writeDef(Meaning)
    elif len(soup.select("#Definition section[data-src='hm'] .pseg .ds-single")) != 0:
        print("dsSingle",word)
        dsSingle = str(soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-single")[0])
        # print(dsSingle)
        fText = re.sub(r"<.*?>", "", dsSingle)
        with open("Result.txt", "a") as resultFile:
            resultFile.write("\n\t"+fText)
    else:
        print("skipped",word)

###
# word = input('Enter the word ')
# data = requests.get('https://www.thefreedictionary.com/{}'.format(word))
# soup = BeautifulSoup(data.text, 'html.parser')

# Mean = [soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-list:nth-of-type(1)"),soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-list:nth-of-type(2)")]

# print("-"+word)


# if len(Mean[0]) !=0:
    # Mean[0] = str(Mean[0][0]);
    # writeDef(Mean[0])
# if len(Mean[1]) !=0:
    # Mean[1] = str(Mean[1][0]);
    # writeDef(Mean[1])
