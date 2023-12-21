def read_int(prompt, min_number, max_number):
    number = None
    while number is None:
        try:
            number = int(input(f'{prompt} >'))
            if min_number < number > max_number:
                print (f'Gib eine Zahl von {min_number} bis {max_number} ein')
                number = None
        except ValueError:
            print (f'Keine gültige Lottozahl')

    return number

def read_float(prompt, min_number, max_number):
    number = None
    while number is None:
        try:
            number = float(input(f'{prompt} >'))
            if min_number < number > max_number:
                print (f'Gib eine Zahl von {min_number} bis {max_number} ein')
                number = None
        except ValueError:
            print (f'Keine gültige Zahl')

    return number


if __name__ == '__main__':
    pass
