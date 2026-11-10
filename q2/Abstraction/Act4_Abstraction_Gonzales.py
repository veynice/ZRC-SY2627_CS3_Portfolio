from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def get_reading(self):
        pass

    def display(self):
        print(f"[{self.name}] Reading: {self.get_reading()}")


class PHMeter(Sensor):

    def __init__(self):
        self.name = "pH Sensor"

    def get_reading(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):

    def __init__(self):
        self.name = "Temperature Sensor"

    def get_reading(self):
        return "24.5 °C"

class FeverSensor(TempSensor):
    def __init__(self):
        super().__init__()
        self.name = "Fever Sensor"

    def get_reading(self):
        return "38.5 °C (Fever Detected)"



print("---Lab Diagnosis System---")

lab_sensors = [PHMeter(), TempSensor(), FeverSensor()]

for sensor in lab_sensors:
    sensor.display()

print("-" * 23)