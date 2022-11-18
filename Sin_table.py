#!/usr/bin/env python3
# Created By: Daniel Momoh
# Date: Oct 14th, 2022
# This program asks user to input a number an /n
# calculates the sin of that degree (0 to 360)./n
import math


def main():
    while True:
        counter = -1
        sum = 0
        User_Input = input("Enter a positive integer from 0 - 360 : ")
        try:
            User_number = int(User_Input)
        except Exception:
            print("")
            print("This is a string.")
            print("")
            continue
        if User_number < 0:
            print("")
            print("This is a negative number.")
            print("")
            continue
        elif User_number > 360:
            print("")
            print("This exceeds 360.")
            print("")
            continue
        while User_number > counter:
            counter = counter + 1
            sum = math.sin(counter)
            print("")
            print("The sin of {} is equal to {:.4f}".format(counter, sum))
        break
    print("Thanks for playing.")


if __name__ == "__main__":
    main()
