# Created by Alex Hurtado
import sqlite3
import os
import os.path

if not os.path.isfile("planner.db"):
    DIRECTORY = os.path.dirname(os.path.realpath("setup.py"))
    DATABASE = os.path.join(DIRECTORY + '\\' + 'planner.db')

def get_db():
    """Opens a database connection if there is none yet for the current
    application context."""
    pass

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
