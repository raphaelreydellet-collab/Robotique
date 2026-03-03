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
TH = 50  # Seuil de différence entre capteurs
MAX_SPEED = 5.0
MIN_SPEED = 1.0
DISTANCE_CIBLE = 0.01
TURN_FACTOR = 0.7  # Facteur de correction

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
    if sensor_value <= 0: return 0.09333
    for i in range(len(lookup_table) - 1):
        d1, v1 = lookup_table[i]
        d2, v2 = lookup_table[i + 1]
        if v1 >= sensor_value >= v2:
            return d1 + (d2 - d1) * (v1 - sensor_value) / (v1 - v2)
    return 0.0

while robot.step(timestep) != -1:
    vals = [ds[i].getValue() for i in range(7)]

    # Distance au centre (capteur 2)
    distance_center = sensor_value_to_distance(vals[2])

    if distance_center > 0:
        # Calcul vitesse proportionnelle
        base_speed = MAX_SPEED * (distance_center / 0.09333)
        base_speed = max(MIN_SPEED, min(base_speed, MAX_SPEED))

        # Gestion de la distance
        if distance_center < DISTANCE_CIBLE:
            base_speed = MIN_SPEED * 0.5
            led.set(0xFFA500)  # Orange
        else:
            led.set(0x00FF00)  # Vert

        # Correction de trajectoire
        left_diff = vals[0] - vals[1]  # Différence gauche
        right_diff = vals[4] - vals[3]  # Différence droite

        # Correction progressive
        left_speed = base_speed
        right_speed = base_speed

        if left_diff > TH:  # Plus à gauche
            left_speed *= TURN_FACTOR
        elif right_diff > TH:  # Plus à droite
            right_speed *= TURN_FACTOR

        # Appliquer les vitesses
        mL.setVelocity(left_speed)
        mR.setVelocity(right_speed)
    else:
        # Aucun obstacle détecté
        mL.setVelocity(0)
        mR.setVelocity(0)
        led.set(0xFFFFFF)  # Blanc
