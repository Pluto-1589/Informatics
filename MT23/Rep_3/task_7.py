from datetime import date, datetime


def weekday_of(date_string):
    # The function should return the day of the week of the given date as an integer number between 1 (Monday) and 7 (Sunday).

    date_string = datetime.fromisoformat(date_string)

    return date.isoweekday(date_string)


print(weekday_of("1998-10-25"))
print(weekday_of("2001-01-01"))
print(weekday_of("1995-12-12"))
