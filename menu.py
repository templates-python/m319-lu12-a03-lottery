def show_menu():
    print('Lotto\n' +
          '---------\n' +
          'A) Konto Ein- und Auszahlungen tätigen\n' +
          'B) Lottotipps abgeben\n' +
          'Z) Beenden')


def select_menu():
    choice = None
    while choice is None:
        choice = input('Auswahl (A/B/C/Z) > ')
        if choice not in 'AaBbCcZz':
            print('Ungültige Auswahl')
            choice = None

    return choice


if __name__ == '__main__':
    pass
