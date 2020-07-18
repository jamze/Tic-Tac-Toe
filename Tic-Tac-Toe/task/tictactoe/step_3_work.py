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

all_moves = input("Enter cells:")

print("---------")
print("|", all_moves[0], all_moves[1], all_moves[2], "|")
print("|", all_moves[3], all_moves[4], all_moves[5], "|")
print("|", all_moves[6], all_moves[7], all_moves[8], "|")
print("---------")

for char in all_moves:
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

if (all_moves[0] == all_moves[1] == all_moves[2] == "X" or
        all_moves[3] == all_moves[4] == all_moves[5] == "X" or
        all_moves[6] == all_moves[7] == all_moves[8] == "X"):
    win_X += 1

if (all_moves[0] == all_moves[1] == all_moves[2] == "O" or
        all_moves[3] == all_moves[4] == all_moves[5] == "O" or
        all_moves[6] == all_moves[7] == all_moves[8]) == "O":
    win_O += 1


# pionowo
if (all_moves[0] == all_moves[3] == all_moves[6] == "X" or
        all_moves[1] == all_moves[4] == all_moves[7] == "X" or
        all_moves[2] == all_moves[5] == all_moves[8] == "X"):
    win_X += 1

if (all_moves[0] == all_moves[3] == all_moves[6] == "O" or
        all_moves[1] == all_moves[4] == all_moves[7] == "O" or
        all_moves[2] == all_moves[5] == all_moves[8] == "O"):
    win_O += 1

# krzyz

if (all_moves[0] == all_moves[4] == all_moves[8] or
        all_moves[2] == all_moves[4] == all_moves[6]):
    if (all_moves[4] == "X"):
        win_X += 1
    elif (all_moves[4] == "Y"):
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

if win_X == 0 == win_O and "_" not in all_moves:
    print("Draw")
elif win_X == win_X == 0 and "_" in all_moves and impossible == 0:
    print("Game not finished")


else:
    if win_O >0 and impossible == 0:
        print("O wins")
    elif win_X>0 and impossible == 0:
        print("X wins")

#print(win_O)
#print(win_X)