import auth

class User:
	def __init__(self):
		auth.Login.__init__(self)
		command = ''
		print()
		if self.name in auth.admins:
			while not command == 'log_out':
				command = str(input('Type your command: '))
				while str(command) not in auth.permissions:
					command == str(input('Wrong command! Try again: '))
				if command == 'add_adm':
					auth.add_adm()
				elif command == 'show':
					auth.show(self.name)
				elif command == 'remove_adm':
					auth.remove_adm()
				elif command == 'adm_pr':
					auth.adm_pr()
				else:
					auth.log_out(self.name)
					print('You successfully logged out')
		else:
			while not command == 'log_out':
				command = str(input('Type your command: '))
				while str(command) not in auth.us_perm:
					command == str(input('Wrong command! Try again: '))
				if command == 'adm_pr':
					auth.adm_pr()
				elif command == 'show':
					auth.show(self.name)
				else:
					auth.log_out(self.name)
					print('You successfully logged out')

user = User()