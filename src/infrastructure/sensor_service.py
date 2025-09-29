from abc import ABC, abstractmethod


class SensorService(ABC):

    @abstractmethod
    def distance_meters(self) -> float:
        raise NotImplementedError