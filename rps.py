import random as rnd

player_points = 0
comp_points = 0


def main():
    global player_points
    global comp_points
    move_list = ['rock', 'paper', 'scissors']
    while True:
        print('please pick a move')
        player = input()
        if player not in move_list:
            print('please pick a valid move')
            continue
        else:
            break

    comp = rnd.choice(move_list)
    print('computer picked ', comp)

    if move_list[move_list.index(comp)] == move_list[move_list.index(player) - 1]:
        player_points += 1
    elif move_list[move_list.index(player)] == move_list[move_list.index(comp) - 1]:
        comp_points += 1
    go_nogo = input('do we continue?')
    if go_nogo == 'y':
        main()
    else:
        print(player_points, comp_points)


main()
