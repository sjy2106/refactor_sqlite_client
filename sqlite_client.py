# Refactored sqlite_client.py

import sqlite3

class SQLClient:
    """A context manager for SQLite connection management."""
    
    def __init__(self, dbname='records.db'):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def __enter__(self):
        # Open the connection when entering the 'with' block
        self.conn = sqlite3.connect(self.dbname)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Commit and close the connection when exiting the 'with' block
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback() # Rollback on error
        self.conn.close()

# The SQLModel now uses the client context manager for all operations.
