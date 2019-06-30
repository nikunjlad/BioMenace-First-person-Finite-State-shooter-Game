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
from BioMenace import update_health_stats, update_duck_stats, update_ammo_stats, update_reload_stats, check_input, level4, inventory_stats, check_key_status, level_stats


class Room4:

	def __init__(self, stats):
		"""

		:param stats: stats dict contains statistics of the game
		"""
		self.duck = stats["duck"]
		self.total_shoots = stats["total_shoots"]
		self.reload = 3
		self.medic = stats["medic"] + 6
		self.hp = stats["health"]
		self.ammo_dict = stats["ammo"]
		self.weapons_list = stats["weapons"]
		self.has_key = False
		self.life = 3
		self.enemy_health = 100
		self.exit_status = False
		self.total_moves = stats["total_moves"]

	def enter_room_4(self):
		"""

		:return: return status dictionary having status of various game properties (health, ammo, etc)
		"""
		self.ammo_dict["Plasma Blaster"] = 3
		self.weapons_list.append("Plasma Blaster")
		level_4 = True
		enemy_dead = False
		total_exit = False
		enemy = "Palatine"
		shoot_level4 = 0
		move_count = 1

		level4()

		print("*****************************************************************\n")
		level_stats(self.hp, self.life, self.medic, self.duck, self.total_shoots, self.weapons_list[3])

		while level_4:

			try:
				print("\n1. Duck\n2. Shoot 1 Plasma Blaster round\n3. Reload your gun\n4. Use a Medic-kit\n5. Pick up Room 4 Key\n6. Exit game")
				user_choice = check_input()

				if user_choice != 6:
					if not enemy_dead:
						if move_count % 2 != 0:
							if user_choice != 4:
								self.hp -= 38
								self.hp = max(0, self.hp)
								print("You are hit by " + enemy + ".  Please kill it before it kills you. Your health is reduced to " + str(self.hp))

							if self.hp == 0:
								print("\nOhh damm..! You are dead. Looks like you are killed by Palatine...! Don't worry you still got " + str(self.life) + " life left.")
								self.exit_status = True
								break

				if user_choice == 1:
					self.duck = update_duck_stats(self.hp, self.enemy_health, enemy, self.duck)
				elif user_choice == 2:
					hit_factor = 40
					ammo_factor = 1
					self.ammo_dict["Plasma Blaster"], shoot_level4, self.hp, self.enemy_health, self.exit_status, enemy_dead = update_ammo_stats(self.ammo_dict["Plasma Blaster"],
					                                                                                                                             enemy, self.enemy_health, self.hp,
					                                                                                                                             shoot_level4, self.exit_status,
					                                                                                                                             hit_factor, ammo_factor)
				elif user_choice == 3:
					reload_factor = 3
					self.reload, self.ammo_dict["Plasma Blaster"] = update_reload_stats(self.reload, self.ammo_dict["Plasma Blaster"], reload_factor, enemy)
				elif user_choice == 4:
					increase_factor = 30
					self.hp, self.medic, self.enemy_health = update_health_stats(self.medic, self.hp, increase_factor, self.enemy_health, enemy, enemy_dead)
				elif user_choice == 5:
					self.has_key = check_key_status(self.has_key, enemy, level_no=5)
				elif user_choice == 6:
					print("\nSad to see you leave so soon! Do catch up before the alien invasion takes over the City.")
					total_exit = True
					break

				if self.hp == 0:
					self.life -= 1
					print("\nOhh damm..! You are dead. Looks like you are killed by Palatine...! Don't worry you still got " + str(self.life) + " life left.")
					self.exit_status = True
					break

				inventory_stats(self.hp, self.enemy_health, self.medic, self.reload, self.ammo_dict["Plasma Blaster"], self.has_key, 4)

				if self.has_key and self.enemy_health == 0:
					level_4 = False

				move_count += 1
				self.total_moves += 1
			except Exception as e:
				print(e)
				print("Enter correct input.")

			print("-------------------------------------------------------------------------------------------------------------------------------")

		stats_dict = {
			'duck': self.duck,
			'total_shoots': self.total_shoots + shoot_level4,
			'shoot_level4': shoot_level4,
			'level4_moves': move_count - 1,
			'life': self.life,
			'health': self.hp,
			'medic': self.medic,
			'ammo': self.ammo_dict,
			'reload': self.reload,
			'enemy_health': self.enemy_health,
			'weapons': self.weapons_list,
			'exit_status': self.exit_status,
			'has_key': self.has_key,
			'total_moves': self.total_moves,
			'total_exit': total_exit
		}

		return stats_dict
