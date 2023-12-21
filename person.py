from dataclasses import dataclass


@dataclass
class Person:
    """
    A person playing the lottery
    """
    name: str
    password: str
    balance: float


if __name__ == '__main__':
    # used for testing
    person = Person('Hans', 'test', 25.75)
    print (person)
