import sys
from pympler import asizeof
from typing import Union


class Student:

    def __init__(self, name: str = 'Ivan', age: int = 18, groupNum: str = '10A'):
        """
        :param name:
        :param age:
        :param groupNum:
        """
        self.name = name
        self.age = age
        self.groupNum = groupNum

    def __repr__(self):
        return f'Name: {self.name}; Age: {self.age}; GroupNum: {self.groupNum}'

    def getName(self) -> str:
        return self.name

    def getAge(self) -> int:
        return self.age

    def getGroupNum(self) -> Union[str, int]:
        return self.groupNum

    def setName(self, new_name: str) -> str:
        self.name = new_name
        return self.name

    def setAge(self, new_age: int) -> int:
        self.age = new_age
        return self.age


if __name__ == '__main__':
    student_1 = Student()
    student_2 = Student('Peter', 22, '11Z')
    student_3 = Student('Tom', 15, '8J')
    print(student_2.getName(), student_2.getAge())
    print(id(student_2))
    print(student_2.__dict__)
    Student.setAge(student_2, 17)
    print(student_2.getName(), student_2.getAge())
    print(id(student_2))
    print(student_2.__dict__)
    print(asizeof.asizeof(student_2))
    print(asizeof.asizeof(student_3))
    print(asizeof.asizeof(student_1))
