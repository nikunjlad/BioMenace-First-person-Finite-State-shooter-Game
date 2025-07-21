"""
Copyright (c) 2018 Nikunj Lad

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from BioMenace import update_health_stats, update_duck_stats, update_ammo_stats, update_reload_stats, check_input, \
    introduction, level1, inventory_stats, view_game_stats, check_key_status, rules
from Room2 import Room2
from Room3 import Room3
from Room4 import Room4
from Room5 import Room5
import sys


class Room1:

    def __init__(self, duck, total_shoots, reload, medic, hp, ammo_dict, weapons_list, enemy_health, life, has_key,
                 total_moves):
        """
        :param duck:  deceptive move not necessarily required for the game. Don't use it for your moves.
        :param total_shoots: total shoots taken in each game
        :param reload: no of reloads for a particular person
        :param medic: amount of medic available for survival
        :param hp: your current health status
        :param ammo_dict: ammunition you currently hold
        :param weapons_list: the weapon you currently hold
        :param enemy_health: whats the enemy health
        :param life: no of lives left
        """
        self.duck = duck
        self.total_shoots = total_shoots
        self.reload = reload
        self.medic = medic
        self.enemy_health = enemy_health
        self.life = life
        self.has_key = has_key
        self.hp = hp
        self.ammo_dict = ammo_dict
        self.weapons_list = weapons_list
        self.total_moves = total_moves

    def enter_room_1(self):
        """
        :return: return status dictionary having status of various game properties (health, ammo, etc)
        """
        exit_status = False
        move_count = 1
        level_1 = True
        enemy_dead = False
        total_exit = False
        enemy = "Troll"

        level1()
        print("*****************************************************************\n")

        while level_1:
            print("\n1. Duck\n2. Shoot 3 shotgun rounds\n3. Reload your gun\n4. Use a Medic-kit\n5. Pick up Room 2 Key\n6. Exit game")

            try:
                user_choice = check_input()

                if user_choice != 6:
                    if not enemy_dead:
                        if move_count % 2 != 0:
                            if user_choice != 4:
                                self.hp -= 25
                                self.hp = max(0, self.hp)
                                print("You are hit by " + enemy + ". Please kill it before it kills you. Your health is reduced to " + str(
                                        self.hp))

                            if self.hp == 0:
                                print("\nOhh damm..! You are dead. Looks like you are killed by Troll...! Don't worry you still got " + str(
                                        self.life) + " life left.")
                                exit_status = True
                                break

                if user_choice == 1:
                    self.duck = update_duck_stats(self.hp, self.enemy_health, enemy, self.duck)
                elif user_choice == 2:
                    hit_factor = 30
                    ammo_factor = 3
                    self.ammo_dict[
                        "shotgun"], self.total_shoots, self.hp, self.enemy_health, exit_status, enemy_dead = update_ammo_stats(
                        self.ammo_dict["shotgun"],
                        enemy, self.enemy_health, self.hp,
                        self.total_shoots,
                        exit_status, hit_factor, ammo_factor)
                elif user_choice == 3:
                    reload_factor = 6
                    self.reload, self.ammo_dict["shotgun"] = update_reload_stats(self.reload, self.ammo_dict["shotgun"],
                                                                                 reload_factor, enemy)
                elif user_choice == 4:
                    increase_factor = 25
                    self.hp, self.medic, self.enemy_health = update_health_stats(self.medic, self.hp, increase_factor,
                                                                                 self.enemy_health, enemy, enemy_dead)
                elif user_choice == 5:
                    self.has_key = check_key_status(self.has_key, enemy, level_no=2)
                elif user_choice == 6:
                    print("\nSad to see you leave so soon! Do catch up before the alien invasion takes over the City.")
                    total_exit = True
                    break

                if self.hp == 0:
                    self.life -= 1
                    print("\nOhh damm..! You are dead. Looks like you are killed by viper...! Don't worry you still got " + str(
                            self.life) + " life left.")
                    exit_status = True
                    break

                inventory_stats(self.hp, self.enemy_health, self.medic, self.reload, self.ammo_dict["shotgun"],
                                self.has_key, 1)

                if self.has_key and self.enemy_health == 0:
                    level_1 = False

                move_count += 1
                self.total_moves += 1
            except Exception as e:
                print(e)
                print("Please enter a valid input.")

            print("------------------------------------------------------------------------------------------------------------------------------")

        stats_dict = {
            'duck': self.duck,
            'total_shoots': self.total_shoots,
            'shoot_level1': self.total_shoots,
            'level1_moves': move_count - 1,
            'life': self.life,
            'health': self.hp,
            'medic': self.medic,
            'ammo': self.ammo_dict,
            'reload': self.reload,
            'enemy_health': self.enemy_health,
            'weapons': self.weapons_list,
            'exit_status': exit_status,
            'has_key': self.has_key,
            'total_moves': self.total_moves,
            'total_exit': total_exit
        }

        return stats_dict


def main():
    """
    :return:
    """
    # initial status of  default ammo and guns
    ammo = {'shotgun': 6}  # ammo dictionary to hold different ammos with their magazine capacity
    weapons = ['shotgun']  # ammo list to hold to different ammo names
    enemy_health = 100
    life1 = 3
    exit_status = True  # exit status tells us exit the game when user selects exit option
    total_moves = 0  # total moves to track total moves done by user throughout the game.

    # Game rules
    rules()

    # Introduction to the game
    introduction()

    # ask user if he wants to start the game
    ask = input("Do you want to play the game? (y/n): ")
    if ask == "y" or ask == "Y":
        while life1 != 0 and exit_status:
            bm = Room1(duck=0, total_shoots=0, reload=1, medic=4, hp=100, ammo_dict=ammo, weapons_list=weapons,
                       enemy_health=enemy_health, life=life1, has_key=False,
                       total_moves=total_moves)
            stats = bm.enter_room_1()
            life1 = stats["life"]
            exit_status = stats["exit_status"]
            if stats["total_exit"]:
                sys.exit()
            elif stats["enemy_health"] == 0 and stats["has_key"] is True:
                print("You seemed to have killed the troll and possessed the key to room no. 2")
                life2 = 3
                exit_status = True
                while life2 != 0 and exit_status:
                    bm2 = Room2(stats)
                    stats1 = bm2.enter_room_2()
                    life2 = stats1["life"]
                    exit_status = stats1["exit_status"]
                    if stats1["total_exit"]:
                        sys.exit()
                    elif stats1["enemy_health"] == 0 and stats1["has_key"] is True:
                        print("You seemed to have killed the Neuroid and possessed the key to room no. 3")
                        life3 = 3
                        exit_status = True
                        while life3 != 0 and exit_status:
                            bm3 = Room3(stats1)
                            stats2 = bm3.enter_room_3()
                            life3 = stats2["life"]
                            exit_status = stats2["exit_status"]
                            if stats2["total_exit"]:
                                sys.exit()
                            elif stats2["enemy_health"] == 0 and stats2["has_key"] is True:
                                print("You seemed to have killed the Neuroid and possessed the key to room no. 3")
                                life4 = 3
                                exit_status = True
                                while life4 != 0 and exit_status:
                                    bm4 = Room4(stats2)
                                    stats3 = bm4.enter_room_4()
                                    life4 = stats3["life"]
                                    exit_status = stats3["exit_status"]
                                    if stats3["total_exit"]:
                                        sys.exit()
                                    elif stats3["enemy_health"] == 0 and stats3["has_key"] is True:
                                        print("You seemed to have killed the Neuroid and possessed the key to room no. 3")
                                        life5 = 3
                                        exit_status = True
                                        while life5 != 0 and exit_status:
                                            bm5 = Room5(stats3)
                                            stats4 = bm5.enter_room_5()
                                            life5 = stats4["life"]
                                            exit_status = stats4["exit_status"]
                                            if stats4["total_exit"] or (
                                                    stats4["enemy_health"] == 0 and stats4["hostages_saved"] is True):
                                                print("Congratulations, you have killed all aliens and saved the hostages. Earth is safe, thanks to you General!")
                                                view_game_stats(stats, stats1, stats2, stats3, stats4)
                                                sys.exit()
    elif ask == "n" or ask == "N":
        print("Game Exited")
        sys.exit()
    else:
        print("Invalid input!")


if __name__ == "__main__":
    main()
