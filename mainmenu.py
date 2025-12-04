# In mainmenu.py
@staticmethod
def _argstrip(function, *args):
    return function()

#def _bind_accelerators(self):
    # ...
 #   self.bind_all(key, partial(self._argstrip, command))

def _bind_accelerators(self):
    keybinds = self.get_keybinds()
    for key, command in keybinds.items():
        # Use lambda to discard the event argument passed by Tkinter
        self.bind_all(
            key,
            lambda event, cmd=command: cmd()
        )
# Remove _argstrip static method
