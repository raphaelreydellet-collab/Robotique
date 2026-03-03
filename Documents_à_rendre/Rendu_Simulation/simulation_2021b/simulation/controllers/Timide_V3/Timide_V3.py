from controller import Robot

# Initialisation
robot = Robot()
timestep = int(robot.getBasicTimeStep() / 2)

# Configuration des moteurs
mL = robot.getDevice('motor.left')
mR = robot.getDevice('motor.right')
mL.setPosition(float('inf'))
mR.setPosition(float('inf'))
mL.setVelocity(0.0)
mR.setVelocity(0.0)

# Configuration des capteurs
ds = []
for i in range(7):
    d = robot.getDevice('prox.horizontal.' + str(i))
    d.enable(timestep)
    ds.append(d)

# LED
led = robot.getDevice('leds.top')

# Paramètres
Seuil = 200  # Seuil de détection
MAX_SPEED = 4.0  # Vitesse max
MIN_SPEED = 1.5  # Vitesse min
MAX_DISTANCE = 0.09333

def sensor_value_to_distance(sensor_value):
    lookup_table = [
        (0.0, 4235), (0.00333, 4308), (0.00666, 4298), (0.01, 4279),
        (0.01333, 4253), (0.01666, 4201), (0.02, 4139), (0.02333, 3981),
        (0.02666, 3733), (0.03, 3515), (0.03333, 3326), (0.03666, 3141),
        (0.04, 2965), (0.04333, 2860), (0.04666, 2696), (0.05, 2570),
        (0.05333, 2475), (0.05666, 2344), (0.06, 2248), (0.06333, 2182),
        (0.06666, 2044), (0.07, 1941), (0.07333, 1835), (0.07666, 1689),
        (0.08, 1597), (0.08333, 1473), (0.08666, 1345), (0.09, 1195),
        (0.09333, 0)
    ]
    if sensor_value >= 4235: return 0.0
    if sensor_value <= 0: return MAX_DISTANCE
    for i in range(len(lookup_table) - 1):
        d1, v1 = lookup_table[i]
        d2, v2 = lookup_table[i + 1]
        if v1 >= sensor_value >= v2:
            return d1 + (d2 - d1) * (v1 - sensor_value) / (v1 - v2)
    return 0.0

while robot.step(timestep) != -1:
    vals = [ds[i].getValue() for i in range(7)]
    distance = sensor_value_to_distance(max(vals[1:5]))  # Capteurs avant

    if any(v > Seuil for v in vals[1:5]):  # Obstacle devant
        # Arrêt complet
        mL.setVelocity(0)
        mR.setVelocity(0)
        led.set(0xFF0000)  # Rouge
    else:
        # Calcul vitesse proportionnelle avec minimum
        speed = MAX_SPEED * (distance / MAX_DISTANCE)
        speed = max(MIN_SPEED, min(speed, MAX_SPEED))

        # Maintien tout droit
        mL.setVelocity(speed)
        mR.setVelocity(speed)
        led.set(0x00FF00)  # Vert
