import random as rn
import time as tm


def printXOX(i):
    print("\n", i[0], "|", i[1], "|", i[2], "\n-----------\n", i[3], "|", i[4], "|", i[5], "\n-----------\n", i[6], "|",
          i[7], "|", i[8])


def get(i, st):
    print("\n", st, "'s turn...\n")
    global position
    while True:
        try:
            position = int(input("Enter position : "))
        except ValueError:
            pass

        if (position not in che) or (position in rep):
            temp = [x for x in avl if x not in rep]
            print("***Invalid input***\nChoose from these ", temp, '\n')
        else:
            break

    rep.append(position)
    if position == -1:
        print("***", st, " surrenders***")
        exit()
    xox[position - 1] = st
    printXOX(xox)
    if (i[0] == i[1] == i[2] == st) or (i[3] == i[4] == i[5] == st) or \
            (i[6] == i[7] == i[8] == st) or (i[0] == i[3] == i[6] == st) or \
            (i[1] == i[4] == i[7] == st) or (i[2] == i[5] == i[8] == st) or \
            (i[0] == i[4] == i[8] == st) or (i[2] == i[4] == i[6] == st):
        print("\n***", st, " WON***")
        exit()


def easy_move(i, st1):
    tm.sleep(1.2)
    s = set(rep)

    pc_move = [x for x in pos if x not in s]
    move = rn.choice(pc_move)
    rep.append(move)
    xox[move - 1] = st1
    printXOX(xox)
    if (i[0] == i[1] == i[2] == st1) or (i[3] == i[4] == i[5] == st1) or \
            (i[6] == i[7] == i[8] == st1) or (i[0] == i[3] == i[6] == st1) or \
            (i[1] == i[4] == i[7] == st1) or (i[2] == i[5] == i[8] == st1) or \
            (i[0] == i[4] == i[8] == st1) or (i[2] == i[4] == i[6] == st1):
        print("\n***PC WON***")
        exit()


def hard_move(i, st):
    tm.sleep(1.2)

    s = set(rep)
    pc_move = [x for x in pos if x not in s]
    move = 99

    if(5 in pc_move) and ((i[1] == i[7] == st) or (i[3] == i[5] == st) or (i[0] == i[8] == st) or (i[2] == i[6] == st)):
        move = 5

    elif (1 in pc_move) and ((i[1] == i[2] == st) or (i[3] == i[6] == st) or (i[4] == i[8] == st)):
        move = 1

    elif (3 in pc_move) and ((i[0] == i[1] == st) or (i[5] == i[8] == st) or (i[4] == i[6] == st)):
        move = 3

    elif (7 in pc_move) and ((i[0] == i[3] == st) or (i[7] == i[8] == st) or (i[4] == i[2] == st)):
        move = 7

    elif (9 in pc_move) and ((i[2] == i[5] == st) or (i[0] == i[4] == st) or (i[6] == i[7] == st)):

        move = 9
    elif (2 in pc_move) and ((i[0] == i[2] == st) or (i[4] == i[7] == st)):
        move = 2

    elif (4 in pc_move) and ((i[0] == i[6] == st) or (i[4] == i[5] == st)):
        move = 4

    elif (6 in pc_move) and ((i[2] == i[8] == st) or (i[3] == i[4] == st)):
        move = 6

    elif (8 in pc_move) and ((i[1] == i[4] == st) or (i[6] == i[8] == st)):
        move = 8

    if move == 99:

        if (5 in pc_move) and ((i[1] == i[7] != (' ' or st)) or (i[3] == i[5] != (' ' or st)) or
                               (i[0] == i[8] != (' ' or st)) or (i[2] == i[6] != (' ' or st))):
            move = 5

        elif (1 in pc_move) and ((i[1] == i[2] != (' ' or st)) or (i[3] == i[6] != (' ' or st)) or (i[4] == i[8] !=
                                                                                                    (' ' or st))):
            move = 1

        elif (3 in pc_move) and ((i[0] == i[1] != (' ' or st)) or (i[5] == i[8] != (' ' or st)) or (i[4] == i[6] !=

                                                                                                    (' ' or st))):
            move = 3

        elif (7 in pc_move) and ((i[0] == i[3] != (' ' or st)) or (i[7] == i[8] != (' ' or st)) or (i[4] == i[2] !=
                                                                                                    (' ' or st))):
            move = 7

        elif (9 in pc_move) and ((i[2] == i[5] != (' ' or st)) or (i[0] == i[4] != (' ' or st)) or (i[6] == i[7] !=
                                                                                                    (' ' or st))):
            move = 9

        elif (2 in pc_move) and ((i[0] == i[2] != (' ' or st)) or (i[4] == i[7] != (' ' or st))):
            move = 2

        elif (4 in pc_move) and ((i[0] == i[6] != (' ' or st)) or (i[4] == i[5] != (' ' or st))):
            move = 4

        elif (6 in pc_move) and ((i[2] == i[8] != (' ' or st)) or (i[3] == i[4] != (' ' or st))):
            move = 6

        elif (8 in pc_move) and ((i[1] == i[4] != (' ' or st)) or (i[6] == i[8] != (' ' or st))):
            move = 8

        else:
            move = rn.choice(pc_move)
            xox[move - 1] = st

    print("Position : ", move)
    rep.append(move)
    xox[move-1] = st
    printXOX(xox)
    if (i[0] == i[1] == i[2] == st) or (i[3] == i[4] == i[5] == st) or \
            (i[6] == i[7] == i[8] == st) or (i[0] == i[3] == i[6] == st) or \
            (i[1] == i[4] == i[7] == st) or (i[2] == i[5] == i[8] == st) or \
            (i[0] == i[4] == i[8] == st) or (i[2] == i[4] == i[6] == st):
        print("\n***PC WON***")
        exit()


def spl_move(i, st2):
    tm.sleep(1.2)

    cho1 = [3, 7, 9]
    cho2 = [1, 7, 9]
    cho3 = [1, 3, 9]
    cho4 = [1, 7, 9]
    cho11 = [4, 6, 8]
    cho22 = [2, 6, 8]
    cho33 = [2, 4, 8]
    cho44 = [2, 4, 6]

    if i[0] != ' ':
        move = rn.choice(cho1)

    elif i[2] != ' ':
        move = rn.choice(cho2)

    elif i[6] != ' ':
        move = rn.choice(cho3)

    elif i[8] != ' ':
        move = rn.choice(cho4)

    elif i[1] != ' ':
        move = rn.choice(cho11)

    elif i[3] != ' ':
        move = rn.choice(cho22)

    elif i[5] != ' ':
        move = rn.choice(cho33)

    elif i[7] != ' ':
        move = rn.choice(cho44)

    else:
        s = set(rep)
        pc_move = [x for x in pos if x not in s]
        move = rn.choice(pc_move)

    print("Position : ", move)
    rep.append(move)
    xox[move-1] = st2
    printXOX(xox)


xox = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
che = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
avl = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rep = [0]

sm = str(input("SINGLE PLAYER OR MULTI PLAYER (S OR M) : "))
while True:
    if sm in ("S", "M", "s", "m"):
        break
    else:
        print('***ENTER PROPER INPUT***')
        sm = str(input("SINGLE PLAYER OR MULTI PLAYER (S OR M) : "))

# SINGLE
if sm.lower() == "s":
    mode = str(input("EASY MODE OR HARD MODE (E OR H) : "))
    while True:
        if mode in ("E", "H", "e", "h"):
            break
        else:
            print('***ENTER PROPER INPUT***')
            mode = str(input("EASY MODE OR HARD MODE (E OR H) : "))
    # EASY
    if mode.lower() == "e":
        print("Let's play XOX\nThis is the position...")
        printXOX(pos)
        print("\nand -1 for surrender...\nSo Choose your side...")
        start = str(input("X or O : "))
        while True:
            if start in ("X", "O", "x", "o"):
                break
            else:
                print('***ENTER PROPER INPUT***')
                start = str(input("X or O : "))
        if start.lower() == "x":
            for count in range(4):
                get(xox, "X")
                print("\nPC'S TURN...")
                easy_move(xox, "O")
            get(xox, "X")
            print("CONGRATS ITS A DRAW")
        elif start.lower() == "o":
            for count in range(4):
                get(xox, "O")
                print("\nPC'S TURN...")
                easy_move(xox, "X")
            get(xox, "O")
            print("CONGRATS ITS A DRAW")
    # HARD
    elif mode.lower() == "h":
        print("Let's play XOX\nThis is the position...")
        printXOX(pos)
        print("\nand -1 for surrender...\nSo choose your side...")
        start = str(input("X or O : "))
        while True:
            if start in ("X", "O", "x", "o"):
                break
            else:
                print('***ENTER PROPER INPUT***')
                start = str(input("X or O : "))
        if start.lower() == "x":
            get(xox, "X")
            print("\nPC'S TURN...")
            spl_move(xox, "O")
            # easy_move(xox, "O")
            for count in range(3):
                get(xox, "X")
                print("\nPC'S TURN...")
                hard_move(xox, "O")
            get(xox, "X")
            print("CONGRATS ITS A DRAW")
        elif start.lower() == "o":
            get(xox, "O")
            print("\nPC'S TURN...")
            spl_move(xox, "X")
            # easy_move(xox, "X")
            for count in range(3):
                get(xox, "O")
                print("\nPC'S TURN...")
                hard_move(xox, "X")
            get(xox, "O")
            print("CONGRATS ITS A DRAW")
# MULTI
elif sm.lower() == "m":
    print("Let's play XOX\nThis is the position...")
    printXOX(pos)
    print("\nand -1 for surrender...\nShall we start! who's gonna play first...")
    start = str(input("X or O : "))
    while True:
        if start in ("X", "O", "x", "o"):
            break
        else:
            print('***ENTER PROPER INPUT***')
            start = str(input("X or O : "))
    if start.lower() == "x":
        for count in range(4):
            get(xox, "X")
            get(xox, "O")
        get(xox, "X")
        print("CONGRATS GUYS ITS A DRAW")
    elif start.lower() == "o":
        for count in range(4):
            get(xox, "O")
            get(xox, "X")
        get(xox, "O")
        print("CONGRATS GUYS ITS A DRAW")

