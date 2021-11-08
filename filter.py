import sys
import csv

csv.field_size_limit(sys.maxsize)

'''
If climate change words in title, it gets filtered out. For the subdomains it also checks
for the keywords in the title. The articles (from New York Post and New York Times, max. 10.000)
get written to a file.
'''

def load_wordlist(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def titlefilter(title, wordlist):
    for word in wordlist:
        if word in title:
            return False
    return True

def titlefilter2(title, wordlist):
    for word in wordlist:
        if word in title:
            return True
    return  False

def main():
    articles = []
    left = 0
    right = 0
    wordlist = load_wordlist('wordlist.txt')
    try:
        if sys.argv[1] == 'all':
            with open('combined_csv.csv') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for splitted in lines:
                    try:
                        title = splitted[2].lower()
                        if titlefilter(title, wordlist):
                            if splitted[3] == 'New York Times':
                                if left <= 5000:
                                    splitted.append('l')
                                    articles.append(splitted)
                                    left += 1


                            elif splitted[3] == 'New York Post':
                                if right <= 5000:
                                    splitted.append('r')
                                    articles.append(splitted)                  
                                    right += 1   

                    except:
                        continue

            with open('test.csv','w') as output:
                writer = csv.writer(output)
                for i in articles:
                    x = [i[9],i[-1]]
                    writer.writerow(x)

        elif sys.argv[1] == 'trump':
            wordlist2 = ['trump']
            with open('combined_csv.csv') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for splitted in lines:
                    try:
                        title = splitted[2].lower()
                        if titlefilter(title, wordlist) and titlefilter2(title, wordlist2):
                            if splitted[3] == 'New York Times':
                                if left <= 5000:
                                    splitted.append('l')
                                    articles.append(splitted)
                                    left += 1


                            elif splitted[3] == 'New York Post':
                                if right <= 5000:
                                    splitted.append('r')
                                    articles.append(splitted)                  
                                    right += 1   

                    except:
                        continue

            with open('testtrump.csv','w') as output:
                writer = csv.writer(output)
                for i in articles:
                    x = [i[9],i[-1]]
                    writer.writerow(x)

        elif sys.argv[1] == 'education':
            wordlist2 = ['education', 'school', 'schools']
            with open('combined_csv.csv') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for splitted in lines:
                    try:
                        title = splitted[2].lower()
                        if titlefilter(title, wordlist) and titlefilter2(title, wordlist2):
                            if splitted[3] == 'New York Times':
                                if left <= 5000:
                                    splitted.append('l')
                                    articles.append(splitted)
                                    left += 1


                            elif splitted[3] == 'New York Post':
                                if right <= 5000:
                                    splitted.append('r')
                                    articles.append(splitted)                  
                                    right += 1   

                    except:
                        continue

            with open('testeducation.csv','w') as output:
                writer = csv.writer(output)
                for i in articles:
                    x = [i[9],i[-1]]
                    writer.writerow(x)

        elif sys.argv[1] == 'police':
            wordlist2 = ['police']
            with open('combined_csv.csv') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for splitted in lines:
                    try:
                        title = splitted[2].lower()
                        if titlefilter(title, wordlist) and titlefilter2(title, wordlist2):
                            if splitted[3] == 'New York Times':
                                if left <= 5000:
                                    splitted.append('l')
                                    articles.append(splitted)
                                    left += 1


                            elif splitted[3] == 'New York Post':
                                if right <= 5000:
                                    splitted.append('r')
                                    articles.append(splitted)                  
                                    right += 1   

                    except:
                        continue

            with open('testpolice.csv','w') as output:
                writer = csv.writer(output)
                for i in articles:
                    x = [i[9],i[-1]]
                    writer.writerow(x)

        elif sys.argv[1] == 'immigration':
            wordlist2 = ['immigration', 'immigrants', 'refugees','foreign','foreigners']
            with open('combined_csv.csv') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for splitted in lines:
                    try:
                        title = splitted[2].lower()
                        if titlefilter(title, wordlist) and titlefilter2(title, wordlist2):
                            if splitted[3] == 'New York Times':
                                if left <= 5000:
                                    splitted.append('l')
                                    articles.append(splitted)
                                    left += 1


                            elif splitted[3] == 'New York Post':
                                if right <= 5000:
                                    splitted.append('r')
                                    articles.append(splitted)                  
                                    right += 1   

                    except:
                        continue

        elif sys.argv[1] == 'economy':
            wordlist2 = ['economy', 'tax', 'taxes']
            with open('combined_csv.csv') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for splitted in lines:
                    try:
                        title = splitted[2].lower()
                        if titlefilter(title, wordlist) and titlefilter2(title, wordlist2):
                            if splitted[3] == 'New York Times':
                                if left <= 5000:
                                    splitted.append('l')
                                    articles.append(splitted)
                                    left += 1


                            elif splitted[3] == 'New York Post':
                                if right <= 5000:
                                    splitted.append('r')
                                    articles.append(splitted)                  
                                    right += 1   

                    except:
                        continue
            with open('testeconomy.csv','w') as output:
                writer = csv.writer(output)
                for i in articles:
                    x = [i[9],i[-1]]
                    writer.writerow(x)
    except IndexError:
        print("Pick one of: 'all', 'trump', 'police', 'education', 'immigration', 'economy'.")


    print('Left: ', left)
    print('Right: ', right)
    
main()
        



