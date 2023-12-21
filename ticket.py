from dataclasses import dataclass


@dataclass
class Ticket:
    """
    A lottery ticket with a list of numbers and the joker
    """
    numbers: list
    joker: int


if __name__ == '__main__':
    my_numbers = [1,17,8,32]
    ticket = Ticket(my_numbers, 7)
    assert 17 in ticket.numbers
    assert ticket.joker == 7
