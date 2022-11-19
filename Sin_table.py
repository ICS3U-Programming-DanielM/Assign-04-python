#!/usr/bin/env python3
# Created By: Daniel Momoh
# Date: Oct 14th, 2022
# This program asks user to input a number an /n
# calculates the sin of that degree (0 to 360)./n
import math


def main():
    while True:
        # Set counter and sum
        counter = -1
        sum = 0
        # get User_Input from user
        User_Input = input("Enter a positive integer from 0 - 360 : ")
        # check to see if user inserted a string or integer
        try:
            User_number = int(User_Input)
        # if user inserted a string loop back to get User_Input
        except Exception:
            print("This is a string.")
            print("")
            continue
        # checks to see if User_number is negative /n
        # if it is negative it loops back to get a User_Input/n 
        if User_number < 0:
            print("This is a negative number.")
            print("")
            continue
        # checks to see if User_number is more than 360 /n
        # if more than 360 it loops back to get User_Input /n
        elif User_number > 360:
            print("This exceeds 360.")
            print("")
            continue
        # calculates the user_number and loops it till it gets to the requested number
        while User_number > counter:
            counter = counter + 1
            sum = math.sin(counter)
            print("")
            print("The sin of {} is equal to {:.4f}".format(counter, sum))
        break
    print("Thanks for playing.")


if __name__ == "__main__":
    main()
