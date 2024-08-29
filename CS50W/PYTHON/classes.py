class Point():
	def __init__(self, input1, input2):
		self.x = input1
		self.y = input2

class Flight():
	def __init__(self, capacity):
		self.capacity = capacity
		self.passengers = []

	def open_seats(self):
		return self.capacity - len(self.passengers)

	def add_passanger(self, name):
		if self.open_seats() != 0:
			self.passengers.append(name)
			return True
		return False



flight = Flight(3)

people = ["Harry","Ron","Hermione","Ginny"]

for person in people:
	success = flight.add_passanger(person)

	if success:
		print(f"Added {person} to flight succesfully.")
	else:
		print(f"Not available seats for {person}")