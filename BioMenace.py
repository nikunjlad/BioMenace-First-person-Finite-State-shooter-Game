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

import matplotlib

matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np


def update_health_stats(medic, hp, factor, enemy_health, enemy, enemy_dead):
    if medic != 0:
        print("\nYou seem to be badly hurt!  Nice move taking the medic. ")
        hp += factor
        hp = min(100, hp)  # trying to avoid health go beyond 100 in case of taking medikits
        if enemy == "Xenomorph":
            if enemy_dead:
                enemy_health = 0
            else:
                enemy_health += 5
                enemy_health = min(100, enemy_health)  # trying to avoid enemy health cross 100
        medic -= 1
        print("You health is restored to " + str(hp) + " hp after taking medic. You still have " + str(
            medic) + " kits remaining")
    else:
        print("You have run out of medic-kits. I really can't help you buddy...! RIP !!")

    return hp, medic, enemy_health


def update_duck_stats(hp, enemy_health, enemy, duck):
    print("\nYou ducked! Trying to avoid the bullets!! Nice move but try to be quick next time!")
    duck += 1
    print("Your health is " + str(hp) + "," + enemy + " health is " + str(enemy_health))
    return duck


def update_ammo_stats(ammo, enemy, enemy_health, hp, shoot, exit_status, hit_factor, ammo_factor):
    enemy_dead = False
    if ammo == 0:
        print("\nYou don't have enough ammo left. Please reload the gun!")
    else:
        print("\nYou hit the enemy! Keep going.")
        shoot += 1
        enemy_health -= hit_factor
        if enemy_health <= 0:
            ammo -= ammo_factor
            enemy_health = 0
            print(enemy + " health is " + str(enemy_health) + ".You killed a  " + enemy + ". Good game!")
            enemy_dead = True
            if not exit_status:
                exit_status = True
        else:
            ammo -= ammo_factor

    return ammo, shoot, hp, enemy_health, exit_status, enemy_dead


def update_reload_stats(reload, ammo, factor, enemy):
    """

    :param reload: number of reloads available to the user.
    :param ammo: ammo available for the guns
    :param factor: factor by which the ammo needs to be increased
    :param enemy: enemy name
    :return:
    """
    if reload != 0:
        print("\nLooks like you have run out of ammo. Let's make the reload quick")
        ammo += factor
        reload -= 1
        print("You have " + str(ammo) + " rounds in your shotgun after reload")
        print("You have " + str(reload) + " reload s left.")
    else:
        print("Looks like you have run out of ammo. Good luck with the " + enemy + "!!")

    return reload, ammo


def check_input():
    while True:
        try:
            choice = int(input("Select your  move from above: "))
            if choice < 1 or choice > 6:
                print("Please enter a positive integer value which is within the option range.")
            else:
                break
        except ValueError:
            print("Please enter a number.")

    return choice


def check_key_status(has_key, enemy, level_no):
    if has_key:
        print("You already have the Room " + str(level_no) + "keys.")
    else:
        has_key = True
        print("\nYou have picked up the Room " + str(
            level_no) + " keys. I hope you have killed the " + enemy + ". If not, haha.. good luck buddy!")

    return has_key


def introduction():
    print("********************************************************************\n")
    print("""
	INTRODUCTION
	
	Welcome to BioMenace! You are General Paul. As a veteran you are enjoying your days when,
	the CIA requires you for a top secret operation. Somewhere in the North Atlantic Ocean, besides
	Bermuda Triangle, lies an island whose inhabitants vanished suddenly in a span of a month. Heat
	signatures and our military scanners have come to identify a possible alien invasion of Planet Earth.
	The alien ship is supposedly said to have emerged from another dimension via the Bermuda Triangle.
	Your task is to kill these aliens and make sure the area is safe enough void of alien life. Remember 
	this is a suicide mission and you are all alone in this. You will be briefed by the intelligence as an when
	required on the mission. Humanity is in your hands General..! Good luck!
	
	""")
    print("********************************************************************\n")


def level1():
    print("********************************************************************\n")
    print("""
	WELCOME TO LEVEL 1
	
	Welcome to Level 1 General. Here your task is to kill the Troll. Trolls are green aliens which are huge
	and gigantic. You are given a shotgun with 2 medikits initially. Each magazine of the shotgun has 6 
	rounds in it. Your job is to kill the Troll and acquire the Key to next level. Your health will decrease 
	gradually along the course of the level as you will take hits from the Troll and so will the health of 
	the Troll reduce as you fire your rounds. Use the medikits wisely! Good Luck!
	
	""")
    print("********************************************************************\n")


def level2():
    print("********************************************************************\n")
    print("""
	WELCOME TO LEVEL 2
	
	Welcome to Level 2 General. Here your task is to kill the fire spitting Viper. Vipers are pretty fast 
	creatures and they spit fire balls in quick succession.You are given a  Bullpup rifle with each magazine 
	having 10 rounds in it. Your job is to kill the Viper and acquire the Key to next level. Your health will decrease 
	gradually along the course of the level as you will take hits from the Viper and so will the health of 
	the Viper reduce as you fire your rounds. Use the medikits wisely! Good Luck!

	""")
    print("********************************************************************\n")


def level3():
    print("********************************************************************\n")
    print("""
	WELCOME TO LEVEL 3
	
	Welcome to Level 3 General. Here your task is to kill the Neuroid. Neuroids are psychic aliens. They
	hypnotise you when you look them in the eye. You are given a  Magnum Sniper with each magazine 
	having 7 rounds in it. Your job is to kill the Neuroid with a headshot and acquire the Key to next level. 
	Your health will decrease gradually along the course of the level as you will take hits from the Neuroid
	and so will the health of  the Neuroid reduce as you fire your rounds. Use the medikits wisely! Good Luck!

	""")
    print("********************************************************************\n")


def level4():
    print("********************************************************************\n")
    print("""
	WELCOME TO LEVEL 4
	
	Welcome to Level 4 General. Here your task is to kill the Palatine. Palatines are generals in the alien world. They
	serve the mother queen and defend her to their last breath. You are given a  Plasma Blaster with each magazine 
	having 3 rounds in it.  Plasma Blaster are advanced weaponary which are derived from the alien universe. They
	can cause lot of damage. Your job is to kill the Palatine and acquire the Key to next level. 
	Your health will decrease gradually along the course of the level as you will take hits from the Palatine
	and so will the health of  the Palatine reduce as you fire your rounds. Use the medikits wisely! Good Luck!

	""")
    print("********************************************************************\n")


def level5():
    print("********************************************************************\n")
    print("""
	WELCOME TO LEVEL 5
	
	Welcome to Level 5 General. You finally have one task left. Kill the Xenomorph. Xenomorph are mother aliens. 
	She commands everything and breeds other aliens. You are given an Atomic Blaster with each magazine 
	having 3 rounds in it. Atomic Blasters are radioactive weaponary. Devised by humans for mass destruction they can literally create a dent in the universe.
	Though you are having a radiation proof kevlar, for every shot you take, your health will reduce. Also, for every medikit you take, the Queen heals herself 
	by some proportion compared to you. Your job is to kill the Queen and save the hostages. 
	Your health will decrease gradually along the course of the level as you will take hits from the Queen
	and so will the health of  the Queen reduce as you fire your rounds. Use the medikits wisely! Good Luck!

	""")
    print("********************************************************************\n")


def level_stats(hp, life, medic, duck, total_shoots, gun):
    print("*****************************************************************\n")
    print("Current game statistics which you might want to look at!")
    print("1. Your current health is " + str(hp))
    print("2. Your current ammunition is " + gun)
    print("3. You currently have " + str(life) + " lives left in this level.")
    print("4. You currently have " + str(medic) + " medic-kits.")
    print("5. You have ducked " + str(duck) + " times till now.")
    print("6. You have shot " + str(total_shoots) + " rounds till now.")


def inventory_stats(hp, enemy_health, medic, reload, ammo, has_key, level):
    try:
        if has_key:
            if level != 5:
                key = "You have the keys"
            else:
                key = "You have saved the hostages. Please keep them safe!"
        else:
            if level != 5:
                key = "You do not have the keys"
            else:
                key = "You haven't saved any hostages. Please rescue them!"
    except Exception as e:
        print(e)
        key = "Rescue hostages"

    print("Inventory Stats: | Your health : " + str(hp) + " | Enemy health : " + str(
        enemy_health) + " | MedicKits : " + str(medic) + " | Reloads : " + str(reload) + " | Ammo : " + str(
        ammo) + " | Keys / Hostages :" + key)


def make_plots(pt1, pt2, pt3, pt4, pt5, labels):
    x = np.arange(5)
    val = [pt1, pt2, pt3, pt4, pt5]

    def millions(x, _):
        # The two args are the value and tick position
        return '%2d' % x

    formatter = FuncFormatter(millions)
    fig, ax = plt.subplots()
    ax.yaxis.set_major_formatter(formatter)
    plt.bar(x, val)
    plt.xlabel("Levels")
    plt.ylabel(labels)
    plt.xticks(x, ('Level 1', 'Level 2', 'Level 3', 'Level 4', 'Level 5'))
    plt.show()


def view_game_stats(stats1, stats2, stats3, stats4, stats5):
    make_plots(stats1["shoot_level1"], stats2["shoot_level2"], stats3["shoot_level3"], stats4["shoot_level4"],
               stats5["shoot_level5"], labels="Shoots done")
    make_plots(stats1["life"], stats2["life"], stats3["life"], stats4["life"], stats5["life"], labels="lives left")
    make_plots(stats1["health"], stats2["health"], stats3["health"], stats4["health"], stats5["health"],
               labels="health left")
    make_plots(stats1["medic"], stats2["medic"], stats3["medic"], stats4["medic"], stats5["medic"],
               labels="medics left")
    make_plots(stats1["ammo"]["shotgun"], stats2["ammo"]["Bullpup"], stats3["ammo"]["Magnum Sniper"],
               stats4["ammo"]["Plasma Blaster"], stats5["ammo"]["Atomic Gun"], labels="ammo left")
    make_plots(stats1["reload"], stats2["reload"], stats3["reload"], stats4["reload"], stats5["reload"],
               labels="reloads left")
    make_plots(stats1["level1_moves"], stats2["level2_moves"], stats3["level3_moves"], stats4["level4_moves"],
               stats5["level5_moves"], labels="Moves made per level")


def rules():
    print("********************************************************************\n")
    print("""
		GAME RULES

		1. This is first person shooter game. You need to select options and play the moves.
		2. Select integer values only.
		3. Your health is reduced every alternate move as part of the enemy attacking you. 
		4. Use medic kits wisely.
		5. You have 3 lives per level after which the game will terminate
		6. The 'Duck' command is a deception and may / may not be used. Honestly its there to eat up your moves
		7. Your health will reduce by different proportions in different levels.
		8. Your game statistics will be displayed at the end once you win.

		""")
    print("********************************************************************\n")


if __name__ == "__main__":
    make_plots(3, 6, 7, 8, 20, "hello")
