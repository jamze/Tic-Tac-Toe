# write your code here

import math
def print_function(all_moves):
    print("---------")
    print("|", all_moves[0], all_moves[1], all_moves[2], "|")
    print("|", all_moves[3], all_moves[4], all_moves[5], "|")
    print("|", all_moves[6], all_moves[7], all_moves[8], "|")
    return("---------")

count_X = 0
count_O = 0
previous = ""
consecutive = 0
consecutive_X = 0
consecutive_O = 0
win_X = 0
win_O = 0
impossible = 0

all_moves_input = input("Enter cells:")
all_moves = list(all_moves_input)
print(print_function(all_moves))

#cordinates = input("Enter the coordinates:")
while True:
    cordinates = input("Enter the coordinates:")
    if cordinates[0].isnumeric() and cordinates[0].isnumeric():
        if 0 < int(cordinates[0]) < 4 and (0 < int(cordinates[2]) < 4):
            if cordinates == "1 1":
                if all_moves[6] == "_":
                    all_moves[6] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "2 1":
                if all_moves[7] == "_":
                    all_moves[7] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "3 1":
                if all_moves[8] == "_":
                    all_moves[8] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "1 2":
                if all_moves[3] == "_":
                    all_moves[3] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "2 2":
                if all_moves[4] == "_":
                    all_moves[4] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "3 2":
                if all_moves[5] == "_":
                    all_moves[5] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "1 3":
                if all_moves[0] == "_":
                    all_moves[0] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "2 3":
                if all_moves[1] == "_":
                    all_moves[1] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "3 3":
                if all_moves[2] == "_":
                    all_moves[2] = "X"
                    print(print_function(all_moves))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")





