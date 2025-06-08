


#main lists

Keyword = []
Solved = []
Guesses = []

def drawSnowman(n):
    if n == 0:
        #ascii print draw of snaowman in state 0
        print("    ")


    pass

#begin your code here

str = input("gimme a word")
for c in str:
    Keyword.append(c)
    Solved.append('_')

#while ask user for a letter

print(Keyword)
print(Solved)

Solved[1]='a'
print(Solved)


for index in enumerate(Keyword):
    print(index)
    print(Keyword[index[0]])
    Solved[index[0]] = 'q'

print(Solved)




