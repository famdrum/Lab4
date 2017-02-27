import string
import os
import time
import copy

users = {}
admins = ['admin']
loged = []

class Ship:
	def __init__(self, length, bow):
		self.length = length
		self.bow = bow
		self.hit = [False for i in range(sum(self.length) - 1)]
class Field:
	def __init__(self):
		import random
		points = [(i, j) for i in range(10) for j in range(10)]
		field = [[' ' for i in range(10)] for i in range(10)]
		check = []
		for ship in range(4, 0, -1):
			repeat = ship
			while repeat != 5:
				direction = random.choice((1,2))
				if direction == 1:
					while True:
						point = random.choice(points)
						g_ship = Ship((1, ship), point)
						for i in range(ship):
							if ((g_ship.bow[0]), (g_ship.bow[1] + i)) not in points:
								check = []
								break
							if ((g_ship.bow[0]), (g_ship.bow[1] + i)) in points:
								check.append(((g_ship.bow[0]), (g_ship.bow[1] + i)))
						if check == []:
							continue
						check = []
						for i in range(3):
							for k in range(ship + 2):
								if ((g_ship.bow[0] - 1 + i), (g_ship.bow[1] - 1 + k)) in points:
									check.append(((g_ship.bow[0] - 1 + i), (g_ship.bow[1] - 1 + k)))
						for i in check:
							points.remove(i)
						check = []
						for i in range(ship):
							field[g_ship.bow[0]][g_ship.bow[1] + i] = g_ship
						break
				if direction == 2:
					while True:
						point = random.choice(points)
						g_ship = Ship((ship, 1), point)
						for i in range(ship):
							if ((g_ship.bow[0] + i), (g_ship.bow[1])) not in points:
								check = []
								break
							if ((g_ship.bow[0] + i), (g_ship.bow[1])) in points:
								check.append(((g_ship.bow[0] + i), (g_ship.bow[1])))
						if check == []:
							continue
						check = []
						for i in range(3):
							for k in range(ship + 2):
								if ((g_ship.bow[0] - 1 + k), (g_ship.bow[1] - 1 + i)) in points:
									check.append(((g_ship.bow[0] - 1 + k), (g_ship.bow[1] - 1 + i)))
						for i in check:
							points.remove(i)
						check = []
						for i in range(ship):
							field[g_ship.bow[0] + i][g_ship.bow[1]] = g_ship
						break
				repeat += 1
		return field
class Player:
	def __init__(self):
		self.name = Login.__init__(self)
class Game:
	def __init__(self):
		Player.__init__(self)
		self.field = Field.__init__(self)
		self.ls = ls = [[' ' for i in range(10)] for i in range(10)]
		self.check = 'oops'
	def read_position(self):
		while True:
			try:
				strike = str(input(self.name + ', enter move: '))
				if strike.lower() == 'restart' and self.name not in admins:
					raise Not_Permitted
				elif strike.lower() == 'restart' and self.name in admins:
					start_game()
					time.sleep(1)
				else:
					if type(self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())]) == Ship:
						if self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].length[0] == 1:
							k = self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].bow[1] - string.ascii_letters.index(strike[0].lower())
							self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].hit[k] = True
						else:
							k = self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].bow[0] - int(strike[1]) - 1
							self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())].hit[k] = True
					return strike
				break
			except Not_Permitted as error:
				error.message(self.name)
			
	def field_without_ships(self):
		strike = Game.read_position(self)
		time.sleep(1)
		if type(self.field[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())]) == Ship:
			self.ls[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())] = 'X'
			self.check = 'checked'
		else:
			self.ls[int(strike[1]) - 1][string.ascii_letters.index(strike[0].lower())] = '0'
			self.check = 'oops'
		fin = ""
		for i in self.ls:
			for k in i:
				fin += k
			fin += '\n'
		print(fin)
	def field_with_ships(self):
		field = copy.deepcopy(self.field)
		for i in range(len(field)):
			for j in range(len(field[i])):
				if type(field[i][j]) == Ship:
					if field[i][j].length[0] == 1:
						if field[i][j].hit[field[i][j].bow[1] - j] == True:
							field[i][j] = 'X'
						else:
							field[i][j] = '*'
					else:
						if field[i][j].hit[field[i][j].bow[0] - i] == True:
							field[i][j] = 'X'
						else:
							field[i][j] = '*'
		st = field
		fin = ""
		for i in st:
			for k in i:
				fin += k
			fin += '\n'
		print(fin)

class Name_Exists(Exception):
	def message(self, name):
		print(str(name) + " already exists!")

class Password_Short(Exception):
	def message(self):
		print("Your password is too short!")

class Name_Not(Exception):
	def message(self ,name):
		print(str(name) + " doesn't exist!")\

class Password_Wrong(Exception):
	def message(self):
		print("Your password is wrong! Try again")

class Not_Permitted(Exception):
	def message(self, name):
		print(str(name) + ", you don't have a permission!")

class Registration:
	def __init__(self):
		print("REGISTRATION")
		print("============")
		while True:
			try:
				self.name = str(input("Type your name: "))
				if self.name in users:
					raise Name_Exists
				break
			except Name_Exists as error:
				error.message(self.name)
		print()
		while True:
			try:
				self.password = str(input("Come up with your password: "))
				if len(self.password) < 6:
					raise Password_Short
				break
			except Password_Short as error:
				error.message()
		users.update({self.name:self.password})

class Login:
	def __init__(self):
		check = ''
		print("LOG IN")
		print("======")
		while True:
			try:
				self.name = str(input("Enter your name. Not registered? Press 'Enter': "))
				while self.name in loged:
					self.name = str(input("Already logged in! Choose an other name. Not registered? Press 'Enter': "))
				if self.name == '':
					print()
					Registration.__init__(self)
					check = "checked"
					break
				if self.name not in users:
					raise Name_Not
				break
			except Name_Not as error:
				error.message(self.name)
		if not check == 'checked':
			print()
			while True:
				try:
					self.password = str(input("Type your password: "))
					if not self.password == users[self.name]:
						raise Password_Wrong
					break
				except Password_Wrong as error:
					error.message()
		loged.append(self.name)
		return self.name

def start_game():
	time.sleep(1)
	print('Player1, please login or register')
	print()
	player1 = Game()
	print('')
	time.sleep(1)
	os.system('cls')
	print('Player2, please login or register')
	print()
	player2 = Game()
	time.sleep(0.5)
	os.system('cls')
	print('Field of the first player')
	player2.field_with_ships()
	time.sleep(4)
	os.system('cls')
	time.sleep(1)
	print('')
	print('Field of the second player')
	player1.field_with_ships()
	time.sleep(4)
	os.system('cls')
	time.sleep(2)
	while True:
		print('First player')
		player2.field_with_ships()
		player1.field_without_ships()
		while player1.check == 'checked':
			time.sleep(1)
			os.system('cls')
			time.sleep(0.5)
			print('First player')
			player2.field_with_ships()
			player1.field_without_ships()
		time.sleep(1)
		os.system('cls')
		time.sleep(0.5)
		print('Second player')
		player1.field_with_ships()
		player2.field_without_ships()
		while player2.check == 'checked':
			time.sleep(1)
			os.system('cls')
			time.sleep(0.5)
			print('Second player')
			player1.field_with_ships()
			player2.field_without_ships()
		time.sleep(1)
		os.system('cls')
		time.sleep(0.5)

start_game()
