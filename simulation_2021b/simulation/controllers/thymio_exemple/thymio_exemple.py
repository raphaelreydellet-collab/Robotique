# Copyright 1996-2019 Cyberbotics Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This controller gives to its node the following behavior:
Listen the keyboard. According to the pressed key, send a
message through an emitter or handle the position of Robot1.
"""
from controller import *
import time

robot = Robot()
timestep = int(robot.getBasicTimeStep())
keyboard = robot.getKeyboard()
keyboard.enable(timestep)

print("Initialization")

led =  robot.getDevice('leds.bottom.right')
led2 = robot.getDevice('leds.bottom.left')
led3 = robot.getDevice('leds.prox.v.led0')
led4 = robot.getDevice('leds.prox.v.led1')
led5 = robot.getDevice('leds.top')

distanceSensors = []
for i in list(range(0,7)):
  distanceSensors.append(robot.getDevice('prox.horizontal.'+str(i)))
  distanceSensors[i].enable(timestep)

motor_left = robot.getDevice("motor.left");
motor_right = robot.getDevice("motor.right");
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

robot_speed = 0.0
distanceVal = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
state = 0
motor_left.setVelocity(0)
motor_right.setVelocity(0)

while (robot.step(timestep) != -1):
  # Read the sensors, like:
  for i in list(range(0,7)):
    distanceVal[i] = distanceSensors[i].getValue()
  #print(distanceVal)     # Display sensor values
  motor_left.setVelocity(robot_speed)
  motor_right.setVelocity(0.0) #robot_speed

  # Process sensor data here
  if state==1:                   # Timid
    print('Timid')
  elif state==2:                 # Indecisive
    print('Indecisive')
  elif state==3:                 # Paranoid
    print('Paranoid')
  elif state==4:                 # Paranoid 1
    print('Paranoid 1')
  elif state==5:                # Paranoid 2
    print('Paranoid 2')

  # Enter here functions to send actuator commands, like:
  led.set(0xff0000)   #red
  led2.set(0x00ff00)  #green
  led3.set(32)
  led4.set(32)
  led5.set(0x0000ff)  #blue
  
  command = keyboard.getKey()
  #print(command)

  if command==65: # Touche a : Timid
    state = 1
  elif command==66: # Touche b : Indecisive
    state = 2
  elif command==67: # Touche c : Paranoid
    state = 3
  elif command==68: # Touche d : Paranoid 1
    state = 4
  elif command==69: # Touche e : Paranoid 2
    state = 5
  elif command==88: # Touche x : Manual control
    state = 0