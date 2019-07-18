### inheritance

class Vehicel():
    def __init__(self, size, color, year, make,speed):
        self.make= make
        self.color= color
        self.size = size
        self.year = year
        self.speed= speed


class Truck(Vehicel):
    def __init__(self, size, color, year, make,speed, trailer_size):
        super().__init__(size, color, year, make,speed)
        self.trailer = trailer_size


    def accelarate(self):
        return self.speed ++ 10


my_car=  Vehicel(1.3, "blue", 2014, "Audi",75)
my_truck= Truck(4.5,"matt black",2019,"ford",14,75)

print(f"Hamza has a {my_car.make} of size {my_car.size} of color {my_car.color} is year {my_car.year}")

print(f"mike has a {my_truck.make} of size {my_truck.size} of color {my_truck.color} is year {my_truck.year} \n "
      f"trailor size is {my_truck.trailer} ")

print(my_truck.accelarate())
