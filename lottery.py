def create_ticket():
    pass


def select_numbers():
    pass


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
