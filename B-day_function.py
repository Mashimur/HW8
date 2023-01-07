from collections import defaultdict
from datetime import datetime, timedelta

days_of_week = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя"
}

def get_birthdays_per_week(users, meantime=7):
    actual_date = datetime.now()
    actual_date = actual_date.date()
    end_date = actual_date + timedelta(days=meantime)
    dictionary = defaultdict(list)
    for person in users:
        for name, birthday in person.items():
            current_b_day = birthday.strftime('%y %m %d').split()
            current_b_day[0] = str(actual_date.year)
            current_b_day = " ".join(current_b_day)
            birthday = datetime.strptime(current_b_day, '%Y %m %d').date()
            if actual_date <= birthday < end_date:
                week_day = birthday.weekday()
                if week_day not in (5, 6):
                    dictionary[birthday].append(name)
                elif week_day == 5:
                    dictionary[birthday + timedelta(days=2)].append(name)
                elif week_day == 6:
                    dictionary[birthday + timedelta(days=1)].append(name)
            else:
                continue

    sorted_list = sorted(dictionary)
    for day in sorted_list:
        sorted_list = ", ".join(dictionary[day])
        print(f"{days_of_week[day.weekday()]}: {sorted_list}")
    if len(dictionary) == 0:
        print("Дні народження відсутні!")


if __name__ == "__main__":
    print("\n\t\t\t\tДні народженя\n")
    b_days_list = [
        {"Оксана": datetime(1973, 1, 8)},
        {"Олег": datetime(2003, 1, 9)},
        {"Софія": datetime(1978, 1, 8)},
        {"Олександр": datetime(1973, 1, 12)},
        {"Марія": datetime(1999, 1, 15)},
        {"Артем": datetime(1956, 1, 14)},
        {"Владислав": datetime(1983, 1, 10)},
        {"Анастасія": datetime(2005, 1, 12)},
        {"Христина": datetime(2007, 1, 13)},
        {"Богдан": datetime(1989, 1, 12)},
        {"Микита": datetime(1991, 1, 9)},
        {"Світлана": datetime(1996, 1, 14)},
        {"Дарія": datetime(2001, 1, 15)},
        {"Олена": datetime(2002, 1, 11)},
        {"Євген": datetime(1985, 1, 7)}
    ]

    get_birthdays_per_week(b_days_list, 7)
