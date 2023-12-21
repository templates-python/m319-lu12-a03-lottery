from numeric_input import read_float


def transfer_money(person):
    choice = ' '
    while choice not in 'Zz':
        print(f'Guthaben: {person.balance}')
        choice = input('Auswahl > ')
        if choice in 'Aa':
            amount = read_float('Auszahlung', 10, 20)
            person.balance -= amount
        if choice in 'Ee':
            amount = read_float('Einzahlung', 10, 20)
            person.balance += amount


def select_transaction():
    transaction = None
    while transaction is None:
        transaction = input('Auswahl (A/E/Z) >')
        if transaction not in ['A', 'a', 'E', 'e', 'Z', 'z']:
            transaction = None
            print('Keine gültige Auswahl')

    return transaction


if __name__ == '__main__':
    pass
