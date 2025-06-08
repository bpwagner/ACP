def get_word():
    print("SNOWMAN")
    print("Game stars now.")
    word = input("Give me a word: ")
    return word


def play(word):
    tries = 6
    guessed_letter = []
    print(snowman(tries))
    word_completion = "_" * len(word)
    guessed = False
    print(word_completion)
    while guessed == False and tries > 0:
        guess = \
            input("Guess a letter: ")
        if guess in guessed_letter:
            print("You have already guessed it.")
        elif guess in word:
            print("You guessed right.")
            guessed_letter.append(guess)
            index_number = word.find(guess)
            temp = ""
            for i in range(len(word_completion)):
                #if index_number == i:
                if word[i] == guess:
                    temp += guess
                else:
                    temp += word_completion[i]
            word_completion = temp

            if "_" not in word_completion:
                guessed = True
                print("You won.")

        else:
            print("It is not in the word.")
            guessed_letter.append(guess)
            tries -= 1

        print(snowman(tries))
        print(word_completion)

    if "_"  in word_completion:
        print("You lost.")



def snowman(tries):
    stages = ["""
                   _|==|_
                    ('')___/
                >--(`^^')
                  (`^'^'`)
                  `======'  
             """
        ,
              """
                    _|==|_
                     ('')
                 >--(`^^')
                   (`^'^'`)
                   `======'        
              """
        ,
              """
                    _|==|_
                     ('')
                    (`^^')
                   (`^'^'`)
                   `======'
              """
        ,
              """
 
                     ('')
                    (`^^')
                   (`^'^'`)
                   `======'
              """
        ,
              """
 
 
                    (`^^')
                   (`^'^'`)
                   `======'
              """
        ,
              """
 
 
 
                   (`^'^'`)
                   `======'
              """
        ,
              """
 
 
 
 
                   `======'
              """
              ]
    return stages[tries]


def start():
    test = get_word()
    play(test)


start()