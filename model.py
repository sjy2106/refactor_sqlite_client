def get_table_info(self, tblname):
    # Cache the result if you query it often
    self.cursor.execute("PRAGMA table_info({tb})".format(tb=tblname))
    return self.cursor.fetchall()

def get_field_names(self, tblname):
    data = self.get_table_info(tblname)
    # Efficiently extract names using a list comprehension
    return [row[1] for row in data]

# Refactored models.py (in SQLModel.insert_record)

def insert_record(self, tblname, values):
    """Inserts a new record using parameterized queries."""
    
    # 1. Get column names and prepare placeholders (e.g., ?, ?, ?)
    field_names = self.get_field_names(tblname)
    placeholders = ', '.join(['?'] * len(field_names)) 
    
    # 2. Build the query string
    sql = "INSERT INTO {tb} ({fields}) VALUES ({ph})".format(
        tb=tblname,
        fields=', '.join(field_names),
        ph=placeholders
    )
    
    # 3. Execute with the client context manager and pass values as a tuple
    with SQLClient(self.dbname) as cursor:
        cursor.execute(sql, tuple(values)) 
    # Commit/Close is handled by SQLClient.__exit__
