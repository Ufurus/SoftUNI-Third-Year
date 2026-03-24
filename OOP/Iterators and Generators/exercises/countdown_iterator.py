class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.counter = 0
        self.end = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.end:
            self.i = self.count
            self.count -= 1
            self.counter += 1
            return self.i
        else:
            raise StopIteration()

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
