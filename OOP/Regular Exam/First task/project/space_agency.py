from project.astronauts.base_astronaut import BaseAstronaut
from project.stations.base_station import BaseStation
from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation

class SpaceAgency:

    def __init__(self):
        self.astronauts: list[BaseAstronaut] = []
        self.stations: list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):

        astronaut_types = {
            "EngineerAstronaut": EngineerAstronaut,
            "ScientistAstronaut": ScientistAstronaut,
        }

        if astronaut_type not in astronaut_types:
            raise ValueError(f"Invalid astronaut type!")

        if any(astro.id_number == astronaut_id_number for astro in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        astro = astronaut_types[astronaut_type](astronaut_id_number, astronaut_salary, astronaut_type)
        self.astronauts.append(astro)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    # @staticmethod
    def add_station(self,station_type: str, station_name: str):

        station_types = {
            "ResearchStation": ResearchStation,
            "MaintenanceStation": MaintenanceStation,
        }

        if station_type not in station_types:
            raise ValueError(f"Invalid station type!")

        if any(station.name == station_name for station in self.stations):
            raise ValueError(f"{station_name} has been already added!")

        station = station_types[station_type](station_name, capacity=0)
        self.stations.append(station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        current_station = next((x for x in self.stations if station_name == x.name), None)
        if current_station is None:
            raise ValueError(f"Station {station_name} does not exist!")

        current_astronaut = next((x for x in self.astronauts if astronaut_type == x.specialization), None)
        if current_astronaut is None:
            raise ValueError(f"No available astronauts of the type!")


        for station in self.stations:
            if station.name == current_station:
                if station.capacity < 0:
                    return "This station has no available capacity."

        self.astronauts.remove(current_astronaut)
        current_station.astronauts.append(current_astronaut)
        current_station.capacity -= 1
        return f"{current_astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        curr_station = station
        for astronaut in curr_station.astronauts:
            for i in range(sessions_number):
                astronaut.train()

        total_stamina = 0
        for astronaut in curr_station.astronauts:
            total_stamina += astronaut.stamina

        return f"{curr_station.name} astronauts have {total_stamina} total stamina after {sessions_number} training session/s."

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        curr_station = station
        curr_astronaut = next((x for x in curr_station.astronauts if x.id_number == astronaut_id_number), None)
        if curr_astronaut is None or curr_astronaut.stamina == 100:
            return f'The retirement process was canceled.'
        curr_station.astronauts.remove(curr_astronaut)
        curr_station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):

        all_agencies = []

        for station in self.stations:
                station.update_salaries(min_value)

        total_capacity = 0

        for station in self.stations:
            total_capacity += station.capacity

        all_agencies.append(f"*Space Agency Up-to-Date Report*")
        total_astronauts = 0
        for station in self.stations:
            total_astronauts += len(station.astronauts)
        all_agencies.append(f"Total number of available astronauts: {total_capacity - total_astronauts}")

        station_count = 0

        for station in self.stations:
            station_count += 1
        all_agencies.append(f"**Stations count: {station_count}; Total available capacity: {total_capacity}**")

        station_info = '\n'.join(x.status() for x in sorted(self.stations, key=lambda x: (-len(x.astronauts), x.name)))
        all_agencies.append(station_info)

        return f"\n".join(all_agencies)







