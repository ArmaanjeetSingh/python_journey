import tkinter as tk

class Scrollbox(tk.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)
        self.scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nse', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky,
                     rowspan=rowspan, columnspan=columnspan, **kwargs)

        self.scrollbar.grid(row=row, column=column+1, sticky='ns')
        self.config(yscrollcommand=self.scrollbar.set)