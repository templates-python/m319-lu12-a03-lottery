from authenticate import login
from lottery import create_ticket
from menu import select_menu
from money import transfer_money


def main():
    person = login()
    selection = ' '
    while person is not None and selection not in 'Zz':
        selection = select_menu()
        if selection in 'Aa':
            transfer_money(person)
        elif selection in 'Bb':
            create_ticket(person)



if __name__ == '__main__':
    main()
