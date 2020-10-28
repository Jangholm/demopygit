from Game import Game
import os

player_position_x_axis = 0
player_position_y_axis = 0
map_x_axis_size = 0
map_y_axis_size = 0
map_list = []
game_is_on = True
map_elements_list = ["D", "Z", "S", "W", "_", "_", "_", "_", "_", "_", "_"]

while True:
    print("\n_______WELCOME TO DEATH ROW_______\n")
    print("1.    Play Game\n5.      Exit")
    user_answer = input("Choose an alternitive: ")
    if user_answer == "1":
        game = Game()
        map_list, map_x_axis_size, map_y_axis_size = game.create_map(map_list, map_x_axis_size, map_y_axis_size,
                                                                     map_elements_list)
        game.place_player(map_list,player_position_x_axis, player_position_y_axis)
        game.print_out_map(map_list)
        game.test_reset_map(map_list, player_position_x_axis, player_position_y_axis)
        while game_is_on:
            player_position_x_axis, player_position_y_axis = game.ask_to_move_player(player_position_x_axis,
                                                                                     player_position_y_axis,
                                                                                     map_x_axis_size,
                                                                                     map_y_axis_size)
            game.place_player(map_list, player_position_x_axis, player_position_y_axis)
            os.system('cls')
            game.print_out_map(map_list)
            print(player_position_x_axis)
            game.test_reset_map(map_list, player_position_x_axis, player_position_y_axis)
    elif user_answer == "5":
        break
    else:
        print("kiss")