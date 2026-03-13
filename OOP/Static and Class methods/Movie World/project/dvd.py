class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        date = date.split('.')
        month, creation_year = int(date[1]), int(date[2])
        months = {1: "January", 2: "February", 3: "March",
                  4: "April",   5: "May", 6: "June",
                  7: "July", 8: "August", 9: "September",
                  10: "October", 11: "November",12: "December"}
        creation_month = months[month]
        return cls(name, id, creation_year, creation_month, age_restriction)

    def __repr__(self):
        status = 'not rented' if not self.is_rented else 'rented'
        return (f"{self.id}: {self.name} ({self.creation_month}"
                f" {self.creation_year}) has age restriction {self.age_restriction}. Status: {status}")


