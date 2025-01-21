from datetime import date


def weekday_of(date_string):

    date_string = date.fromisoformat(date_string)

    return date.isoweekday(date_string)


print(weekday_of("1998-10-25"))
print(weekday_of("2001-01-01"))
print(weekday_of("1995-12-12"))
