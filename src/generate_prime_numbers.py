import math
def generatePrimeNumbers(length):
    if length == 0:
        return []
    arr = [2]
    count = 3
    while len(arr) < length:
        isprime = True
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break
        if isprime:
            arr.append(count)
        count += 1
    return arr
