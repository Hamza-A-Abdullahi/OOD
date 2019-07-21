### abstruction
#giving the user only the information needede to perform a task
#while keeping unnecessary information away

class Animal():
    def __init__(self, age, weight, specie):
        self.color= weight
        self.size = age
        self.year = specie

    def can_hunt(self,value):
        return value

    def eat(self):
        return "nom nom nom"

    def sleep(self):
        return  "zz zz zz zz zz"


class Mammal(Animal):
    def __init__(self, age, weight, specie,name):      #contractor used when a new object is created
        super().__init__(age, weight, specie)
        self.name= name

    def can_speak_a_language(self,can_speak):
         return can_speak

class Bird(Animal):
    def __init__(self, age, weight, specie,name,feather_color):
        super().__init__(age, weight, specie)
        self.name= name
        self.feather_color= feather_color

    def can_fly(self, can_fly):
        return can_fly



class Reptiles(Animal):
    def __init__(self, age, weight, specie,name,region_found):
        super().__init__(age, weight, specie)
        self.region= region_found
        self.name= name

    def is_venomous(self,value):
        return value