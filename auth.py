users = {}
main = []
admins = []
loged = []
permissions = ['add_adm', 'remove_adm', 'log_out', 'adm_pr', 'show']
us_perm = ['log_out', 'adm_pr', 'show']

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
		if main == []:
			main.append(str(self.name))
			admins.append(self.name)
			print()
			print("Your permissions:")
			for i in permissions:
				print(i)
		else:
			print()
			print("Your permissions:")
			for i in us_perm:
				print(i)

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

def add_adm():
	print()
	name = str(input('Type a name to add: '))
	admins.append(name)

def remove_adm():
	print()
	name = str(input('Type a name to remove: '))
	admins.remove(name)

def adm_pr():
	for i in admins:
		print(i)

def log_out(name):
	loged.remove(name)

def show(name):
	print(name)