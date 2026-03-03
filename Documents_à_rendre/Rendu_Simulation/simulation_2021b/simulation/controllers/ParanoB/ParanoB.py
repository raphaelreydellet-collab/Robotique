from controller import Robot

# Initialisation
robot = Robot()
timestep = int(robot.getBasicTimeStep()/2)

# Configuration des Moteurs
mL = robot.getDevice('motor.left')
mR = robot.getDevice('motor.right')
mL.setPosition(float('inf'))
mR.setPosition(float('inf'))
mL.setVelocity(0.0)
mR.setVelocity(0.0)

# Configuration des Capteurs de proximité (0 à 6)
ds = []
for i in range(7):
    d = robot.getDevice('prox.horizontal.' + str(i))
    d.enable(timestep)
    ds.append(d)

# LED & Clavier (clavier pas utilisé ici, mais on le laisse)
led = robot.getDevice('leds.top')
kb = robot.getKeyboard()
kb.enable(timestep)

# --- Un seul seuil
TH = 500
Vmax=9.3


# Boucle principale
while robot.step(timestep) != -1:

    # Lecture des capteurs
    vals = [ds[i].getValue() for i in range(7)]


    Moy_F=(vals[1]+ vals[2]+ vals[3])/3
    Moy_R = (vals[3]+vals[4])/2
    Moy_L = (vals[0]+vals[1])/2
    
    obs_F = (Moy_F > TH)          # devant
    obs_R = (vals[4]>vals[3])          # droite
    obs_L = (vals[0]>vals[1])         # gauche

    # Logique
    if obs_F:
        # obstacle devant -> tourner sur place
        vitesse=-0.0022*Moy_F + Vmax         
        mL.setVelocity(vitesse)
        mR.setVelocity(vitesse)
        led.set(0x00FF00)  # vert
        

    elif obs_R:
        # obstacle à droite -> tourner à gauche
         
        vitesse=-0.0025*Moy_R + Vmax
        mL.setVelocity(-(vitesse))
        mR.setVelocity(vitesse)
        led.set(0x0000FF)  # bleu

    elif obs_L:
        # obstacle à gauche -> tourner à droite
        vitesse=-0.0025*Moy_L + Vmax
        mL.setVelocity(vitesse)
        mR.setVelocity(-(vitesse))
        led.set(0xFFFFFF)  # blanc

    else:
        # rien -> arret
        mL.setVelocity(0)
        mR.setVelocity(0)
        led.set(0xFF0000)  # rouge
        