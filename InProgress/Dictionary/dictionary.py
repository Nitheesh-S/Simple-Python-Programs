import requests
from bs4 import BeautifulSoup
import re

# f= open("WordList.txt","r")
# contents = f.readlines()

# for content in contents:
#     # word = re.sub(r"(\n)", "", content)
#     word = content.strip()
#     data = requests.get('https://www.thefreedictionary.com/{}'.format(word))
#     soup = BeautifulSoup(data.text, 'html.parser')
#     definition = soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-list:nth-of-type(1)")
#     if len(definition) != 0:
#         definition = str(definition[0]);
#         fText = re.sub(r"<.*?>", "", definition)
#         fText = re.sub(r"([b-n]\.\s\s)", r"\n\t   \1", fText)
#         with open("Result.txt", "a") as myfile:
#             myfile.write("-"+word+"\n\t"+fText+"\n")

word = input('Enter the word ')

data = requests.get('https://www.thefreedictionary.com/{}'.format(word))
soup = BeautifulSoup(data.text, 'html.parser')

Mean = soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-list:nth-of-type(1)")

Mean2 = soup.select("#Definition section[data-src='hm'] .pseg:nth-of-type(1) .ds-list:nth-of-type(2)")

print("-"+word)
def writeDef(definition):
    if len(definition) != 0:
        fText = re.sub(r"<.*?>", "", definition)
        fText = re.sub(r"([b-n]\.\s\s)", r"\n\t   \1", fText)
        print("\t"+fText)

if len(Mean) !=0:
    Mean = str(Mean[0]);
    writeDef(Mean)
if len(Mean2) !=0:
    Mean2 = str(Mean2[0]);
    writeDef(Mean2)
# r"\n\1"
# lambda x: '\n' + str(x.group(0))