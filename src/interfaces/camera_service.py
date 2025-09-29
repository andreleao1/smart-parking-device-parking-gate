from abc import ABC, abstractmethod


class CameraService(ABC):

    @abstractmethod
    def capture(self, output_path: str) -> None:
        raise NotImplementedError