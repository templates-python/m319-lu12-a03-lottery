from person import Person


def login():
    people = load_people()
    password = input('Passwort > ')
    for person in people:
        if password == person.password:
            return person

    return None


def load_people():
    """
    loads the list of people
    :return: list of person-objects
    """
    people_list = list()
    people_list.append(Person('Inga', 'geheim', 14.00))
    people_list.append(Person('Peter', 'secrät', 7.00))
    people_list.append(Person('Beatrice', 'passWORT', 23.00))
    return people_list


if __name__ == '__main__':
    person = login()
    assert person is None
