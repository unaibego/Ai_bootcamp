class Account(object):
	ID_COUNT = 1
	def __init__(self, name, **kwargs):
		self.__dict__.update(kwargs)
		self.id = self.ID_COUNT
		Account.ID_COUNT += 1
		self.name = name
		if not hasattr(self, 'value'):
			self.value = 0
		if self.value < 0:
			raise AttributeError("Attribute value cannot be negative.")
		if not isinstance(self.name, str):
			raise AttributeError("Attribute name must be a str object.")
	def transfer(self, amount):
		self.value += amount

def	check_corrupted(acount):
	names = 0
	ids = 0
	values = 0
	if len(dir(acount))% 2 == 1:
		return 1
	for string in dir(acount):
		if string[0] == 'b' or string[1:3] == 'zip' or string[1:4] == 'addr':
			return 2
		if	string == 'name':
			names = 1
		if	string == 'id':
			ids = 1
		if	string == 'value':
			values = 1
	if names == 0:
		return 3
	if ids == 0:
		return 4
	if values == 0:
		return 5
	if type(acount.name) != str:
		return 6
	if type(acount.id) != int:
		return 7
	if type(acount.value) != int and type(acount.value) != float:
		return 8
	return 0

class Bank(object):
	"""The bank"""
	def __init__(self):
		self.accounts = []
	def add(self, new_account):
		""" Add new_account in the Bank
		@new_account: Account() new account to append
		@return True if success, False if an error occured
		"""
		for acount in self.accounts:
			if acount.name == new_account:
				return False
		if isinstance(self, Account):
			return False
		try:
			self.accounts.append(new_account)
			return True
		except:
			return False
	def transfer(self, origin, dest, amount):
		"""" Perform the fund transfer
		@origin: str(name) of the first account
		@dest: str(name) of the destination account
		@amount: float(amount) amount to transfer
		@return True if success, False if an error occured
		"""
		count = 0
		for acount in self.accounts:
			if acount.name == origin:
				if (check_corrupted(acount)):
					print("Origin account is corrupted")
					return False
				if (acount.value < amount):
					return False
				count += 1
			if acount.name == dest:
				if (check_corrupted(acount)):
					print("Dest account is corrupted")
					return False
				count += 1
		if count != 2:
			return False
		for acount in self.accounts:
			if acount.name == origin:
				acount.value -= amount
			if acount.name == dest:
				acount.value += amount
		return True
			
	# ... Your code ...
	def fix_account(self, name):
		""" fix account associated to name if corrupted
		@name: str(name) of the account
		@return True if success, False if an error occured
		"""
		for acount in self.accounts:
			if acount.name == name:
				while(check_corrupted(acount)):
					if check_corrupted(acount) == 1:
						setattr(acount, "atribute1", "uknown")
					if check_corrupted(acount) == 2:
						for string in dir(acount):
							if string[0] == 'b'  or string[:3] == 'zip' or string[:4] == 'addr':
								delattr(acount, string)
					if check_corrupted(acount) == 3:
						setattr(acount, "name", "uknown")
					if check_corrupted(acount) == 4:
						setattr(acount, "id", 0)
					if check_corrupted(acount) == 5:
						setattr(acount, "values", 0)
					if check_corrupted(acount) == 6:
						delattr(acount, "name")
						setattr(acount, "name", "uknown")
					if check_corrupted(acount) == 7:
						delattr(acount, "id")
						setattr(acount, "id", 0)
					if check_corrupted(acount) == 8:
						delattr(acount, "value")
						setattr(acount, "value", 0)
				
								
	# ... Your code ...

cuenta1 = Account("Unai", value = 400000)
cuenta2 = Account("Andoni")
BBk = Bank()
BBk.add(cuenta1)
BBk.add(cuenta2)
BBk.fix_account("Unai")
# BBk.fix_account("Andoni")
BBk.transfer("Unai", "Andoni", 100)
print(cuenta1.value)
print(cuenta2.value)


