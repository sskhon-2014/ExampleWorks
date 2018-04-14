from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

"""
Reads in HTML file with matched abstracts from Perl script and outputs excel sheet with relevant columns.
"""

data = open('data/03-06-2018.html', encoding="utf-8")
soup = BeautifulSoup(data, 'lxml')

data_dict = {'Article': [], 'Link': [], 'Journal': [], 'Abstract': [], 'PMID': [], 'Sentence Scope': []}

def is_valid(index, arr):
    return index >= 0 and index < len(arr)

for a in soup.find_all('a'):
    data_dict['Article'].append(a.text)
    data_dict['Link'].append(a['href'])
    uids = re.search(r'\d{7,}', a['href']) # Some of the links have multiple PMIDs (citated articles)
    if uids.group() == "8" or uids.group() == "9": # 7 digit PMID (Hardcoded for 1997-2007)
        data_dict['PMID'].append(uids.group()[:7])
    else: # 8 digit PMID
        data_dict['PMID'].append(uids.group()[:8])
for p in soup.find_all('p', id='Journal'):
    data_dict['Journal'].append(p.text)
for p in soup.find_all('p', id='Abstract'):
    data_dict['Abstract'].append(p.text)
    sentences = re.findall(r'[^.!?\s][^.!?]*(?:[.!?](?![\'\"]?\s|$)[^.!?]*)*[.!?]?[\'\"]?(?=\s|$)', p.text)
    match = ["% sensitivity", "% specificity"]
    found = False
    index = 0
    upstream, downstream = "", ""
    for sentence in sentences:
        if any(x in sentence for x in match):
            if is_valid(index - 2, sentences):
                upstream = sentences[index - 2] + sentences[index - 1]
            elif is_valid(index - 1, sentences):
                upstream = sentences[index - 1]
            if is_valid(index + 2, sentences):
                downstream = sentences[index + 1] + sentences[index + 2]
            elif is_valid(index + 1, sentences):
                downstream = sentences[index + 1]
            data_dict['Sentence Scope'].append(upstream + " " + sentences[index] + " " + downstream)
            found = True
            break
        index += 1
    if not found:
        data_dict['Sentence Scope'].append("Sentences not found") # after bug fix, no instances w/o match

df = pd.DataFrame.from_dict(data_dict)
df.head()

# Removing duplicates based on Article Title
df = df.drop_duplicates('Article')
df = df.reset_index(drop=True)

# Converting data into Excel sheet
from pandas import ExcelWriter
writer = ExcelWriter('data/03-06-2018.xlsx')
df.to_excel(writer)
writer.save()
