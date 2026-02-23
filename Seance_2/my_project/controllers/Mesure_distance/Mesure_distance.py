from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Moteurs
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')

# Encodeurs (capteurs de position des roues)
leftSensor = robot.getDevice('left wheel sensor')
rightSensor = robot.getDevice('right wheel sensor')
leftSensor.enable(timestep)
#Active le capteur
rightSensor.enable(timestep)

# Mode vitesse (avance continue)
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(1.0)
rightMotor.setVelocity(1.0)

# Rayon de roue e-puck (≈ 20.5 mm = 0.0205 m)
WHEEL_RADIUS = 0.0205  # en mètres

# Attendre 1 pas pour que les capteurs soient valides
robot.step(timestep)

# Valeurs initiales des encodeurs (en radians)
left0 = leftSensor.getValue()
right0 = rightSensor.getValue()

while robot.step(timestep) != -1:
    # Angles actuels (rad)
    leftAngle = leftSensor.getValue()
    rightAngle = rightSensor.getValue()

    # Distance parcourue par chaque roue depuis le départ (m)
    dLeft = (leftAngle - left0) * WHEEL_RADIUS
    dRight = (rightAngle - right0) * WHEEL_RADIUS

    # Distance robot (si déplacement quasi rectiligne)
    distance = (dLeft + dRight) / 2.0

    print(f"Distance parcourue : {distance:.3f} m")