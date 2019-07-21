#ENCAPSULATION

class Person():

    def __init__(self,age,name,email,height):
        self.__height = height    #_Person__height
        self.age= age
        self.name= name
        self.email=email


    def show(self):

        print(f" my name is {self.name}  and i am {self.age} old and email is {self.email} "
              f"and height {self.__height}")



    def set_height(self,value):
        if value > 9 or value < 0:
            self.__height = 4.5
        else:
            self.__height = value

    def get_height(self):
        return self.__height

Hamza= Person(24,"Hamza","jack@gmail.com",1.88)

# Hamza.show()
# Hamza.name= "Luc"
# Hamza.show()
# Hamza.age= 33
Hamza.show()

Hamza.set_height(5.5) ## this will work from accidental outisde changing not intentional
Hamza.show()           #print(markson.__height)  # this will crash


Hamza.he
