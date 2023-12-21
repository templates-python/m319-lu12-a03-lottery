from numeric_input import read_int
from ticket import Ticket


def create_ticket(person):
    if person.balance >= 2.00:
        person.balance -= 2.00
        ticket = Ticket(list(), 0)
        select_numbers(ticket)
        print_ticket(ticket)
        print(f'Guthaben: {person.balance}')
    else:
        print('Dein Guthaben reicht nicht aus')


def select_numbers(ticket):
    count = 0
    while count < 5:
        number = read_int('Lottozahl', 1,42)
        if number in ticket.numbers:
            print ('Diese Zahl wurde schon gewählt')
        else:
            ticket.numbers.append(number)
            count+=1

    number = read_int('Jokerzahl', 1,6)
    ticket.joker = number


def print_ticket(ticket):
    for i in range(1,42):
        if i in ticket.numbers:
            print ('  X ','')
        else:
            print (i)
        if i % 6 == 0:
            print(' ')

    print (ticket.joker)


if __name__ == '__main__':
    pass
