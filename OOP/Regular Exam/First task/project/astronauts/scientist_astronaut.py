from project.astronauts.base_astronaut import BaseAstronaut

class ScientistAstronaut(BaseAstronaut):

    def __init__(self, id_number: str, salary: float, specialization: str):
        super().__init__(id_number, salary, specialization, stamina=70)
        self.specialization = 'ScientistAstronaut'
        self.stamina = 70

    def train(self):
        if self.stamina + 3 >= 100:
            self.stamina = 100
        else:
            self.stamina += 3