from enum import Enum


class SchoolName(Enum):
    A = "Tsuen Wan Public Ho Chuen Yiu Memorial Primary School"
    B = "Salesian Yip Hon Primary School"
    C = "S.K.H. Chu Oi Primary School"
    D = "S.K.H. Chu Oi Primary School (Lei Muk Shue) "

    @classmethod
    def printSchoolList(self):
        for name, member in SchoolName.__members__.items():
            print("({}): {}".format(name, member.value))

    @classmethod
    def get(self, code):
        if code is None:
            return ""
        return SchoolName[code.upper()].value
