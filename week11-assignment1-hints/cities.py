
class CitiesFST:
    def __init__(self):
        self.states = {
            'A': {'Z': 'B', 'K': 'C', 'ring': False},
            'B': {'Z': 'A', 'W': 'E', 'ring': False},
            'C': {'K': 'A', 'M': 'F', 'ring': False},
            'D': {'V': 'E', 'ring': False},
            'E': {'W': 'B', 'R': 'F', 'V': 'D', 'ring': False},
            'F': {'M': 'C', 'R': 'E', 'ring': True}
        }
        self.current = 'A'
        self.final = 'D'
        self.user_has_key = False

    def display_current(self):
        current = self.states[self.current]
        print(f"City: {self.current}")
        for key in current:
            if key == 'ring' and current[key]:
                print("There is a ring here, type GET to get it")
            elif key == 'ring' and not current[key]:
                print("No ring here")
            else:
                print(f"Type {key} to move to {current[key]}")
        print("==============================")
            

    def action(self, key):
        current = self.states[self.current]
        if key in current and key != 'ring':
            self.current = current[key]
        elif key == 'GET' and current['ring']:
            self.user_has_key = True
            print("You got the ring")
        else:
            print(f"Wrong choice {key}")


    def check_complete(self):
        if self.current == self.final and self.user_has_key:
            print("Mission accomplished")
            return True 
        else:
            return False



cities = CitiesFST()
completed = False
while not completed:
    cities.display_current()
    key = input("Type a letter so that you move to another city: ")
    cities.action(key)
    completed = cities.check_complete()
print("Bye!")
