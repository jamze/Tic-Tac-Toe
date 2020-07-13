# write your code here

import math
def print_function(pole):
    print("---------")
    print("|", pole[0], pole[1], pole[2], "|")
    print("|", pole[3], pole[4], pole[5], "|")
    print("|", pole[6], pole[7], pole[8], "|")
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

pole_input = input("Enter cells:")
pole = list(pole_input)
print(print_function(pole))

#cordinates = input("Enter the coordinates:")
while True:
    cordinates = input("Enter the coordinates:")
    if cordinates[0].isnumeric() and cordinates[0].isnumeric():
        if 0 < int(cordinates[0]) < 4 and (0 < int(cordinates[2]) < 4):
            if cordinates == "1 1":
                if pole[6] == "_":
                    pole[6] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "2 1":
                if pole[7] == "_":
                    pole[7] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "3 1":
                if pole[8] == "_":
                    pole[8] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "1 2":
                if pole[3] == "_":
                    pole[3] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "2 2":
                if pole[4] == "_":
                    pole[4] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "3 2":
                if pole[5] == "_":
                    pole[5] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "1 3":
                if pole[0] == "_":
                    pole[0] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "2 3":
                if pole[1] == "_":
                    pole[1] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
            elif cordinates == "3 3":
                if pole[2] == "_":
                    pole[2] = "X"
                    print(print_function(pole))
                    break
                else:
                    print("This cell is occupied! Choose another one!")
                    continue
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")





