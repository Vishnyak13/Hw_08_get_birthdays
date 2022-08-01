from datetime import datetime, timedelta


def get_employees(path):
    with open(path, 'r', encoding='utf-8') as file:
        users = []
        line = file.readline()
        while True:
            data = line.removesuffix('\n').split(',')
            users.append({'Name': data[0], 'Birthday': data[1]})
            line = file.readline()
            if not line:
                break
    return users


print(get_employees('employees_list.txt'))


def get_birthdays_per_week(users):
    data = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }
    current_date = datetime.now()
    users = get_employees('employees_list.txt')
    for el in users:
        birthday = datetime.strptime(el.get('Birthday'), '%d.%m.%Y')
        system_birthday = birthday.replace(year=current_date.year)
        diff = system_birthday.date() - current_date.date()
        if timedelta(0) <= diff <= timedelta(7):
            weekday = datetime.weekday(system_birthday)
            if weekday == 0 or weekday == 5 or weekday == 6:
                data['Monday'] = data['Monday'] + el['Name'] + ', '
            if weekday == 1:
                data['Tuesday'] = data['Tuesday'] + el['Name'] + ', '
            if weekday == 2:
                data['Wednesday'] = data['Wednesday'] + el['Name'] + ', '
            if weekday == 3:
                data['Thursday'] = data['Thursday'] + el['Name'] + ', '
            if weekday == 4:
                data['Friday'] = data['Friday'] + el['Name'] + ', '

    for key, value in data.items():
        if len(value) != 0:
            print(f'{key}: {value[:-2]}')


if __name__ == '__main__':
    get_birthdays_per_week(get_employees('employees_list.txt'))
