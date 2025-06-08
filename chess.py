#import PIL
#from Pil import Image
#from numpy import*

class White():
    color = "w"
    class Pawn():
        piece = "p"
        name = "WP"
        #name = Image.open(whitePawn.jpg)
        cntr = 0
    class Rook():
        piece = 'r'
        name = "WR"
        cntr = 0
    class Knight():
        piece = "n"
        name = "WN"
        cntr = 0
    class Bishiop():
        piece = "b"
        name = "WB"
        cntr = 0
    class Queen():
        piece = "q"
        name = "WQ"
        cntr = 0
    class King():
        piece = 'k'
        name = "WK"
        cntr = 0

class Black():
    color = "b"
    class Pawn():
        piece = "p"
        name = "BP"
        #name = Image.open(whitePawn.jpg)
        cntr = 0
         #def movement(self):
    class Rook():
        name = "BR"
        cntr = 0
    class Knight():
        name = "BN"
        cntr = 0
    class Bishiop():
        name = "BB"
        cntr = 0
    class Queen():
        name = "BQ"
        cntr = 0
    class King():
        name = "BK"
        cntr = 0

class EmptySpace():
    name = "* "

#white pieces
wrl = White.Rook()
wnl = White.Knight()
wbl = White.Bishiop()
wq = White.Queen()
wk = White.King()
wbr = White.Bishiop()
wnr = White.Knight()
wrr = White.Rook()
wp1 = White.Pawn()
wp2 = White.Pawn()
wp3 = White.Pawn()
wp4 = White.Pawn()
wp5 = White.Pawn()
wp6 = White.Pawn()
wp7 = White.Pawn()
wp8 = White.Pawn()

#black pieces
brl = Black.Rook()
bnl = Black.Knight()
bbl = Black.Bishiop()
bq = Black.Queen()
bk = Black.King()
bbr = Black.Bishiop()
bnr = Black.Knight()
brr = Black.Rook()
bp1 = Black.Pawn()
bp2 = Black.Pawn()
bp3 = Black.Pawn()
bp4 = Black.Pawn()
bp5 = Black.Pawn()
bp6 = Black.Pawn()
bp7 = Black.Pawn()
bp8 = Black.Pawn()
#empty space
e = EmptySpace()
#makes the board
board = [[brl, bnl, bbl, bq, bk, bbl, bnl, brl], [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8], [e, e, e, e, e, e, e, e], [e, e, e, e, e, e, e, e], [e, e, e, e, e, e, e, e], [e, e, e, e, e, e, e, e], [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8], [wrl, wnl, wbl, wq, wk, wbr, wnr, wrr]]
#prints the board
for i in range(8):
    print(8-i, end=' ')
    for j in range(8):
        print(board[i][j].name, end=' ')
    print()
print(" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ")
checkmate = False
#starts the game
while not checkmate:
    # enter move
    illegal = False
    move = str(input("Move: "))
    move = move.lower()
    move2 = []
    for i in range(4):
        move2.append(move[i])
    move = ""
    for i in range(4):
        if move2[i] == "8":
            move2[i] = 0
        if move2[i] == "7":
            move2[i] = 1
        if move2[i] == "6":
            move2[i] = 2
        if move2[i] == "5":
            move2[i] = 3
        if move2[i] == "4":
            move2[i] = 4
        if move2[i] == "3":
            move2[i] = 5
        if move2[i] == "2":
            move2[i] = 6
        if move2[i] == "1":
            move2[i] = 7
    for i in range(4):
        if move2[i] == "a":
            move2[i] = 0
        if move2[i] == "b":
            move2[i] = 1
        if move2[i] == "c":
            move2[i] = 2
        if move2[i] == "d":
            move2[i] = 3
        if move2[i] == "e":
            move2[i] = 4
        if move2[i] == "f":
            move2[i] = 5
        if move2[i] == "g":
            move2[i] = 6
        if move2[i] == "h":
            move2[i] = 7
    for i in range(4):
        move += str(move2[i])
    #moves piece

    #rook movement
    if board[int(move[1])][int(move[0])].name[1] == "R":
        if int(move[1]) == int(move[3]) and int(move[0]) == int(move[2]) or int(move[1]) != int(move[3]) and int(move[0]) != int(move[2]):
            print("illegal move")
            illegal = True

    #bishop movement
    if board[int(move[1])][int(move[0])].name[1] == "B":
        if abs(int(move[1]) - int(move[3])) !=  abs(int(move[0]) - int(move[2])):
            print("illegal move")
            illegal = True

    #queen movement
    if board[int(move[1])][int(move[0])].name[1] == "Q":
        if (abs(int(move[1]) - int(move[3])) != abs(int(move[0]) - int(move[2]))) and (int(move[1]) == int(move[3]) and int(move[0]) == int(move[2]) or int(move[1]) != int(move[3]) and int(move[0]) != int(move[2])):
            print("illegal move")
            illegal = True

    #pawn movement
    if board[int(move[1])][int(move[0])].name[1] == "P":
        #white pawn moves
        if board[int(move[1])][int(move[0])].name[0] == "W":
            if int(move[0]) != int(move[2]):
                if abs(int(move[1]) - int(move[3])) != abs(int(move[0]) - int(move[2])) or abs(int(move[1]) - int(move[3])) != 1 or abs(int(move[0]) - int(move[2])) != 1 or board[int(move[3])][int(move[2])].name[0] != "B" or int(move[1]) - int(move[3]) < 0:
                    print("illegal move")
                    illegal = True
            else:
                if int(move[0]) != int(move[2]):
                    print("illegal move")
                    illegal = True
                if int(move[1]) - int(move[3]) < 0:
                    print("illegal move")
                    illegal = True
                if board[int(move[1])][int(move[0])].cntr == 0 and abs(int(move[1]) - int(move[3])) > 2:
                    print("illegal move")
                    illegal = True
                if board[int(move[1])][int(move[0])].cntr != 0 and abs(int(move[1]) - int(move[3])) > 1:
                    print("illegal move")
                    illegal = True
        #black pawn moves
        elif board[int(move[1])][int(move[0])].name[0] == "B":
            if int(move[0]) != int(move[2]):
                if abs(int(move[1]) - int(move[3])) != abs(int(move[0]) - int(move[2])) or abs(int(move[1]) - int(move[3])) != 1 or abs(int(move[0]) - int(move[2])) != 1 or board[int(move[3])][int(move[2])].name[0] != "W" or int(move[1]) - int(move[3]) > 0:
                    print("illegal move")
                    illegal = True
            if int(move[0]) != int(move[2]):
                print("illegal move")
                illegal = True
            if int(move[1]) - int(move[3]) > 0:
                print("illegal move")
                illegal = True
            if board[int(move[1])][int(move[0])].cntr == 0 and abs(int(move[1]) - int(move[3])) > 2:
                print("illegal move")
                illegal = True
            if board[int(move[1])][int(move[0])].cntr != 0 and abs(int(move[1]) - int(move[3])) > 1:
                print("illegal move")
                illegal = True
        #pawn moves with out taking
        #else:
            #if int(move[0]) != int(move[2]):
                #print("illegal move")
                #illegal = True
            #if board[int(move[1])][int(move[0])].name[0] == "W":
                #if int(move[1]) - int(move[3]) < 0:
                    #print("illegal move")
                    #illegal = True
            #if board[int(move[1])][int(move[0])].name[0] == "B":
                #if int(move[1]) - int(move[3]) > 0:
                    #print("illegal move")
                    #illegal = True
            #if board[int(move[1])][int(move[0])].cntr == 0 and abs(int(move[1]) - int(move[3])) > 2:
                #print("illegal move")
                #illegal = True
            #if board[int(move[1])][int(move[0])].cntr != 0 and abs(int(move[1]) - int(move[3])) > 1:
                #print("illegal move")
                #illegal = True

    #knight movement
    if board[int(move[1])][int(move[0])].name[1] == "N":
        if not (abs(int(move[0]) - int(move[2])) == 2) and (abs(int(move[1]) - int(move[3])) == 1):
            if not (abs(int(move[0]) - int(move[2])) == 1) and (abs(int(move[1] - int(move[3])) == 2)):
                print("illegal move")
                illegal = True
    if not illegal:
        # checks for open space
        if board[int(move[3])][int(move[2])] == e:
            board[int(move[3])][int(move[2])] = board[int(move[1])][int(move[0])]
            board[int(move[1])][int(move[0])] = e
        #checks for same color
        elif board[int(move[3])][int(move[2])].name[0] == board[int(move[1])][int(move[0])].name[0]:
            print("illegal move")
        #checks for opposite color
        elif board[int(move[3])][int(move[2])].name[0] != board[int(move[1])][int(move[0])].name[0]:
            board[int(move[3])][int(move[2])] = board[int(move[1])][int(move[0])]
            board[int(move[1])][int(move[0])] = e
        #adds to cntr
        board[int(move[3])][int(move[2])].cntr += 1
    #prints the board
    for i in range(8):
        print(8 - i, end=' ')
        for j in range(8):
            print(board[i][j].name, end=' ')
        print()
    print(" ", "A ", "B ", "C ", "D ", "E ", "F ", "G ", "H ")
    print(wp4.cntr)
    #checkmate = True