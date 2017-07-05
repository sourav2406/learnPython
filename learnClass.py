class CreditCard:
	def __init__(self,customer, bank, acnt, limit):
		self._customer = customer
		self._bank = bank
		self._account = acnt
		self._limit = limit
		self._balance = 0

	def get_customer(self):
		return self._customer

	def get_bank(self):
		return self._bank

	def get_account(self):
		return self._account

	def get_limit(self):
		return self._limit

	def get_balance(self):
		return self._balance

	def charge(self,price):
		if price + self._balance > self._limit:
			return False
		else:
			self._balance+=price
			return True

	def make_payment(self,amount):
		self._balance-= amount

if __name__ == '__main__':
	my_card = CreditCard('Sourav','axis','9875000065462582',10000)

	print(my_card.get_customer())
	print(my_card.get_bank())
	print(my_card.get_account())
	print(my_card.get_limit())
	print(my_card.get_balance())