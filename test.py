import math

if __name__ == "__main__":

    x1 = int(input('Please enter value of x1: '))
    y1 = int(input('Please enter value of y1: '))
    x2 = int(input('Please enter value of x2: '))
    y2 = int(input('Please enter value of y2: '))

    distance = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))

    print(distance)
