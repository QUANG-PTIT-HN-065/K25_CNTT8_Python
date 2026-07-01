from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    def __init__(self):
        self.__odometer = 0

    @property
    def odometer(self):
        return self.__odometer

    @abstractmethod
    def calculate_efficiency(self):
        pass

    def drive(self, distance):
        if distance <= 0:
            raise ValueError("Distance must be greater than 0!")

        self.__odometer += distance

    def __lt__(self, other):
        return self.odometer < other.odometer

    @staticmethod
    def validate_license_plate(plate:str):
        return len(plate) == 9 and plate.startswith("29")


class AutonomousFeature:
    def calculate_efficiency(self):
        return 95.0


class ElectricBus(BaseVehicle):
    def calculate_efficiency(self):
        efficiency = 100 - (self.odometer * 0.005)

        if efficiency < 50:
            return 50.0

        return efficiency


class RoboBus(ElectricBus, AutonomousFeature):
    def calculate_efficiency(self):
        electric = ElectricBus.calculate_efficiency(self)
        autonomous = AutonomousFeature.calculate_efficiency(self)

        return (electric + autonomous) / 2

