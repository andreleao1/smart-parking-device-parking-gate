import time
from PyQt5.QtCore import QThread, pyqtSignal
from src.infrastructure.sensor_rpi import RPiSensorService

class SensorThread(QThread):
    vehicle_detected = pyqtSignal(float)

    def __init__(self, threshold=2.0, interval=0.5, parent=None):
        super().__init__(parent)
        self.threshold = threshold
        self.interval = interval
        self._running = True
        self.sensor = RPiSensorService()

    def run(self):
        while self._running:
            try:
                distance = self.sensor.distance_meters()
                if distance < self.threshold:
                    self.vehicle_detected.emit(distance)
                    time.sleep(2)
            except Exception as e:
                print(f"Error reading sensor: {e}")
                self._running = False
            time.sleep(self.interval)

    def stop(self):
        self._running = False
        self.quit()
        self.wait()