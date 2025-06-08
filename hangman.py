
#here are your global variables
letterGuesses = []
solved = []


#here are your functions
def drawHangman(n):
    if n == 0:
        print("  ----  ")
        print("     |  ")
        print("     |  ")
        print("     |  ")
        print("     |  ")
        print("-------")
    elif n == 1:
        print("  ----  ")
        print("  O  |  ")
        print("     |  ")
        print("     |  ")
        print("     |  ")
        print("-------")
    elif n == 2:
        print("  ----  ")
        print("  O  |  ")
        print("  |  |  ")
        print("     |  ")
        print("     |  ")
        print("-------")
    elif n == 3:
        print("  ----  ")
        print(" \O  |  ")
        print("  |  |  ")
        print("     |  ")
        print("     |  ")
        print("-------")
    elif n == 4:
        print("  ----  ")
        print(" \O/ |  ")
        print("  |  |  ")
        print("     |  ")
        print("     |  ")
        print("-------")
    elif n == 5:
        print("  ----  ")
        print(" \O/ |  ")
        print("  |  |  ")
        print(" /   |  ")
        print("     |  ")
        print("-------")
    elif n == 6:
        print("  ----  ")
        print(" \O/ |  ")
        print("  |  |  ")
        print(" / \ |  ")
        print("     |  ")
        print("-------")



# here is the main program
if __name__ == "__main__":
    print()
    keyword = input("Gimme a key word and don't show the other player: ")  # returns a string
    # keyWord = getpass.getpass(prompt="Gimme a key word and dont show the other player: ")
    keyword = keyword.strip()
    keyword = keyword.upper()
    for i in range(40):
        print("")

    # create a list with _ the same length as the word
    for i in range(len(keyword)):
        if keyword[i] == ' ':
            solved.append(' ')
        else:
            solved.append('_')

    gameOver = False
    wrongGuesses = 0

    while not gameOver:
        print("Solved: ", end='')
        print(solved)
        letter = input("Gimme a letter: ")  # returns a string
        letter = letter.strip().upper()


        #idiot proofing
        if len(letter) != 1 or not letter.isalpha():
            print("  I said gimme a letter not a word...")
        else:
            letterGuesses.append(letter)
            #print("Length of keyword is: " + str(len(keyWord)))

            goodGuess = False
            for i in range(len(keyword)):
                if keyword[i] == letter:
                    solved[i] = letter
                    if not goodGuess:
                        print("Good guess!")
                    goodGuess = True


            if not goodGuess:
                print("BAD guess!")
                wrongGuesses += 1

            drawHangman(wrongGuesses)

            print("Your Guesses are: ", end='')
            print( letterGuesses)

            if wrongGuesses == 6:
                print("you died!")
                print("The word was: " + keyword)
                gameOver = True
            #did we win?
            elif keyword == ''.join(solved):
                print("you win!")
                print("The word was: " + keyword)
                gameOver = True

