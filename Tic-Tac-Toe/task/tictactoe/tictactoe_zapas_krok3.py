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

pole = input("Enter cells:")

print("---------")
print("|", pole[0], pole[1], pole[2], "|")
print("|", pole[3], pole[4], pole[5], "|")
print("|", pole[6], pole[7], pole[8], "|")
print("---------")

for char in pole:
    if char == "X":
        count_X += 1
    elif char == "O":
        count_O += 1

    if previous == char:
        consecutive += 1
        if consecutive == 3:
            if char == "X":
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