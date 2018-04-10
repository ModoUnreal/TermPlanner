# Created by Alex Hurtado
# Used to sort dates in the database
import datetime


def find_years(date):
    """Used to find the year within the string."""
    date_length = len(date)
    if date[date_length - 4:].find('.') == -1:
        year = date[date_length - 4:]

    elif date[date_length - 4].find('.') != -1 and date_length != 10:
        year = date[:date_length - 7]

    else:
        year = date[:date_length - 6]

    return year

def find_days(date):
    """Used to find the days in a date string."""
    date_length = len(date)
    if date[date_length - 3:].find('.') == -1:
        if date_length == 8:
            day = date[:date_length - 7]
        elif date_length == 10:
            day = date[:date_length - 8]

    elif date[:date_length - 7].find('.') != 0:
        day = date[date_length - 2:]

    return day
