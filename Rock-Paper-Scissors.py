#!/usr/bin/env python3
#This is answer to exercise number 8


player1 = input("Hi Player 1 we are playing rock-sicssors-paper, insert your choice: ")
player2 = input("Hi Player 2we are playing rock-sicssors-paper, insert your choice: ")

while player1 == "rock":
    if player2 == "paper":
        print("Player 2 win")
    else:
        print("Player 1 win")
        break
while player1 == "sicssors":
    if player2 == "rock":
        print("Player 2 win")
    else:
        print("Player 1 win")
        break
while player1 == "paper":
    if player2 == "sicssors":
        print("Player 2 win")
    else:
        print("Player 1 win")
        break

