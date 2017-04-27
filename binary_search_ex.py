import sys
import math

def binary_search_1(array, targetValue):
    min = 0
    # print("len(array) = " + str(array))
    max = len(array)-1
    guess = 0
    step = 0
    if targetValue in array:
        while (array[guess] != targetValue):
            guess = math.floor((max + min) / 2)
            if (array[guess] == targetValue):
                return guess
            elif (array[guess] >= targetValue):
                max = guess
            else:
                min = guess
            # print("Step #" + str(step) + " min: " + str(min) + ": guess = " + str(guess) +
            #       ", max: " + str(max) + ", array[guess] = " + str(array[guess]))
            step += 1
    else:
        return -1


def main():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    value = binary_search_1(primes, 73)
    print("Value 73 is at index " + str(binary_search_1(primes, 73)) + " in array.")
    print("Value 19 is at index " + str(binary_search_1(primes, 19)) + " in array.")
    print("Value 2 is at index " + str(binary_search_1(primes, 2)) + " in array.")
    print("Value 53 is at index " + str(binary_search_1(primes, 53)) + " in array.")

if __name__ == "__main__":
    sys.exit(main())
