#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program is a number guessing game

from random import randint


class number:
    def __init__(self):
        self.random_number = randint(1, 65500)
        self.user_number = 0

    def game(self):
        while True:
            self.user_number = int(input("Enter ypur guess: "))
            if self.user_number > self.random_number:
                print("your number is larger than mine")
                pass
            elif self.user_number < self.random_number:
                print("youe number is smaller than mine")
                pass
            elif self.user_number == self.random_number:
                print("You won")
                break
            else:
                print("What the hell did you do !!! i havent thought i that!")
                pass
if __name__ == "__main__":
    
    number().game()
