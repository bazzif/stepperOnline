import time
import RPi.GPIO as GPIO
from stepper import StepperMotor
# define pins



DIR1 = 16
STEP1 = 20
ENA1= 21

DIR2 = 17
STEP2 = 27
ENA2= 22

DIR3 = 10
STEP3 = 9
ENA3= 11

stepper1 = StepperMotor(ENA1, DIR1, STEP1)
stepper2 = StepperMotor(ENA2, DIR2, STEP2)
stepper3 = StepperMotor(ENA3, DIR3, STEP3)
stepper1.start()
stepper2.start()
stepper3.start()
stepper1.disable()
try:
    while True:
        stepper2.set_direction("clockwise")
        stepper2.move(200) 
        stepper3.set_direction("clockwise")
        stepper3.move(200) 
        time.sleep(1)
        stepper2.set_direction("counterclockwise")
        stepper2.move(200)
        stepper3.set_direction("counterclockwise")
        stepper3.move(200) # Rotate 200 steps counterclockwise
        time.sleep(1)
except KeyboardInterrupt:
    stepper.cleanup()

# direction = True
# # set pin mode
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR, GPIO.OUT)
# GPIO.setup(STEP, GPIO.OUT)
# GPIO.setup(ENA, GPIO.OUT)
# # Set rotation direction and stepping mode
# GPIO.output(DIR, direction)  # clockwise rotation
# GPIO.output(ENA, GPIO.HIGH)
# # Control stepper motor rotation
# periods = 20
# steps = 500 # Set the number of rotation steps
# delay = 0.001
# # set delay
# for j in range(periods):
#     direction = not direction
#     for i in range(steps):
#               GPIO.output(STEP, GPIO.HIGH)
#               time.sleep(delay)
#               GPIO.output(STEP, GPIO.LOW)
#               time.sleep(delay)
#     GPIO.output(DIR,direction)
# # Clean up GPIO and exit
# GPIO.cleanup()
