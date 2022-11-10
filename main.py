valid_answer = False

while not valid_answer:
    total_spaces = input("How many playable spaces do you want? ")
    try:
        total_spaces = int(total_spaces)
    except:
        print("Please input a number greater than 2.")
        continue
    if total_spaces < 3:
        print("Please input a number greater than 2.")
        continue
    valid_answer = True

spaces_key = [None]*total_spaces
spaces_value = "_"
win = False
win_player = None
current_player = 1
valid_move = True

for i in range(total_spaces):
    spaces_key[i] = i+1

board = dict.fromkeys(spaces_key, spaces_value)

while win != True:
    valid_move = True
    print()
    print(f"Player {current_player}")
    print(" ".join(board.values()))

    chosen_space = input("Choose a space ")
    try:
        chosen_space = int(chosen_space)
    except:
        print(f"Please choose a number between 1-{total_spaces}")
        continue
    
    if chosen_space not in range(1, total_spaces+1):
        print(f"Please choose a number between 1-{total_spaces}")
        continue

    chosen_value = input("S or O? ").upper()
    if chosen_value != "S" and chosen_value != "O":
        print("Please choose S or O.")
        continue
    
    if board[chosen_space] == "S" or board[chosen_space] == "O":
        print("That space is already taken, please choose a different space.")
        continue

    board[chosen_space] = chosen_value

    for i in range(total_spaces):
        try:
            if board[i+1] == "S" and board[i+2] == "O" and board[i+3] == "S":
                win = True
                print(" ".join(board.values()))
                print(f"Player {current_player} has won the game!")
                break
        except:
            break
    if win == True:
        continue

    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1
