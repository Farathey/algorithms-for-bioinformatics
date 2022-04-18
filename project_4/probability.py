# we use numpy.array() becasue it's easier to work on them insted of lists
import numpy as np
# random.random() draws random values between 0.0 and 1.0
from random import random


def generateMotifs(number):
    '''Generates matrix of arg number, 8-char long random motifs with probability specified in profilIN matrix\n
        It also returns matrix of standard deviations of generated matrix from profilIN matrix\n
        number = number of samples we want to generate'''

    profilIN = np.array([[0.2, 0.1, 0.5, 0.1, 0.1, 0.4, 0.2, 0.7],
                         [0.4, 0.6, 0.3, 0.3, 0.1, 0.4, 0.0, 0.2],
                         [0.3, 0.3, 0.1, 0.5, 0.6, 0.1, 0.2, 0.1],
                         [0.1, 0.0, 0.1, 0.1, 0.2, 0.1, 0.6, 0.0]])

    motifs = np.array([[0]*8]*4)
    standardDeviation = np.array([[0.0]*8]*4)

    # this loop generates matrix of (number) samples
    for i in range(number):
        for j in range(0, 8):
            value = random()
            if (value < profilIN[0][j]):
                motifs[0][j] += 1
            elif (value < (profilIN[0][j] + profilIN[1][j])):
                motifs[1][j] += 1
            elif (value < (profilIN[0][j] + profilIN[1][j] + profilIN[2][j])):
                motifs[2][j] += 1
            elif (value < (profilIN[0][j] + profilIN[1][j] + profilIN[2][j] + profilIN[3][j])):
                motifs[3][j] += 1

    # we divide values so they can be compared to profil_in matrix
    diminishedMotifs = motifs/number

    # this loop creates standard deviation martix with equation σ = √(((x - x̅)^2)/n), in our case n = 1
    for i in range(4):
        for j in range(8):
            standardDeviation[i][j] = np.sqrt(
                (diminishedMotifs[i][j] - profilIN[i][j])**2)

    return motifs, standardDeviation


def probabilityInPositions(motifs, number):
    ''' Returns matrix of probabilities of given base occuring in given position\n
        mottifs = matrix of motifs generated in generate motifs\n
        number = number of samples'''

    probability = np.array([[0.0]*8]*4)

    # this loop calculates probability in which given base occurse with equation P = |A| / |Ω|, where |A| is the number of occurrences
    # of given base and |Ω| is the number of drawed samples
    for i in range(4):
        for j in range(8):
            probability[i][j] = motifs[i][j]/number

    return probability


if __name__ == "__main__":
    # for generateMotifs(1) values are either 1 or 0 if probability in profilIN is greater than 0,
    # or just 0 if probability is equal to 0
    # deviation is always less than 1

    testValues, testDeviation = generateMotifs(1)

    for i in range(4):
        for j in range(8):
            assert testValues[i][j] == 1 or testValues[i][j] == 0
            assert testDeviation[i][j] < 1

    testProbability = probabilityInPositions(testValues, 1)

    # for probabilityInPositions(motifs, numberOfSample) values are between 0 and 1
    # as are values in classic probability
    for i in range(4):
        for j in range(8):
            assert 0 <= testProbability[i][j] <= 1
