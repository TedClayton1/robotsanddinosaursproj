from robot import Robot
from weapon import Weapon

axe = Weapon('axe', 50)
axe2 = Weapon('karate chop', 15)

robot1 = Robot("Tony", 10, axe)
robot2 = Robot("Byron", 2, axe)
robot3 = Robot("Webster", 5, axe2)



# print(robot3.name)

from dinosaurs import Dinosaurs

dino1 = Dinosaurs("Jimmy", 8, 10)
dino2 = Dinosaurs("Tyrone", 2, 3)
dino3 = Dinosaurs("Ryan", 10, 120)

# robot1.attack(dino1)
dino3.attack(robot3)