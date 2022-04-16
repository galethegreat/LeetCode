import random

class RandomizedSet:

    def __init__(self):
        self.dict = dict()

        self.arr = []

    def insert(self, val: int) -> bool:

        if val in self.dict:
            return False

        self.dict[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.dict:

            index_to_remove = self.dict[val]

            self.arr[index_to_remove], self.arr[-1] = self.arr[-1], self.arr[index_to_remove]
            self.dict[self.arr[index_to_remove]] = index_to_remove
            self.arr.pop()


            del(self.dict[val])

            return True

        return False

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.arr) - 1)
        return self.arr[random_index]
