from project.stations.base_station import BaseStation

class MaintenanceStation(BaseStation):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.capacity = 3
        self.astronauts = []

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.specialization == "EngineerAstronaut":
                if astronaut.salary <= min_value:
                    astronaut.salary += 3000