import csv
import random
import math
import operator


def loadDataset(filename, split, trainingSet=[] , testSet=[]):
    with open(filename, 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])
                
def Distance(instance1, instance2, length):
    d = 0
    for x in range(length):
        d += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(d)
    
def Neighbors(trainingSet, testInstance, k):
    di = []
    l = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = Distance(testInstance, trainingSet[x], l)
        di.append((trainingSet[x], dist))
    di.sort(key = operator.itemgetter(1))
    n = []
    for x in range(k):
        n.append(di[x][0])
    return n
    
def Response(n):
    classVotes = {}
    for x in range(len(n)):
        response = n[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]
    
def Accuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
                
def main():
    trainingSet=[]
    testSet=[]
    split = 0.6
    loadDataset('C:\Users\Manas\Desktop\New folder\dataset\Iris.csv', split, trainingSet, testSet)
    print 'Train set: ' + repr(len(trainingSet))
    print 'Test set: ' + repr(len(testSet))    
    predictions=[]
    k = 3
    for x in range(len(testSet)):
        neighbors = Neighbors(trainingSet, testSet[x], k)
        result = Response(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
    accuracy = Accuracy(testSet, predictions)
    print 'Accuracy: ', accuracy

if __name__=="__main__":
    main()

