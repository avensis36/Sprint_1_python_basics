types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_duplicate(dictionary):
    for i in dictionary.keys():
        for j in range(i + 1, len(dictionary) + 1):
            dictionary[j] = list(set(dictionary[j]).difference(set(dictionary[i])))
    return dictionary

def tickets_by_type(types, tickets):
    upd_tickets = delete_duplicate(tickets)
    tickets_by_type = {}
    for i in range(1, len(upd_tickets) + 1):
        tickets_by_type[types[i]] = upd_tickets[i]
    return tickets_by_type