from person import Person


def login():
    pass


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
    pass
