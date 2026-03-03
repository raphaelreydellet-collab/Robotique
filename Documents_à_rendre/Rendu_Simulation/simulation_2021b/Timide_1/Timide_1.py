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

# Boucle principale
while robot.step(timestep) != -1:
    
    # Lecture des capteurs 
    vals = [ds[i].getValue() for i in range(7)]
    obstacle = any(v > 0 for v in vals[0:6])
    #Regulation vitesse
    
     # Logique
    if obstacle:
        mL.setVelocity(0)
        mR.setVelocity(0)
        led.set(0xFF0000) # rouge
    else:
        mL.setVelocity(2.0)
        mR.setVelocity(2.0)
        led.set(0x00FF00) # vert

