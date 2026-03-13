from project.customer import Customer
from project.dvd import DVD

class MovieWorld:

    def __init__(self, name: str):
        self.name = name
        self.customers: list = []
        self.dvds: list = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        capacity = MovieWorld.customer_capacity()
        if len(self.customers) < capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        capacity = MovieWorld.dvd_capacity()
        if len(self.dvds) < capacity:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        curr_dvd = next((x for x in self.dvds if x.id == dvd_id), None)
        curr_customer = next((x for x in self.customers if x.id == customer_id), None)

        if curr_dvd in curr_customer.rented_dvds:
            return f"{curr_customer.name} has already rented {curr_dvd.name}"

        if curr_dvd.is_rented:
            return f"DVD is already rented"

        if curr_dvd.age_restriction > curr_customer.age:
            return f"{curr_customer.name} should be at least {curr_dvd.age_restriction} to rent this movie"

        curr_customer.rented_dvds.append(curr_dvd)
        curr_dvd.is_rented = True
        return f"{curr_customer.name} has successfully rented {curr_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        curr_dvd = next((x for x in self.dvds if x.id == dvd_id), None)
        curr_customer = next((x for x in self.customers if x.id == customer_id), None)

        if curr_dvd in curr_customer.rented_dvds:
            curr_customer.rented_dvds.remove(curr_dvd)
            curr_dvd.is_rented = False
            return f"{curr_customer.name} has successfully returned {curr_dvd.name}"
        return f"{curr_customer.name} does not have that DVD"

    def __repr__(self):
        customers = [x for x in self.customers]
        dvds = [x for x in self.dvds]

        final_result = []
        final_result.extend(customers)
        final_result.extend(dvds)
        return '\n'.join(map(str, final_result))