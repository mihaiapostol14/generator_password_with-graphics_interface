from datetime import datetime

from customtkinter import (
    CTkToplevel,
    CTkEntry,
    CTkButton
)

from .export_format import ExportFormat
from .utils import copy_password

datetime_password = {}

now = datetime.now()  # todo: current date and time
date_and_time = now.strftime('%m/%d/%Y, %H:%M:%S')


class ToplevelWindow(CTkToplevel,ExportFormat):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.password = None
        self.label_password = None

        self.geometry('400x399')
        self.title('Export')
        self.resizable(False, False)

        # todo: here is a other window that apparent after generating password

    def show_password(self, *, password):  # todo: this method is showing password after generating it
        self.label_password = CTkEntry(
            width=400,
            master=self,
            fg_color='transparent',
            font=('Arial', 14)
        )
        self.label_password.insert(0, password)
        self.label_password.configure(state='disabled')
        self.label_password.grid(row=0, rowspan=2, columnspan=2, pady=0)

    def create_button(self, text: str = '', command=None):
        return CTkButton(master=self, text=text, command=command)

    def place_buttons(self):
        self.password = self.label_password.get()
        datetime_password.update({date_and_time: self.password})

        self.create_button(text='export password to text file',
                           command=lambda: self.export_text_file(password=self.password)).grid(padx=50, pady=10)

        self.create_button(text='export password to csv file',
                           command=lambda: self.export_csv_file(date_time=date_and_time, password=self.password)).grid(
            padx=50, pady=10)

        self.create_button(text='export password to excel file',
                           command=lambda: self.export_excel_file(dictionary=datetime_password)).grid(padx=50, pady=10)

        self.create_button(text='export password to json file',
                           command=lambda: self.export_json_file(dictionary=datetime_password)).grid(padx=50, pady=10)

        self.create_button(text='copy password',
                           command=lambda: copy_password(password=self.password)).grid(padx=50, pady=10)

        self.create_button(text='open directory with files',
                           command=self.open_output).grid(padx=50, pady=10)
