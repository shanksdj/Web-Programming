from sre_constants import SUCCESS


class point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = point(2,5)

print(p.x)
print(p.y)


class Flights():
    def __init__(self, Capacity):
        self.Capacity = Capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats (self):
        return self.Capacity - len(self.passengers)

flight = Flights(30)
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flights successfully.")
    else:
        print(f"No Available Seat for {person}.")
