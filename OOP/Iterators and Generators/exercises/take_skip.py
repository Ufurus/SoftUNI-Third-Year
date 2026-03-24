class take_skip:
        def __init__(self, step: int, count: int):
            self.step = step
            self.count = count
            self.number = 0
            self.counter = 0

        def __iter__(self):
            return self

        def __next__(self):
             if self.counter <= 0:
                 self.counter += 1
                 return 0
             elif self.counter < self.count:
                 self.number += self.step
                 self.counter += 1
                 return self.number
             else:
                 raise StopIteration

numbers = take_skip(2, 6)
for number in numbers:
    print(number)