import sys
from enum import Enum
import random

wheelValues = [2500, 200, 900, 700, 300, 800, 750, 400, "Bankrupt", "Million", "Bankrupt", 600, 350, 400, 900, "Bankrupt", 650, 200, 700, "Lose a Turn", 800, 950, 450, 750, 300, "Bankrupt"]
puzzles = ["SUMMERTIME", "SANDWICHES", "JAMES BOND", "SCARLETT JOHANSEN", "BRAD PITT", "HARRY POTTER", "SPAGHETTI",
    "CHICKEN ALFREDO", "INSPECTOR GADGET", "SPIDERMAN", "THE AVENGERS", "LOVE ME LIKE YOU DO", "DIE ANOTHER DAY"]
calledLetters = []
calledPuzzles = []

class Players(Enum):
	PLAYER1 = 1
	PLAYER2 = 2
	PLAYER3 = 3

class Rounds(Enum):
    ROUND1 = 1
    ROUND2 = 2
    ROUND3 = 3
    BONUSROUND = 4

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

winnings = [0, 0, 0]
extraMillions = [False, False, False]

player1TotalWinnings = 0
player2TotalWinnings = 0
player3TotalWinnings = 0

player1RoundWinnings = 0
player2RoundWinnings = 0
player3RoundWinnings = 0

player1ExtraMillion = False
player2ExtraMillion = False
player3ExtraMillion = False

puzzleSolved = False
activePlayer = Players.PLAYER1
activeRound = Rounds.ROUND1
activePuzzleIndex = random.randint(0, len(puzzles))
activePuzzle = puzzles[activePuzzleIndex]
calledPuzzles.append(activePuzzle)

print("Puzzle is: \nOOOOOOOOOO\n\n")

while not puzzleSolved:
    if sys.version_info[0] < 3:
        raw_input("Press enter to spin the wheel")
    else:
        input("Press enter to spin the wheel")
    
    wheelPosition = random.randint(0, len(wheelValues) - 1)
    if wheelValues[wheelPosition] == "Bankrupt":
        if Players.PLAYER1 == activePlayer:
            player1Winnings = 0
            activePlayer = Players.PLAYER2
        elif Players.PLAYER2 == activePlayer:
            player2Winnings = 0
            activePlayer = Players.PLAYER3
        elif Players.PLAYER3 == activePlayer:
            player3Winnings = 0
            activePlayer = Players.PLAYER1
        continue
    elif wheelValues[wheelPosition] == "Lose a Turn":
        if Players.PLAYER1 == activePlayer:
            activePlayer = Players.PLAYER2
        elif Players.PLAYER2 == activePlayer:
            activePlayer = Players.PLAYER3
        elif Players.PLAYER3 == activePlayer:
            activePlayer = Players.PLAYER1
        continue
    elif wheelValues[wheelPosition] == "Million":
        if Players.PLAYER1 == activePlayer:
            player1ExtraMillion = True
        elif Players.PLAYER2 == activePlayer:
            player2ExtraMillion = True
        elif Players.PLAYER3 == activePlayer:
            player3ExtraMillion = True
        continue
    if Players.PLAYER1 == activePlayer:
        print("Player 1 landed on {0}".format(wheelValues[wheelPosition]))
        print("What would you like to do?")
        choice = input("c: Call a letter\nb: Buy a vowel\ns: Solve the puzzle\n> ")
        if choice.lower() == "c":
            letter = input("Call a letter> ")
            if letter.upper() in puzzle:
                if letter in calledLetters:
                    print("Letter has already been called. Player 2 up to spin.")
                    activePlayer = Players.PLAYER2
                    continue
                calledLetters.append(letter)
                find(activePuzzle, letter)
                occurences = puzzle.count(letter)
                earnings = wheelValues[wheelPosition] * occurences
                player1RoundWinnings += earnings
                print("Player 1's total {0}".format(player1RoundWinnings))
            else:
                print("No {0} in puzzle".format(letter))
                activePlayer = Players.PLAYER2
        elif choice.lower() == "b":
            vowel = input("Enter vowel> ")
            if vowel.upper() in puzzle:
                print("{0} in puzzle".format(vowel))
            else:
                print("No {0} in puzzle".format(vowel))
            player1Winnings = player1Winnings - 250 if player1Winnings >= 250 else 0
        elif choice.lower() == "s":
            solvedPuzzle = input("Solve the puzzle> ")
            if solvedPuzzle.upper() == puzzle:
                print("You solved the puzzle")
                player1TotalWinnings += player1RoundWinnings
                player2RoundWinnings = 0
                player3RoundWinnings = 0
                if activeRound == Rounds.ROUND1:
                    activePuzzleIndex = random.randint(0, len(puzzles))
                    activePuzzle = puzzles[activePuzzleIndex]
                    while activePuzzle in calledPuzzles:
                        activePuzzleIndex = random.randint(0, len(puzzles))
                        activePuzzle = puzzles[activePuzzleIndex]
                    calledPuzzles.append(activePuzzle
                    activeRound = Rounds.ROUND2
                elif activeRound == Rounds.ROUND2:
                    activePuzzleIndex = random.randint(0, len(puzzles))
                    activePuzzle = puzzles[activePuzzleIndex]
                    while activePuzzle in calledPuzzles:
                        activePuzzleIndex = random.randint(0, len(puzzles))
                        activePuzzle = puzzles[activePuzzleIndex]
                    calledPuzzles.append(activePuzzle
                    activeRound = Rounds.ROUND3
                elif activeRound == Rounds.ROUND3:
                    winningPlayer = max(player1TotalWinnings, player2TotalWinnings, player3TotalWinnings)
                    if winningPlayer == player1TotalWinnings:
                        print("Player 1 wins the game")
                    elif winningPlayer == player2TotalWinnings:
                        print("Player 2 wins the game")
                    elif winningPlayer == player3TotalWinnings:
                        print("Player 3 wins the game")
                    print("End of game")
            else:
                print("That is incorrect")
                activePlayer = Players.PLAYER2
    elif Players.PLAYER2 == activePlayer:
        print("Player 2 landed on {0}".format(wheelValues[wheelPosition]))
        letter = input("Call a letter> ")
        if letter.upper() in puzzle:
            occurences = puzzle.count(letter)
            earnings = wheelValues[wheelPosition] * occurences
            player2Winnings += earnings
            print("Player 2's total {0}".format(player2Winnings))
        else:
            print("No {0} in puzzle".format(letter))
            activePlayer = Players.PLAYER3
    elif Players.PLAYER3 == activePlayer:
        print("Player 3 landed on {0}".format(wheelValues[wheelPosition]))
        letter = input("Call a letter> ")
        if letter.upper() in puzzle:
            occurences = puzzle.count(letter)
            earnings = wheelValues[wheelPosition] * occurences
            player3Winnings += earnings
            print("Player 3's total {0}".format(player3Winnings))
        else:
            print("No {0} in puzzle".format(letter))
            activePlayer = Players.PLAYER1
    if puzzle.count("X") == len(puzzle):
        puzzleSolved = True 
