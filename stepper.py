import threading
import RPi.GPIO as GPIO

class StepperMotor:
    gpio_initialized = False

    @staticmethod
    def setup_gpio():
        if not StepperMotor.gpio_initialized:
            GPIO.setmode(GPIO.BCM)
            StepperMotor.gpio_initialized = True

    def __init__(self, enable_pin, direction_pin, step_pin):
        self.enable_pin = enable_pin
        self.direction_pin = direction_pin
        self.step_pin = step_pin

        StepperMotor.setup_gpio()

        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.direction_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)

        self.enable()
        self.direction = "clockwise"  # Default direction
        self.steps_to_move = 0
        self.move_event = threading.Event()
        self.move_thread = threading.Thread(target=self.move_thread_func)

    def enable(self):
        GPIO.output(self.enable_pin, GPIO.HIGH)

    def disable(self):
        GPIO.output(self.enable_pin, GPIO.LOW)

    def set_direction(self, direction):
        self.direction = direction

    def move(self, steps):
        self.steps_to_move = steps
        self.move_event.set()  # Set the event to trigger the movement

    def move_thread_func(self):
        while True:
            self.move_event.wait()  # Wait for the event to be set
            if self.direction == "clockwise":
                GPIO.output(self.direction_pin, GPIO.HIGH)
            elif self.direction == "counterclockwise":
                GPIO.output(self.direction_pin, GPIO.LOW)
            
            for _ in range(self.steps_to_move):
                GPIO.output(self.step_pin, GPIO.HIGH)
                time.sleep(0.001)  # Adjust as needed
                GPIO.output(self.step_pin, GPIO.LOW)
                time.sleep(0.001)  # Adjust as needed

            self.steps_to_move = 0  # Reset steps to move
            self.move_event.clear()  # Clear the event to indicate movement is done

    def start(self):
        self.move_thread.start()

    def stop(self):
        self.move_thread.join()

    def cleanup(self):
        self.stop()
        GPIO.cleanup()
