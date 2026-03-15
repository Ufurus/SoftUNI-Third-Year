class Kitchen:

    def __init__(self, ingredients: list):
        self.ingredients = ingredients

    @classmethod
    def ham_sandwich(cls):
        return cls(['ham', 'tomato', 'mayonnaise', 'pickles'])

first_sandwich = Kitchen.ham_sandwich()
print(first_sandwich.ingredients)