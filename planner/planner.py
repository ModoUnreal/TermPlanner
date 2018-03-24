# Created by Alex Hurtado
import sqlite3
import os
import os.path


# Check to see if .db file exists
if not os.path.isfile("planner.db"):
    DIRECTORY = os.path.dirname(os.path.realpath("planner.py"))
    DATABASE = os.path.join(DIRECTORY + '\\' + 'planner.db')


def connect_db():
    """Connects to the specific database"""
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


def close_connection(connection):
    conn.close()

def create_event(date, event):
    """Creates an event inside of a database..."""
    pass

def show_events(db):
    """Takes event from the database and lists them"""
    pass

def show_current_event(db):
    """Will show any events occuring today"""
    pass

def show_specific_day(db, date):
    """Shows the events listed for a specific date."""
    pass
