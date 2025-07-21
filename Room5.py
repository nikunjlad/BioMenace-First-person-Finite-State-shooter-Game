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
from BioMenace import update_health_stats, update_duck_stats, update_ammo_stats, check_input, update_reload_stats, level5, inventory_stats, level_stats


class Room5:

	def __init__(self, stats):
		"""

		:param stats: stats dict contains statistics of the game
		"""
		self.duck = stats["duck"]
		self.total_shoots = stats["total_shoots"]
		self.reload = 3
		self.medic = stats["medic"] + 8
		self.hp = stats["health"]
		self.ammo_dict = stats["ammo"]
		self.weapons_list = stats["weapons"]
		self.life = 3
		self.enemy_health = 100
		self.exit_status = False
		self.total_moves = stats["total_moves"]

	def enter_room_5(self):
		"""

		:return: return status dictionary having status of various game properties (health, ammo, etc)
		"""

		self.ammo_dict["Atomic Gun"] = 3
		self.weapons_list.append("Atomic Gun")
		level_5 = True
		enemy_dead = False
		total_exit = False
		enemy = "Xenomorph"
		shoot_level5 = 0
		move_count = 1
		hostage_saved = False

		level5()

		print("*****************************************************************\n")
		level_stats(self.hp, self.life, self.medic, self.duck, self.total_shoots, self.weapons_list[4])

		while level_5:

			try:
				print("\n1. Duck\n2. Shoot 1 Atomic Gun round\n3. Reload your gun\n4. Use a Medic-kit\n5. Rescue hostages\n6. Exit game")
				user_choice = check_input()

				if user_choice != 6:
					if not enemy_dead:
						if move_count % 2 != 0:
							if user_choice != 4:
								self.hp -= 40
								self.hp = max(0, self.hp)
								print("You are hit by " + enemy + ".  Please kill it before it kills you. Your health is reduced to " + str(self.hp))

							if self.hp == 0:
								print("\nOhh damm..! You are dead. Looks like you are killed by Xenomorph...! Don't worry you still got " + str(
									self.life) + " life left.")
								self.exit_status = True
								break

				if user_choice == 1:
					self.duck = update_duck_stats(self.hp, self.enemy_health, enemy, self.duck)
				elif user_choice == 2:
					hit_factor = 45
					ammo_factor = 1
					self.ammo_dict["Atomic Gun"], shoot_level5, self.hp, self.enemy_health, self.exit_status, enemy_dead = update_ammo_stats(self.ammo_dict["Atomic Gun"], enemy,
					                                                                                                                         self.enemy_health, self.hp,
					                                                                                                                         shoot_level5,
					                                                                                                                         self.exit_status, hit_factor,
					                                                                                                                         ammo_factor)
					self.hp -= 10
				elif user_choice == 3:
					if self.reload != 0:
						reload_factor = 3
						self.reload, self.ammo_dict["Atomic Gun"] = update_reload_stats(self.reload, self.ammo_dict["Atomic Gun"], reload_factor, enemy)
				elif user_choice == 4:
					increase_factor = 30
					self.hp, self.medic, self.enemy_health = update_health_stats(self.medic, self.hp, increase_factor, self.enemy_health, enemy, enemy_dead)
				elif user_choice == 5:
					if hostage_saved:
						print("You already have saved the hostage! Try to defend yourself now. Hostages are immune to alien attacks since they have evolved being with them.")
					else:
						hostage_saved = True
						print("\nYou have saved 3 hostages. I hope you have killed the Xenomorph. If not, haha.. good luck buddy!")
				elif user_choice == 6:
					print("\nSad to see you leave so soon! Do catch up before the alien invasion takes over the City.")
					total_exit = True
					break

				if self.hp == 0:
					self.life -= 1
					print("\nOhh damm..! You are dead. Looks like you are killed by Xenomorph...! Don't worry you still got " + str(self.life) + " life left.")
					self.exit_status = True
					break

				inventory_stats(self.hp, self.enemy_health, self.medic, self.reload, self.ammo_dict["Atomic Gun"], hostage_saved, 5)
				if hostage_saved and self.enemy_health == 0:
					level_5 = False

				move_count += 1
				self.total_moves += 1
			except Exception as e:
				print(e)
				print("Enter correct input.")

			print("------------------------------------------------------------------------------------------------------------------------------")

		stats_dict = {
			'duck': self.duck,
			'total_shoots': self.total_shoots + shoot_level5,
			'shoot_level5': shoot_level5,
			'level5_moves': move_count - 1,
			'life': self.life,
			'health': self.hp,
			'medic': self.medic,
			'ammo': self.ammo_dict,
			'reload': self.reload,
			'enemy_health': self.enemy_health,
			'weapons': self.weapons_list,
			'exit_status': self.exit_status,
			'hostages_saved': hostage_saved,
			'total_moves': self.total_moves,
			'total_exit': total_exit
		}

		return stats_dict
