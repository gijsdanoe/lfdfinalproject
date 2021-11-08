import json
import sys
import re
from collections import Counter
import csv



def make_filelist():
    filenames = []
    for i in range (1, 25):
        filename = f'''COP{i}.filt3.sub.json'''
        filenames.append(filename)
    filenames.append('COP6a.filt3.sub.json')
    return filenames
        

def main():
    with open('trainOD.csv', 'w') as output:
        writer = csv.writer(output)
        papercounter = Counter()
        # define newspapers and their counts
        papers_r = {'The Australian':6280,'The Times of India (TOI)':255, 'The Times (South Africa)':157}
        papers_l = {'Sydney Morning Herald (Australia)':5371, 'The Age (Melbourne, Australia)': 909, 'The Hindu':255, 'Mail & Guardian':157}
        filelist = make_filelist()
        for filename in filelist:
            with open(filename) as jsonfile:
                data = json.load(jsonfile)
                for article in data['articles']:
                    papername = article["newspaper"]
                    if papername in papers_r:
                    	if papercounter[papername] < papers_r[papername]:
                    		# remove newlines, as we want one article per line
                            rawtext = article["raw_text"].replace("\n", " ")
                            x = [rawtext, 'r']
                            writer.writerow(x)
                            papercounter[papername] += 1

                    elif papername in papers_l:
                        if papercounter[papername] < papers_l[papername]:
                            rawtext = article["raw_text"].replace("\n", " ")
                            x = [rawtext, 'l']
                            writer.writerow(x)
                            papercounter[papername] += 1
    print(papercounter)
main()
            

