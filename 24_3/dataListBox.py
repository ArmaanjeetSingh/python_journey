import tkinter as tk
from scrollbox import Scrollbox

class DataListBox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.cursor = connection.cursor()
        self.table = table
        self.field = field

        self.sql_select = f"SELECT {self.field}, _id FROM {self.table}"

        if sort_order:
            self.sql_order = " ORDER BY " + ",".join(sort_order)
        else:
            self.sql_order = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tk.END)

    def requery(self):
        print(self.sql_select + self.sql_order)
        self.cursor.execute(self.sql_select + self.sql_order)

        self.clear()
        for val in self.cursor:
            self.insert(tk.END, val[0])