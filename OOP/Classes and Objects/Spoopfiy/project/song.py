class Song:
    def __init__(self, name: str, length: float,single: bool):
        self.name = name
        self.single = single
        self.length = length

    def get_info(self):
        return f"{self.name} - {self.length}"