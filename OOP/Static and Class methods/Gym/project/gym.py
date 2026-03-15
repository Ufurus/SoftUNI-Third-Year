from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer

class Gym:

    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    @staticmethod
    def __add_obj(obj, col):
        if obj not in col:
            col.append(obj)

    def add_customer(self, customer: Customer):
        self.__add_obj(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_obj(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_obj(equipment, self.equipment)

    def add_plan(self, plans: ExercisePlan):
        self.__add_obj(plans, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_obj(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        curr_sub = next((x for x in self.subscriptions if x.id == subscription_id), None)
        curr_customer = next((x for x in self.customers if x.id == subscription_id), None)
        curr_trainer = next((x for x in self.trainers if x.id == subscription_id), None)
        curr_equipment = next((x for x in self.equipment if x.id == subscription_id), None)
        curr_plan = next((x for x in self.plans if x.id == subscription_id), None)
        final_result = []
        final_result.append(curr_sub); final_result.append(curr_customer);
        final_result.append(curr_trainer); final_result.append(curr_equipment); final_result.append(curr_plan)
        return '\n'.join(map(str, final_result))