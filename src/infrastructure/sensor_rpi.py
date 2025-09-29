import RPi.GPIO as GPIO
import time

from src.infrastructure.sensor_service import SensorService


class RPiSensorService(SensorService):
    def __init__(self, trig_pin: int = 23, echo_pin: int = 24):
        self.trig = trig_pin
        self.echo = echo_pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)
        GPIO.output(self.trig, False)
        time.sleep(2)

    def distance_meters(self) -> float:
        global stop, start

        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)

        while GPIO.input(self.echo) == 0:
            start = time.time()
        while GPIO.input(self.echo) == 1:
            stop = time.time()

        elapsed = stop - start
        distance_cm = (elapsed * 34300) / 2
        return distance_cm / 100.0

    def __del__(self):
        GPIO.cleanup()