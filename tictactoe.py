import random
import sys


def computersTurn():
    if not boardIsFull():
        while True:
            randomNum = random.randint(0, 8)
            if board[randomNum] == " ":
                board[randomNum] = "X"
                showTheBoard()
                checkIfAnyOneWon()
                break
        playersTurn()

    else:
        print("\n\n\tNobody won!\n")
        sys.exit(0)


def playersTurn():
    if not boardIsFull():
        while True:
            playerChoose = input("Now it is your turn, which place?")
            validation = checkIfInputIsValid(playerChoose)
            if validation:
                # Player will chose a number between 1 to 9 (obs: 9 is included)
                # But the board list will start at zero that's why we subtract 1 from the Player's input.
                if board[int(playerChoose) - 1] == " ":
                    board[int(playerChoose) - 1] = "O"
                    showTheBoard()
                    checkIfAnyOneWon()
                    break
                else:
                    print("This place is already filled!")
        computersTurn()
    else:
        print("Nobody won!")
        sys.exit(0)


def boardIsFull():
    for item in board:
        if item == " ":
            return False
    return True
    
def checkIfInputIsValid(playerInput):
    try:
        toIntegerPlayerChoice = int(playerInput)
        if toIntegerPlayerChoice >= 0 and toIntegerPlayerChoice <= 9:
            return True
        else:
            print("Box numbers are from 1 to 9")
    # If conversion from string to integer failed
    except ValueError:
        print("Invalid input")

    return False


def checkIfAnyOneWon():
    wonCases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for case in wonCases:
        index_0 = case[0]
        index_1 = case[1]
        index_2 = case[2]
        if board[index_0] == board[index_1] and board[index_0] == board[index_2]:
            if board[index_0] != " ":
                if board[index_0] == "X":
                    print("\n\n\tYou Lost\n\n")
                elif board[index_0] == "O":
                    print("\n\n\tYou Won\n\n")
                showTheBoard()
                sys.exit(0)


def showTheBoard():
    print("\n=========================")
    for num in range(len(board)):
        if (num + 1) % 3 == 0:
            print(board[num])
            if (num + 1) != 9:
                print("----------")
        else:
            print(board[num], end=" | ")


def init():
    print("""
        \tWelcome to Tic Tac Toe Game!\n
    These are the number of each box
    1 | 2 | 3
    ----------
    4 | 5 | 6
    ----------
    7 | 8 | 9
    \n\n""")

    input("Press ENTER key to start!")
    computersTurn()


if __name__ == "__main__":
    board = [" "] * 9
    init()