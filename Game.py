from os import system, name
import random

class Game:
    def create_map(self, list, x_axis, y_axis, map_elements_list):
        map_valid = False
        while not map_valid:
            print("Time to set the map size\n")
            x = int(input("Choose a number between 1-20 (x-axis): "))
            y = int(input("Choose a number between 1-20 (y-axis): "))
            print()
            if x <= 20 and y <= 20:
                for i in range(x):
                    small_list = []
                    for z in range(y):
                        small_list.append(random.choice(map_elements_list))
                    list.append(small_list)
                    x_axis = x
                    y_axis = y
                map_valid = True
            else:
                print("Map too big!")
        x_axis -= 1
        y_axis -= 1
        return list, x_axis, y_axis

    def place_player(self, list, x_axis, y_axis):
        x_counter = 0
        y_counter = 0
        for section in list:
            if y_counter == y_axis:
                for element in section:
                    if x_counter == x_axis:
                        section[x_axis] = "X"
                        break
                    elif x_counter < x_axis:
                         x_counter += 1
                    else:
                        x_counter += 1
                        continue
            elif y_counter < y_axis:
                y_counter += 1
                continue
            else:
                y_counter -= 1
            break
        return list

    def print_out_map(self, list):
        for y in list:
            print(y)

    def check_if_player_is_out_of_map(self, user_x_axis, user_y_axis, map_x_axis, map_y_axis):
        if user_x_axis > map_x_axis or user_x_axis < 0:
            return True
        if user_y_axis > map_y_axis or user_y_axis < 0:
            return True

    def player_out_of_map(self, answer, x_axis, y_axis, map_x_axis, map_y_axis):
        if answer == "d":
            x_axis += 1
            if x_axis > map_x_axis:
                return True
        elif answer == "a":
            x_axis -= 1
            if x_axis < 0:
                return True
        elif answer == "w":
            y_axis -= 1
            if y_axis < 0:
                return True
        elif answer == "s":
            y_axis += 1
            if y_axis > map_y_axis:
                return True
        else:
            return False

    def reset_axis(self, answer, ):
        pass

    def ask_to_move_player(self, x_axis, y_axis, map_x_axis, map_y_axis):
        valid_answer = False
        answer = ""
        while not valid_answer:
            answer = input("Move player: ")
            if self.player_out_of_map(answer, x_axis, y_axis, map_x_axis, map_y_axis):
                print("You can't go out of the!")
            else:
                valid_answer = True
        if answer == "d":
            x_axis += 1
        elif answer == "a":
            x_axis -= 1
        elif answer == "w":
            y_axis -= 1
        elif answer == "s":
            y_axis += 1
        return x_axis, y_axis

    def reset_map(self, list, x_axis, y_axis):
        x_axis -= 1
        for section in list:
            for element in range(len(section)):
                section[x_axis] = "_"

    def test_reset_map(self, list, x_axis, y_axis):
        for section in list:
            for index, item in enumerate(section):
                if item == "X":
                    section[index] = "_"

    def clear_screen(self):
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def bajs(self):
        pass