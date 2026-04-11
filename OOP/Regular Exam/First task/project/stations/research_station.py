from project.stations.base_station import BaseStation

class ResearchStation(BaseStation):

    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.capacity = 5
        self.astronauts = []

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.specialization == "ScientistAstronaut":
                if astronaut.salary <= min_value:
                    astronaut.salary += 5000