import random

class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.life = True
        self.happy = 5
        self.zombie = False

    def eat(self):
        option = random.randint(0,2)
        if self.life:
            if option == 0:
                print(self.name + " says 'Mmmmmm, so good and tasty!'")
            if option == 1:
                print(self.name + " says 'So good!'")
            if option == 2:
                print(self.name + " says 'Finally, some good food.'")
            
        else:
            print(self.name + " is too ded to eat.")
            
    def sleep(self):
        option = random.randint(0,1)
        if self.life:
            if option == 0:
                print(self.name + " says 'im schleep'")
            if option == 1:
                print(self.name + " goes 'Zzzzzzzzz...'")
            
        else:
            print(self.name + " seems like they're asleep, atleast...")

    def play(self):
        if self.life:
            option = random.randint(0,1)
            if option == 0:
                print("Yeet!")
            if option == 1:
                print("Yote!")
        else:
            print("You can't play something if you're dead...")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1
        if self.life == False or self.zombie = True:
            print(self.name + " does a zombie walk.")

    def kill(self, other):
        if other.life == True and self.life == True:
            print(self.name + " attacks " + other.name +"!")
            print(other.name + " goes 'O  O  F' and dies horribly.")
            other.life = False
            other.happy = -5
        else:
            print("It's already dead!")

    def rise(self):
        self.life = True
        self.zombie = True
        print(self.name + " rises from the grave!")

    def zombify(self,other):
        if self.zombie == True and other.zombie == False:
            print(other.name + " turned into a zombie!")
            other.zombie = True

    def hug(self, other):
        print(self.name + " hugs " + other.name +"!")
        other.happy += 1

        if other.happy < 10:
            print(other.name + " says, 'I'm like " + str(other.happy) + " happy now.")
        elif other.happy > 0:
            print(other.name + " says, 'Um, this is awkward.'")
        else:
            print(other.name + " is still sad.")
            
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", alive? = " + str(self.alive) + \
               ", d=" + str(self.direction) + "]"
    
pet1 = Pet("Fluffy")
pet2 = Pet("datboi")
pet3 = Pet("Doggo")
