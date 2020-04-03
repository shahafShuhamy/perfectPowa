#  Constants
BASE_NUMBER = 2

def main():
    place_user = input("please insert a number ")
    num = pow(int(place_user), BASE_NUMBER)
    if (place_user == "1"):
        print("1")
    else:
        print(findPerfectPow(int(place_user), num))

def findPerfectPow(index, numberOfTimes):
    numbers_array = [1]
    exponent =  BASE_NUMBER
    while(len(numbers_array).__le__(numberOfTimes)):
        numbers_array = numbers_array + getPoweredNumbers(exponent)
        numbers_array = removeDuplicates(numbers_array)
        numbers_array.sort()
        exponent += 1
    return numbers_array[int(index) - 1]

def removeDuplicates(array):
    return list(dict.fromkeys(array))

def getPoweredNumbers(expo):
    current_expo_number = []
    i = BASE_NUMBER
    while(i.__le__(expo)):
        current_expo_number.append(pow(i, expo))
        current_expo_number.append(pow(expo, i))
        i += 1
    return removeDuplicates(current_expo_number)

## program start ##
main()