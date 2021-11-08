import csv
import random

test_file = 'test.csv'

def read_corpus(corpus_file):
    '''Read in review data set and returns docs and labels'''
    documents = []
    labels = []
    with open(corpus_file, encoding='utf-8') as f:
        lines = csv.reader(f, delimiter=',')
        for line in lines:
            tokens = line
            documents.append(tokens[0])
            # 6-class problem: books, camera, dvd, health, music, software
            labels.append(tokens[-1])
    return documents, labels

def shuffle_dependent_lists(l1, l2):
    '''Shuffle two lists, but keep the dependency between them'''
    tmp = list(zip(l1, l2))
    # Seed the random generator so results are consistent between runs
    random.Random(123).shuffle(tmp)
    return zip(*tmp)

def split_data(X_full, Y_full, test_percentage, shuffle):
    '''Splits the data into train & test sets, everything up to the split point is used as training, the rest for testing. The shuffle flag can be used to shuffle the sets beforehand'''
    split_point = int((1.0 - test_percentage)*len(X_full))
    #  shuffles the lists before splitting, keeping the dependency so each instance still has correct label 
    if shuffle:
        X_full, Y_full = shuffle_dependent_lists(X_full, Y_full)
    X_train = X_full[:split_point]
    Y_train = Y_full[:split_point]
    X_test = X_full[split_point:]
    Y_test = Y_full[split_point:]
    return list(X_train), list(Y_train), list(X_test), list(Y_test)

def main():

    X_full, Y_full = read_corpus(test_file)
    X_train, Y_train, X_testdev, Y_testdev = split_data(X_full, Y_full, 0.40, True)
    X_dev, Y_dev, X_test, Y_test = split_data(X_testdev, Y_testdev, 0.50, False)

    with open('trainID.csv','w') as output:
        writer = csv.writer(output)
        for i,j in zip(X_train, Y_train):
            x = [i,j]
            writer.writerow(x)

    with open('devID.csv','w') as output:
        writer = csv.writer(output)
        for i,j in zip(X_dev, Y_dev):
            x = [i,j]
            writer.writerow(x)

    with open('testID.csv','w') as output:
        writer = csv.writer(output)
        for i,j in zip(X_test, Y_test):
            x = [i,j]
            writer.writerow(x)

main()

