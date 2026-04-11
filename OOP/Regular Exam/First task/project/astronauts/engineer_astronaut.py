from project.astronauts.base_astronaut import BaseAstronaut

class EngineerAstronaut(BaseAstronaut):

    def __init__(self, id_number: str, salary: float, specialization: str):
        super().__init__(id_number, salary, specialization, stamina=80)
        self.specialization = 'EngineerAstronaut'
        self.stamina = 80

    def train(self):
        if self.stamina + 5 >= 100:
            self.stamina = 100
        else:
            self.stamina += 5