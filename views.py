# In views.py, DataRecordForm.__init__
# ... this creates N x M labels, where N is records, M is columns
for y in records:
    row_cnt = row_cnt + 1
    i = 0
    for z in y:
        i = i + 1
        lab = ttk.Label(self,text=z)
        lab.grid(row=row_cnt, column=i,  sticky='NSEW')

# Refactored views.py (DataRecordForm.__init__)

class DataRecordForm(tk.Frame):
    def __init__(self, parent, fields, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        # We only need one set of labels and entry fields for a single record.
        self.inputs = {}
        for idx, name in enumerate(fields):
            # 1. Create Label
            lbl = ttk.Label(self, text=name.title() + ":")
            lbl.grid(row=idx, column=0, sticky='W', padx=5, pady=2)
            
            # 2. Create Input Widget (e.g., a simple Entry)
            var = tk.StringVar()
            entry = ttk.Entry(self, textvariable=var, width=50)
            entry.grid(row=idx, column=1, sticky='EW', padx=5, pady=2)
            
            # Store the input variable for later retrieval/setting of data
            self.inputs[name] = var
            
        # *** REMOVE all code that iterates over 'records' to create a table display ***
        # The records table display is now only handled by DbRecList (Treeview).

    def load_record(self, record_data):
        """Method to load a single record into the form's input fields."""
        for name, value in record_data.items():
            if name in self.inputs:
                self.inputs[name].set(value)


# Refactored views.py (DbRecList)

class DbRecList(ttk.Treeview):
    # ... (init method remains similar)
    
    def update_data(self, field_names, records):
        """Clears old data and loads new data efficiently."""
        
        # 1. Clear existing columns/data
        self.delete(*self.get_children())
        
        # 2. Configure new columns (more efficient to do this once)
        self['columns'] = field_names
        self['show'] = 'headings'
        
        for col_name in field_names:
            self.heading(col_name, text=col_name.title())
            self.column(col_name, width=100) # Default width

        # 3. Insert new records
        for record in records:
            # record is a tuple of values
            self.insert('', 'end', values=record)
