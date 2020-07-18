def board(col= 1, row= 1, what= " "):

    matrix = [[" " for columns in range(3)]
              for rows in range(3)]

    cord_col = (col) - 1
    cord_row = 3 - (row)
    matrix [cord_row][cord_col] = str(what)

    print("---------")
    print("|"," ".join(matrix[0]),"|")
    print("|"," ".join(matrix[1]),"|")
    print("|"," ".join(matrix[2]),"|")
    print("---------")


#main

board()
x_or_y = 1

while x_or_y<5:
    cordinates = input("Enter the coordinates:")
    if x_or_y%2:
        what = "Y"
    else:
        what = "X"
    if cordinates[0].isnumeric() and cordinates[2].isnumeric():
        if 0 < int(cordinates[0]) <= 3 and (0 < int(cordinates[2]) <= 3):
            what = "X"
            board(int(cordinates[0]), int(cordinates[2]), what)
            x_or_y +=1

        else:
            print("Coordinates should be from 1 to 3!")
            continue
    else:
        print("You should enter numbers!")
        continue



def check()

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

