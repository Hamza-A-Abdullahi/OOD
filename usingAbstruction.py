from abstruction import Reptiles

class Snake(Reptiles):
    def __init__(self,age, weight, specie,name,region_found,number_of_fangs,length):
        super().__init__(age, weight, specie,name,region_found)
        self.number_of_fangs = number_of_fangs
        self.length=  length

    def can_contrict(self,value_boolean):
        return value_boolean

    def can_swim(self, value_boolean):
        return value_boolean


python= Snake(21,200,"Green tree python ","hamza","Papua New Guinea",12,30)

print(f" length {python.length}")
print(python.age)
print(f" weight is {python.weight}")
print(python.name)
print(f" number of fangs {python.number_of_fangs}")
print(python.can_contrict(True))
print(python.region_found)
print(python.specie)