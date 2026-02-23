"""epuck_go_forward controller."""

from controller import Robot
# On importe la classe Robot depuis le module Webots "controller"
# Cette classe permet de :
# - Créer l'objet Robot
# - Accéder aux moteurs/capteurs
# - Avancer la simulation pas à pas

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
# Cette ligne récupère le temps défini dans le monde Webots (ex 32 ms)
# et le convertit en entier.

leftMotor = robot.getDevice('left wheel motor')
# On récupère le périphérique (device) nommé "left wheel motor"

rightMotor = robot.getDevice('right wheel motor')
# On récupère le périphérique (device) nommé "right wheel motor"

leftMotor.setPosition(10.0)
# On définit une position de fin pour le moteur gauche.
# On aurait pu mettre float('inf') pour une rotation continue.

leftMotor.setVelocity(3.0)
# On définit la vitesse angulaire du moteur gauche.
# Valeur positive = marche avant
# Valeur négative = marche arrière

rightMotor.setPosition(10.0)
rightMotor.setVelocity(3.0)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    pass

# Enter here exit cleanup code.