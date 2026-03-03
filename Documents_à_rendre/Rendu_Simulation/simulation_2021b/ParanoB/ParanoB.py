from controller import Robot

# Initialisation
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Configuration des Moteurs
mL = robot.getDevice('motor.left')
mR = robot.getDevice('motor.right')
mL.setPosition(float('inf'))
mR.setPosition(float('inf'))
mL.setVelocity(0.0)
mR.setVelocity(0.0)

# Configuration des Capteurs de proximité (ds0 à ds6)
ds = []
for i in range(7):
    d = robot.getDevice('prox.horizontal.' + str(i))
    d.enable(timestep)
    ds.append(d)
 
# LED & Clavier
led = robot.getDevice('leds.top')
kb = robot.getKeyboard()
kb.enable(timestep)

from enum import Enum
class Obstacle (Enum):
    absence = 1
    lointain = 2
    proche = 3
    imminent = 4
    colision =5
Seuils = {
    Obstacle.absence : (0),
    Obstacle.lointain : (1,999),
    Obstacle.proche : (1000,1499),
    Obstacle.imminent : (1500,1999),
    Obstacle.colision : (2000,4990),
         }
    
 

# Boucle principale
while robot.step(timestep) != -1:
    
    # Lecture des capteurs 
    vals = [ds[i].getValue() for i in range(7)]
    obs_F = any(v > 0 for v in vals[1:3])
    obs_R = (vals[4]>vals[3])
    obs_L = (vals[0]>vals[1])
     # Logique
    if obs_F:
        if 
        mL.setVelocity(8)
        mR.setVelocity(8)
        led.set(0x00FF00) # vert
        
    elif obs_R:
        mL.setVelocity(8)
        mR.setVelocity(-2)
        led.set(0x0000FF) # bleu
        
    elif obs_L:
        mL.setVelocity(-2)
        mR.setVelocity(8)
        led.set(0xFFFFFF) # blanc

    else:
        mL.setVelocity(0)
        mR.setVelocity(0)
        led.set(0xFF0000) # rouge
 
