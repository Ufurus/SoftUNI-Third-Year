from project.id_mixin import IDMixin

class Trainer(IDMixin):

    def __init__(self, name: str):
        self.name = name
        self.id = IDMixin.get_next_id()
        self.increment_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"