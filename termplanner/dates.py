# Created by Alex Hurtado
# Used to sort dates in the database
import datetime


def find_years(date):
    """Used to find the year within the string."""
    date_length = len(date)
    if date[date_length - 4:].find('.') != 0:
        year = date[date_length - 4:]

    else:
        year = date[:date_length - 4]

    return year

def find_months(date):
    """Used to find the month in a date string."""
    pass
