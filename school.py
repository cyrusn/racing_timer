from enum import Enum


class School(Enum):
    A = "Tsuen Wan Public Ho Chuen Yiu Memorial Primary School"
    B = "Salesian Yip Hon Primary School"
    C = "S.K.H. Chu Oi Primary School"
    D = "S.K.H. Chu Oi Primary School (Lei Muk Shue) "

    def __str__(self):
        return "({}): {}".format(self.name, self.value)

    @classmethod
    def printList(cls):
        [print(school) for school in cls]

    @classmethod
    def getName(self, code):
        return School[code.upper()].value if code is not None else ""


if __name__ == "__main__":
    print(School.getName("A"))
    print(School.getName(None))
    School.printList()
