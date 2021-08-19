import colorsys
import json
import math
import tkinter as tk
from tkinter import ttk, messagebox, RAISED, Tk
import logic

class form:
    # initialization controls
    def __init__(self):
        self.window = Tk()
        self.from_coin = self.init_from_coin()
        self.to_coin = self.init_to_coin()
        self.sum = self.init_sum()
        self.calc = self.init_calc()
        self.cur_date = f'Date: {logic.select_date()}'
        self.result, self.result_text = None, None
        self.details_label, self.details_text = self.init_details_label()
        self.window.geometry('1000x500')
        self.window.mainloop()

    # design
    def design(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCombobox", fieldbackground="orange", background="white")
        self.window.option_add('*TCombobox*Listbox*Foreground', 'orange')
        self.window.option_add('*TCombobox*Listbox*selectBackground', 'orange')

    # control of comobox
    def init_from_coin(self):
        label = tk.Label(self.window, width=15, text='convert from: ', relief=RAISED, font='Calibri 11', border=0, bg="white", fg="orange")
        label.grid(column=10, row=2)
        como = ttk.Combobox(self.window, width=15, textvariable=tk.StringVar(), font= 'Calibri 11')
        como['values'] = logic.select_coins()
        # הוספה לחלון
        como.grid(column=10, row=3)
        como.current(0)
        self.design()
        return como

    # control of comobox
    def init_to_coin(self):
        label = tk.Label(self.window, width=15, text='to: ', relief=RAISED, font='Calibri 11', border=0, bg="white", fg="orange")
        label.grid(column=20, row=2)
        como = ttk.Combobox(self.window, width=15, textvariable=tk.StringVar(), font= 'Calibri 11')
        como['values'] = logic.select_coins()
        # הוספה לחלון
        como.grid(column=20, row=3)
        como.current(0)
        return como

    # control of spinbox
    def init_sum(self):
        iv = tk.IntVar()
        spin = tk.Spinbox(self.window, width=15, from_=1, to=1000000, textvariable = iv, font= 'Calibri 11', bg="white", fg="orange", border=0)
        spin.grid(column=10, row=4)
        return spin

    # control of button to clac the conversion
    def init_calc(self):
        button = tk.Button(self.window, text="calc", command=self.calc_sum, font='Calibri 11', border=0, bg="white", fg="orange")
        button.grid(column=15, row=3)
        return button

    # label to show details of conversion
    def init_details_label(self):
        details_text = tk.StringVar()
        label = tk.Label(self.window, textvariable=details_text, relief=RAISED, font= 'Calibri 11', bg="white", fg="orange")
        details_text.set(self.cur_date)
        label.grid(column=15, row=0)
        return label, details_text

    # label to show the result of the conversion
    def init_result(self, result):
        result_text = tk.StringVar()
        label = tk.Label(self.window,width=15, textvariable=result_text, relief=RAISED, font= 'Calibri 11', bg="white", fg="orange", border=0)
        label.grid(column=20, row=4)
        result_text.set(result)
        return label, result_text

    # The function send to functions that calculating the conversion.
    # the function presenting the result in the forum
    def calc_sum(self):
        result = logic.calc_convert(self.from_coin.get(), self.to_coin.get(), self.sum.get())
        if result == 'not valid sum':
            label = tk.Label(self.window, width=20, text='not valid sum', relief=RAISED, font='Calibri 13', border=0,
                             bg="white", fg="orange")
            label.grid(row=4)
        elif result:
            self.result, self.result_text = self.init_result(round(result, 3))
            self.details_text.set(f'{self.sum.get()} {self.from_coin.get()} = {result} {self.to_coin.get()}'
                                  f'\n {self.cur_date}')
        else:
            label = tk.Label(self.window, width=20, text='coin not exist', relief=RAISED, font='Calibri 13', border=0,bg="white", fg="orange")
            label.grid(row=11)






