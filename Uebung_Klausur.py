# %%
x: int = 5
y = x

print(x)
print(y)

x += 9

print(x)
print(y)

# %%

x = [1,2,3]
y = x
y[0] = 5

print(x)
print(y)


# %%
class Car:
    def __init__ ( self ) -> None :
        self . __speed = 0 # make privateself    
        self.TOP_SPEED = 2300

    @property
    def speed ( self ):
        return self . __speed

    @speed.setter
    def speed ( self , new_speed ):
            # validation
        self . __speed = min ( new_speed , self.TOP_SPEED )
            # side effect
        print ( f" changing speed to { self . __speed }")
        
c = Car ()

c . speed = 500

# %%
class Car:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("Im Brumm Brumm")
        
class Plain:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("Im Fly Fly")  
        
class vehicle_1(Car, Plain):
    pass

class vehicle_2(Plain, Car):
    pass

v1 = vehicle_1("Any")
v2 = vehicle_2("Bert")

v1.say()

v2.say()        
        
# %%


 
my_list = [1,2,3,4,5,6,7,8,9,10]

new_list = [x for x in my_list if x%2 == 0]
new_lamda_list = list(filter(lambda x: x % 2 == 1 , my_list))

print(my_list)
print(new_list)
print(new_lamda_list)

# %%
