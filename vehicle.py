from abc import ABC
class Vehicle(ABC):
    def __init__(self,veichle_type,licene_plate,rate):
        self.vehicle_type=veichle_type
        self.licence_plate=licene_plate
        self.rate=rate

class Car