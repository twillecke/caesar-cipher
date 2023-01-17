#  import re

creditCards = "42536258796157867"
validFirstNums = ['4', '5', '6']


def checkFirstDigits(card):
    if card[0] in validFirstNums:
        print("Valid: first numbers")
    else:
        print("Invalid: first numbers.")


def checkNumLen(card):
    nOfDigits = (sum(c.isdigit() for c in card))
    if nOfDigits == 16:
        print("Valid: 16 number of digits.")

    else:
        print("Invalid: number of digits.")


def checkIsNumeric(card):
    card = card.replace('-', '')
    if card.isnumeric() is True:
        print("Valid: is only digits.")

    else:
        print("Invalid: must be only digits.")


def checkRepeatedNums(card):
    for digit in range(0, len(card) - 3):

        x = card[digit]
        x2 = card[digit + 1]
        x3 = card[digit + 2]
        x4 = card[digit + 3]

        if x == x2 and x == x3 and x == x4:  # checks if there are 4 consecutive repeated numbers
            print("Invalid: there are more than four consecutive repeated numbers")
            break

        else:
            print("Valid: there ano no four consecutive repeated numbers.")
            break


def validateCreditCard(card):
    checkFirstDigits(card)
    checkNumLen(card)
    checkIsNumeric(card)
    checkRepeatedNums(card)


validateCreditCard(creditCards)
