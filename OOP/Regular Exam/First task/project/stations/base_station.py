from abc import ABC, abstractmethod
from project.astronauts.base_astronaut import BaseAstronaut
from string import ascii_letters, digits

class BaseStation(ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.astronauts: list = [BaseAstronaut]

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        for letter in value:
            if letter not in ascii_letters + digits and letter != '-':
                raise ValueError(f"Station names can contain only letters, numbers, and hyphens!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("A station cannot have a negative capacity!")
        self.__capacity = value

    def calculate_total_salaries(self):
        total_sum = 0
        for astronaut in self.astronauts:
            total_sum += astronaut.salary
        return f'{total_sum:.2f}'

    def status(self):
        total_astronauts = sorted([x.id_number for x in self.astronauts])
        if len(total_astronauts) == 0:
            total_astronauts = 'N/A'
            return f"Station name: {self.name}; Astronauts: {total_astronauts}; Total salaries: {self.calculate_total_salaries()}"
        return f"Station name: {self.name}; Astronauts: {' #'.join(x for x in total_astronauts)}; Total salaries: {self.calculate_total_salaries()}"

    @abstractmethod
    def update_salaries(self, min_value: float):
        pass
