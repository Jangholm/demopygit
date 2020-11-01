from Game import Game
import os
from Enemy import Enemy, Witch, Dragon
from Fight import Fight
from Player import Player

player_position_x_axis = 0
player_position_y_axis = 0
map_x_axis_size = 0
map_y_axis_size = 0
map_list = []
game_is_on = True
map_elements_list = ["O", "_", "_"]
fight_is_on = True

while True:
    print("\n_______WELCOME TO DEATH ROW_______\n")
    print("1.    Play Game\n5.      Exit")
    user_answer = input("Choose an alternitive: ")
    if user_answer == "1":
        game = Game()
        map_list, map_x_axis_size, map_y_axis_size = game.create_map(map_list, map_x_axis_size, map_y_axis_size,
                                                                     map_elements_list)
        player = Player()
        print(player.health)
        player.create_player()
        game.place_player(map_list, player_position_x_axis, player_position_y_axis)
        game.print_out_map(map_list)
        game.reset_map(map_list, player_position_x_axis, player_position_y_axis)
        while game_is_on:
            player_position_x_axis, player_position_y_axis = game.ask_to_move_player(player_position_x_axis,
                                                                                     player_position_y_axis,
                                                                                     map_x_axis_size,
                                                                                     map_y_axis_size)
            if game.check_for_enemy(map_list, player_position_x_axis, player_position_y_axis):
                fight = Fight()
                enemy = fight.create_enemies()
                while fight_is_on:
                    if fight.action_player(enemy, player):
                        if fight.check_for_win(enemy):
                            break
                        fight.action_enemy(enemy, player)
                        if fight.check_for_loss(player):
                            game_is_on = False
                            break
                    else:
                        break
            game.place_player(map_list, player_position_x_axis, player_position_y_axis)
            os.system('cls')
            game.print_out_map(map_list)
            game.reset_map(map_list, player_position_x_axis, player_position_y_axis)
    elif user_answer == "5":
        print("bajs")
        break
