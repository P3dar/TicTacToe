#board data#
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

#variables#
winner = None
full = False
moves = []
game = True

#function that display the game field#
def display():
    for i in board:
        print("-" * 7)
        for j in i:
            print("|" + j, end = "")
        print("|")
    print("-" * 7)

#funcion for victory#
def win(player):
    global winner
    b = board
    hori = b[0][0] == b[0][1] == b[0][2] != " " or b[1][0] == b[1][1] == b[1][2] != " " or b[2][0] == b[2][1] == b[2][2] != " "
    ver = b[0][0] == b[1][0] == b[2][0] != " " or b[0][1] == b[1][1] == b[2][1] != " " or b[0][2] == b[1][2] == b[2][2] != " "
    dia = b[0][0] == b[1][1] == b[2][2] != " " or b[0][2] == b[1][1] == b[2][0] != " "

    if hori or ver or dia:
        winner = player
    
#check the board and return DRAW if board is full°
    for i in board:
        if " " in i:
            full = False
            break
        else:
            full = True

    if full and not winner:
        winner = "draw"

#the game (sorry)#
player = "x"
while game:
    move = input(f"player ({player}) (eg:12) : ")
    if move not in moves:
        moves.append(move)
    else:
        print("Alredy occupied!")
        continue
    try:
        x,y = int(move[0]), int(move[1])
    except:
        print("Enter the coordinates properly!")
        continue
    
    board[2-y][x] = f"{player}"

    display()
    win(player)
    if winner == player:
        print(f"{player} wins!")
        game = False
    elif winner == "draw":
        print("It's a tie!")
        game = False

    if player == "x":
        player = "o"
    else:
        player = "x"
    

        
        
    











    

