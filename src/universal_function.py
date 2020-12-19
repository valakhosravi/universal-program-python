from .generate_prime_numbers import generatePrimeNumbers
import math
from termcolor import colored


def universalFunction(inputs, instructions):
    Z = inputs.pop()
    S = calculateS(inputs)
    K = 1
    Y = 0
    i = -1  # we put -1 in i because i = i + 1 is at the start of while loop
    print(colored('Snapshots:', 'green'))
    while True:
        i = i + 1
        print(str(i + 1) + " - " + "S:" +
              str(S) + ", K:" + str(K) + ", Y:" + str(Y), end="")
        if K == len(instructions) + 1 or K == 0:
            Y = calculateS1(S)
            break
        U = right(instructions[K - 1])
        P = calculateP(right(U) + 1)
        print(", U: " + str(U) + ", P: " + str(P))
        if left(U) == 0:
            K = K + 1
            continue
        if left(U) == 1:
            S = S * P
            K = K + 1
            continue
        if not S % P == 0:
            K = K + 1
            continue
        if left(U) == 2:
            S = math.floor(S / P)
            K = K + 1
            continue
        break
        K = findMinIndex(instructions, left(U))
    print("\n")
    print("Output of the program is: ", Y)


def calculateS(inputs):
    l = len(inputs) * 2
    primeNumbers = generatePrimeNumbers(l)
    out = 1
    for i in range(1, l, 2):
        out = out * primeNumbers[i] ** inputs[int((i - 1) / 2)]
    return out


def calculateP(P):
    return generatePrimeNumbers(P).pop()


def calculateS1(S):
    i = 0
    while S % 2 == 0:  # because P_1 is 2
        S = S / 2
        i = i + 1
    return i


def findMinIndex(instructions, left_U):
    index = 0
    for i in range(0, len(instructions)):
        index = i
        if left(instructions[i]) + 2 - left_U == 0:
            return index
    return index


def left(vector):
    return vector[0]


def right(vector):
    return vector[1]


def fStar(x, y):
    return 2 ** x * (2 * y + 1) - 1
