### inheritance

class Vehicel():
    def __init__(self, engin_size, color, year, make, speed):
        self.make= make
        self.color= color
        self.size = engin_size
        self.year = year
        self.speed= speed

    def accelarate(self):
        return self.speed ++ 10

    def start(self):
        return "Vrooooom"

    def stop(self):
        return  "screech"


class Truck(Vehicel):
    def __init__(self, engin_size, color, year, make, speed, trailer_size):
        super().__init__(engin_size, color, year, make, speed)
        self.trailer = trailer_size



class Boat(Vehicel):
    def __init__(self, engin_size, color, year, make, speed, status_ancher, ):
        super(Boat, self).__init__(engin_size, color, year, make, speed)
        self.status = status_ancher

    def sink(self):
        return "i am sinkinggg"

    def b_horn(self):
        return  "ooooooooooOOOOOOOOOGHOGHOGH"


my_car=  Vehicel(1.3, "blue", 2014, "Audi",75)
my_truck= Truck(4.5,"matt black",2019,"ford",14,75)

my_boat= Boat(4,"white",2016,"BOSTON WHALER",35.2,True)

print(f"Hamza has a {my_car.make} of size {my_car.size} of color {my_car.color} is year {my_car.year} the speed is {my_truck.accelarate()}\n")

print(f"mike has a {my_truck.make} of size {my_truck.size} of color {my_truck.color} is year {my_truck.year} \n "
      f"trailor size is {my_truck.trailer} the speed is {my_truck.accelarate()} ")


print(f" boat status is {my_boat.status} is the boat sinking or floating {my_boat.b_horn()} ")