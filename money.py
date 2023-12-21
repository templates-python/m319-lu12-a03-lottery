def transfer_money():
    pass


def select_transaction():
    transaction = None
    while transaction is None:
        transaction = input('Auswahl (A/E/Z) >')
        if transaction not in ['A', 'a', 'E', 'e', 'Z', 'z']:
            transaction = None
            print ('Keine gültige Auswahl')

    return transaction


if __name__ == '__main__':
    pass
