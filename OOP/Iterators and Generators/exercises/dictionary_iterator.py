class dictionary_iter:

    def __init__(self, dictionary_object: dict):
        self.dict_tuple = tuple(dictionary_object.items())
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.dict_tuple) - 1:
            self.i += 1
            return self.dict_tuple[self.i]
        else:
            raise StopIteration()

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)