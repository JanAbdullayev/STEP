import random
l=True

class PetLife:
    def __init__(self, name):
        self.name = name
        self.rest = 50
        self.happiness = 10
        self.training = 100
        self.alive = True
    def to_study(self):
        print("Time to train")
        self.happiness += 0.12
        self.rest -= 5
        self.training+=100
    def to_sleep(self):
        print("I will sleep")
        self.rest += 3
    def trainingLevel(self):
        self.training+=10
        return self.training
    def to_chill(self):
        print("Rest time")
        self.rest += 5
        self.happiness -= 0.1
        self.training
    def is_alive(self):
        if self.rest < -0.5:
            print("Cast out…")
            self.alive = False
            l=False
        elif self.happiness <= 0:
            print("Depression…")
            self.alive = False
            l=False
        elif self.training > 400:
            print("Passed externally…")
            self.alive = False
            l=False
    def end_of_day(self):
        print(f"Happines = {self.happiness}")
        print(f"Progress ={round(self.training, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" +self.name + "life"
        print(f"{day:=^50}")
        if self.training <100:
            self.to_study()
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
            self.end_of_day()
            self.is_alive()

nick = PetLife(name=input("Enter name: "))
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)
