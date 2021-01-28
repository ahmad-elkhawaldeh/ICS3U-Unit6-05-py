#!/usr/bin/env python3

# Created by: Ahmad
# Created on: Jan 2021
# This program uses an array



def getAvg(array):
    total = 0
    for loop in array:
        total += loop
    return total//len(array)


def main():
    array = []
    number = 0
    print("Please enter 1 mark at a time. Enter -1 to end.");
    while(True):
        number = int(input("What is your mark? (as %) : "));
        if (number == -1):
                break
        array.append(number)
        
    print("The average is ",getAvg(array),"%")


if __name__ == "__main__":
    main()
