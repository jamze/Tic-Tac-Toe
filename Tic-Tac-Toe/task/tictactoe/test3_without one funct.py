### print " ", X or O in given position

#matrix = [[" " for columns in range(3)]
#          for rows in range(3)]

all_moves = [[" " for columns in range(3)]
          for rows in range(3)]


def show(matrix):

    print("---------")
    print("|", " ".join(matrix[0]), "|")
    print("|", " ".join(matrix[1]), "|")
    print("|", " ".join(matrix[2]), "|")
    print("---------")


#### main

print(show(all_moves))
step = 1
win_X = 0
win_O = 0

while step < 10:
    cordinates = input("Enter the coordinates:")
    if len(cordinates) == 3:
        if cordinates[0].isnumeric() and cordinates[2].isnumeric():
            if 0 < int(cordinates[0]) <= 3 and (0 < int(cordinates[2]) <= 3):
                if step > 0:
                    if step % 2:
                        what = "X"
                    else:
                        what = "O"
                else:
                    what = " "
                #print("what:", what)

                #cord_col = int(cordinates[0]) - 1
                #cord_row = 3 - int(cordinates[2])
                #all_moves[cord_row][cord_col] = str(what)

                cord_col = int(cordinates[0])-1
                cord_row = 3 - (int(cordinates[2]))

                if all_moves[cord_row][cord_col] == " ":
                    all_moves[cord_row][cord_col] = what
                    #print("previous: ", all_moves)
                    #all_moves[1 - 1][3 - 1] = "1,3"
                    show(all_moves)
                    step += 1
                else:
                    print("Its already taken!")
                    continue

            else:
                print("Coordinates should be from 1 to 3!")
                continue
        else:
            print("You should enter numbers!")
            continue
    else:
        print("Input proper coordinates")
        continue

    #print("1", all_moves[3-1][1-1], "2", all_moves[2-1][1-1], "3", all_moves[1-1][1-1])


    # pionowo
    if (all_moves[3-1][1-1] == all_moves[2-1][1-1] == all_moves[1-1][1-1] == "X" or
            all_moves[3-1][2-1] == all_moves[2-1][2-1] == all_moves[1-1][2-1] == "X" or
            all_moves[3-1][3-1] == all_moves[2-1][3-1] == all_moves[1-1][3-1] == "X"):
        win_X += 1

    if (all_moves[3 - 1][1 - 1] == all_moves[2 - 1][1 - 1] == all_moves[1 - 1][1 - 1] == "O" or
            all_moves[3 - 1][2 - 1] == all_moves[2 - 1][2 - 1] == all_moves[1 - 1][2 - 1] == "O" or
            all_moves[3 - 1][3 - 1] == all_moves[2 - 1][3 - 1] == all_moves[1 - 1][3 - 1] == "O"):
        win_O += 1

    # krzyz

    if (all_moves[3 - 1][1 - 1] == all_moves[2 - 1][2 - 1] == all_moves[1 - 1][3 - 1] or
            all_moves[1 - 1][1 - 1] == all_moves[2 - 1][2 - 1] == all_moves[3 - 1][3 - 1]):
        if (all_moves[2 - 1][2 - 1] == "X"):
            win_X += 1
        elif (all_moves[2 - 1][2 - 1] == "O"):
            win_O += 1

    #print("win X: ", win_X)

    if win_X or win_O > 0:
        if win_X > 0:
            print ("X wins!")
            break
        else:
            print ("O wins!")
            break

    if win_X == 0 == win_O and step == 9:
        print("Draw")
#    elif win_X == win_X == 0 and "_" in all_moves and impossible == 0:
#        print("Game not finished")



