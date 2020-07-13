# write your code here

import math

count_X = 0
count_O = 0
previous = ""
consecutive = 0
consecutive_X = 0
consecutive_O = 0
win_X = 0
win_O = 0
impossible = 0

pole_input = input("Enter cells:")
pole = list(pole_input)
print("---------")
print("|", pole[0], pole[1], pole[2], "|")
print("|", pole[3], pole[4], pole[5], "|")
print("|", pole[6], pole[7], pole[8], "|")
print("---------")

cordinates = input("Enter the coordinates:")

if cordinates[0].isnumeric() and cordinates[0].isnumeric():
    if 0 < int(cordinates[0]) < 4 and (0 < int(cordinates[2]) < 4):
        if cordinates == "1 1":
            if pole[6] == "_":
                pole[6] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "2 1":
            if pole[7] == "_":
                pole[7] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "3 1":
            if pole[8] == "_":
                pole[8] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "1 2":
            if pole[3] == "_":
                pole[3] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == " 2 2":
            if pole[4] == "_":
                pole[4] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "3 2":
            if pole[5] == "_":
                pole[5] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "1 3":
            if pole[0] == "_":
                pole[0] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "2 3":
            if pole[1] == "_":
                pole[1] = "X"
            else:
                print("This cell is occupied! Choose another one!")
        elif cordinates == "3 3":
            if pole[2] == "_":
                pole[2] = "X"
            else:
                print("This cell is occupied! Choose another one!")

        print("---------")
        print("|", pole[0], pole[1], pole[2], "|")
        print("|", pole[3], pole[4], pole[5], "|")
        print("|", pole[6], pole[7], pole[8], "|")
        print("---------")

    else:
        print("Coordinates should be from 1 to 3!")
else:
    print("You should enter numbers!")





for item in pole:
    if item == "X":
        count_X += 1
    elif item == "O":
        count_O += 1

    if previous == item:
        consecutive += 1
        if consecutive == 3:
            if item == "X":
                consecutive_X += 1
            else:
                consecutive_O += 1
    else:
        consecutive = 0

# poziomo

if (pole[0] == pole[1] == pole[2] == "X" or
        pole[3] == pole[4] == pole[5] == "X" or
        pole[6] == pole[7] == pole[8] == "X"):
    win_X += 1

if (pole[0] == pole[1] == pole[2] == "O" or
        pole[3] == pole[4] == pole[5] == "O" or
        pole[6] == pole[7] == pole[8]) == "O":
    win_O += 1


# pionowo
if (pole[0] == pole[3] == pole[6] == "X" or
        pole[1] == pole[4] == pole[7] == "X" or
        pole[2] == pole[5] == pole[8] == "X"):
    win_X += 1

if (pole[0] == pole[3] == pole[6] == "O" or
        pole[1] == pole[4] == pole[7] == "O" or
        pole[2] == pole[5] == pole[8] == "O"):
    win_O += 1

# krzyz

if (pole[0] == pole[4] == pole[8] or
        pole[2] == pole[4] == pole[6]):
    if (pole[4] == "X"):
        win_X += 1
    elif (pole[4] == "Y"):
        win_O += 1

# conditions for impossible

if win_O == win_X and win_O > 0:
    print("Impossible")
    impossible += 1

if math.fabs(count_X - count_O) >= 2:
    print("Impossible")
    impossible += 1

if consecutive_O == consecutive_X and consecutive_O > 0:
    print("Impossible")

if win_X == 0 == win_O and "_" not in pole:
    print("Draw")
elif win_X == win_X == 0 and "_" in pole and impossible == 0:
    print("Game not finished")


else:
    if win_O >0 and impossible == 0:
        print("O wins")
    elif win_X>0 and impossible == 0:
        print("X wins")

#print(win_O)
#print(win_X)