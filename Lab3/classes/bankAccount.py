class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def deposit(self):
		sum = int(input("Enter sum that you want to deposit: \n"))
		self.balance += sum
		print(f'Now your balance: {self.balance}')

	def withdraw(self):
		sum = int(input("Enter sum that you want to withdraw: \n"))
		if sum > self.balance:
			print(f'You don`t have enough money. Your balance: {self.balance}')
		else:
			self.balance -= sum
			print(f'Now your balance: {self.balance}')

person1 = Account(str(input("Hello, please enter your name! ")), 0)

while True:
	com = str(input(f"Hello {person1.owner}, enter the command (q/d/w): "))
	if com == 'q':
		break
	elif com == 'd':
		person1.deposit()
	elif com == 'w':
		person1.withdraw()