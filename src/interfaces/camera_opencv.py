import cv2

from src.interfaces.camera_service import CameraService


class OpenCVCameraService(CameraService):

    def __init__(self, device_index: int = 0):
        self.device_index = device_index

        def capture(self, output_path: str) -> None:
            cap = cv2.VideoCapture(self.device_index)

            if not cap.isOpened():
                cap.release()
                raise RuntimeError(f'Could not open camera (device {self.device_index})')

            ret, frame = cap.read()
            cap.release()

            if not ret:
                raise RuntimeError('Failed to capture image from camera')

            cv2.imWrite(output_path, frame)