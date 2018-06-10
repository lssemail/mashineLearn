# encoding:utf-8
import sys
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
reload(sys)
sys.setdefaultencoding('utf-8')

def createDataSet():

    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):

    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat**2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

# 解析文本文件为NumPy矩阵
def file2matrix(filename):

    fr = open(filename)
    arrayOflines = fr.readlines()
    numberOfLines = len(arrayOflines)
    # 创建返回的NumPy矩阵
    returnMat = zeros((numberOfLines, 3))
    print returnMat
    classLabelVector = []
    index = 0
    for line in arrayOflines:
        line = line.strip()
        listFromLine = line.split("\t")
        returnMat[index, :] = listFromLine[0: 3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1

    return returnMat, classLabelVector

def matplotlibShowData(datingDataMat, datingLabels):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLabels), 15.0*array(datingLabels))
    plt.show()

if __name__ == '__main__':
    filename = 'data/datingTestSet2.txt'
    returnMat, classLabelVector = file2matrix(filename)

    matplotlibShowData(returnMat, classLabelVector)