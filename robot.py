#! /usr/bin/python

# IMPORTS
import keyboard	   		# MUST RUN AS ROOT TO USE THIS!
import robotlib as robot 	# IMPORT ROBOTLIB FOR ROBOT CONTROL FUNCTIONS

##########################################################################
##       PUT YOUR CODE IN THE TWO 'FUNCTIONS' BELOW THIS POINT          ##
##########################################################################


# Set speed of each motor (recommend 60%-100%)
robot.SetMotorASpeed(100)
robot.SetMotorBSpeed(100)


def RunChallenge1():
    # this code runs when you press the 1 key
    print("running challenge 1")
    t = 1
    robot.Forward(t)


def RunChallenge2():
    # this code runs when you press the 2 key
    print("running challenge 2")


def RunSelfTest():
    # run a series of simple robot commands to test it 
    print("Self test starting")
    robot.Forward(1) 
    robot.Right(1)
    robot.Left(1)
    robot.Backwards(1)
    print("Self test ended")


##########################################################################
##   Read the Keyboard presses and give the right command to the robot  ##
##########################################################################


print("Ready for Robot Commands...")

while True:
	event = keyboard.read_event()
	if event.event_type == keyboard.KEY_DOWN:
		if event.name == 'up':
			robot.RunForwards()
		if event.name == 'down':
			robot.RunBackwards()
		if event.name == 'left':
			robot.TurnLeft()
		if event.name == 'right':
			robot.TurnRight()
		if event.name == '1':
			RunChallenge1()
		if event.name == '2':
			RunChallenge2()
		if event.name == 't':
			RunSelfTest()
		if event.name == 'esc':
			robot.StopMotors()
			print("Escape Pressed, Exiting...")
			exit()
	elif event.event_type == keyboard.KEY_UP:
		robot.StopMotors()

print("Goodbye.")

