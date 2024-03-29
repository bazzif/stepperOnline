# Stepper Motor Control with Python

This Python script provides a simple interface for controlling stepper motors using the Raspberry Pi GPIO pins. Stepper motors are commonly used in various applications, including robotics, 3D printers, CNC machines, and automated systems. This script aims to simplify the process of controlling stepper motors, providing an easy-to-use Python class for managing stepper motor movements.

## Features

- Supports stepper motors with enable, direction, and step control pins.
- Allows setting the direction of rotation (clockwise or counterclockwise).
- Enables precise control over the number of steps to move.
- Uses non-blocking delays for smooth motor operation without blocking the main program.

## Requirements

- Raspberry Pi (or compatible single-board computer)
- Python 3.x
- RPi.GPIO library (for Raspberry Pi GPIO control)
- Stepper motor with compatible driver (e.g., A4988, DRV8825)

## Usage

1. **Wiring**: Connect your stepper motor to the Raspberry Pi GPIO pins. Ensure proper wiring of the enable, direction, and step control pins.

2. **Installation**: Install the RPi.GPIO library if not already installed. You can install it using pip:

    ```
    pip install RPi.GPIO
    ```

3. **Usage**: Import the `StepperMotor` class from the provided Python script and create an instance with the appropriate GPIO pins for your stepper motor. Then, you can set the direction and move the stepper motor as needed. Here's a basic example:

    ```python
    from stepper_motor import StepperMotor
    import time

    # Define GPIO pins
    enable_pin = 17
    direction_pin = 18
    step_pin = 27

    # Create a stepper motor instance
    stepper = StepperMotor(enable_pin, direction_pin, step_pin)

    try:
        while True:
            # Set direction and move 200 steps clockwise
            stepper.set_direction("clockwise")
            stepper.move(200)
            time.sleep(1)

            # Set direction and move 200 steps counterclockwise
            stepper.set_direction("counterclockwise")
            stepper.move(200)
            time.sleep(1)

    except KeyboardInterrupt:
        stepper.cleanup()
    ```

4. **Cleanup**: Ensure to call the `cleanup()` method of the `StepperMotor` instance when done to release GPIO resources properly.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request on GitHub.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
