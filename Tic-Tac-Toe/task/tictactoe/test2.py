### print " ", X or O in given position

def board(step=0, col=1, row=1):
    matrix = [[" " for columns in range(3)]
              for rows in range(3)]

    if step > 0:
        if step % 2:
            what = "X"
        else:
            what = "O"
    else:
        what = " "

    cord_col = (col) - 1
    cord_row = 3 - (row)
    matrix[cord_row][cord_col] = str(what)

    return matrix

### print all board

def show(matrix):

    print("---------")
    print("|", " ".join(matrix[0]), "|")
    print("|", " ".join(matrix[1]), "|")
    print("|", " ".join(matrix[2]), "|")
    print("---------")


### create 
# main


print(show(board()))
step = 1
all_moves = []

while step < 5:
    cordinates = input("Enter the coordinates:")
    if len(cordinates) == 3:
        if cordinates[0].isnumeric() and cordinates[2].isnumeric():
            if (0 < int(cordinates[0]) <= 3 and (0 < int(cordinates[2]) <= 3)):

                #moves[int(cordinates[0])].append(int((cordinates[2])))
                move = board(step, int(cordinates[0]), int(cordinates[2]))
                all_moves.append(move)

                print(board(step, int(cordinates[0]), int(cordinates[2])))

            else:
                print("Coordinates should be from 11 to 3!")
                continue
        else:
            print("You should enter numbers!")
            continue
    else:
        print("Input proper coordinates")
        continue

