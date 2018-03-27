# Created by Alex Hurtado

import sqlite3


class Planner(object):
    """Defines a Planner class"""
    def __init__(self, db="planner.db"):
        self.db = db
        self.connected = None

    def open_connection(self, db):
        """Opens a database connection."""
        self.conn = sqlite3.connect(db)
        self.connected = True
        self.cur = self.conn.cursor()

    def close_connection(self):
        """Closes the connection to the database"""
        if self.check_connection():
            self.cur.close()
            self.conn.close()
            self.connected = False

    def check_connection(self):
        """Checks to see if a connection is open"""
        if self.connected:
            return True

        else:
            return False

    def make_db(self, db):
        """Makes a database, if it doesn't exist already"""
        self.open_connection()
        self.cur.execute('''CREATE TABLE events
                              (date text, events_name text)''')
        self.conn.commit()
        self.close_connection()

    def create_event(self, date, event):
        """Creates an event inside of a database"""
        self.open_connection(self.db)
        self.event = (event,)
        self.date = (date,)
        self.cur.execute('INSERT INTO events (date, events_name) VALUES (?, ?)', (event, date))
        self.conn.commit()
        self.close_connection()
