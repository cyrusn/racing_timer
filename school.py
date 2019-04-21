from enum import Enum


class School(Enum):
    A = "Tsuen Wan Public Ho Chuen Yiu Memorial Primary School"
    B = "Salesian Yip Hon Primary School"
    C = "S.K.H. Chu Oi Primary School"
    D = "S.K.H. Chu Oi Primary School (Lei Muk Shue) "

    def __repr__(self):
        return "({}): {}".format(self.name, self.value)

    @classmethod
    def printList(cls):
        for school in cls:
            print(repr(school))

    @classmethod
    def getName(self, code):
        if code is None:
            return ""
        return School[code.upper()].value


if __name__ == "__main__":
    School.printList()

    print(School.getName("A"))
