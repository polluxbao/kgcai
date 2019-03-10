import random as rnd
from numpy import *


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def distManh(vecA, vecB):
    return sum(abs(vecA - vecB))


def firstCent(dataSet, k):
    n = dataSet.shape[1]
    m = dataSet.shape[0]
    centroids = mat(zeros((k, n)))
    IndNum = arange(1, m + 1)
    print('IndNum:', IndNum)
    kInd = rnd.sample(list(IndNum), k)
    kInd = [a + b for a, b in zip(kInd, [-1] * (m + 1))]
    print('kInd:', kInd)
    for j in range(n):
        centroids[:, j] = dataSet[kInd, j]
    return centroids


def randCent(dataSet, k):
    n = dataSet.shape[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        maxJ = max(dataSet[:, j])
        rangeJ = float(maxJ - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
        # print('j = ', j)
        # print(centroids[:, j])
    return centroids


def kMeans(dataSet, k, distMeans=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True

    while clusterChanged:
        clusterChanged = False

        for i in range(m):
            minDist = inf
            minIndex = -1

            for j in range(k):
                distJI = distMeans(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j

            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True

            clusterAssment[i, :] = minIndex, minDist ** 2

        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0] == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment
