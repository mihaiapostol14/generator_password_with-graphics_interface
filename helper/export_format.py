import csv
import json
import os

import openpyxl
from tkinter.messagebox import showinfo

output_path = os.path.join('C:', 'Users', os.getlogin(), 'Downloads')

class ExportFormat:
    def open_output(self,file_path=output_path):
        os.startfile(file_path)

    def export_message(self,filename: str = '', file_path=None):
        # todo: This function is for information user about successful export file

        for file in os.listdir(file_path):
            if os.path.exists(file.startswith('yours_password')):
                return showinfo('Message', f'file with name {filename} is export with successful'.upper())

    def export_text_file(self,password: str = ''):  # todo: this function  is for creating text file
        with open(file=f'{output_path}/yours_password.txt', mode='w') as file:
            file.write(password)
            return self.export_message(filename=file.name)

    def export_json_file(self,dictionary: dict):  # todo: this function  is for creating json file
        with open(file=f'{self,output_path}/yours_password.json', mode='w') as file:
            json.dump(dictionary, file, indent=4)
            return self.export_message(filename=file.name, file_path=output_path)

    def export_excel_file(self,dictionary: dict):  # todo: this function  is for creating Excel file
        book = openpyxl.Workbook()
        sheet = book.active

        sheet['A1'] = 'DATA AND TIME'
        sheet['B1'] = 'PASSWORD'
        row = 2

        for key, value in dictionary.items():
            sheet[row][0].value = key
            sheet[row][1].value = value
            row += 1

        book.save(f'{output_path}/yours_password.xlsx')

        return self.export_message(filename='yours_password.xlsx', file_path=output_path)

    def export_csv_file(self,date_time: str = '', password: str = ''):  # todo: this function  is for creating csv file
        with open(file=f'{output_path}/yours_password.csv', mode='w') as file:
            writer = csv.writer(file)
            writer.writerows([
                ('DATA AND TIME', 'PASSWORD'),
                [date_time, password]
            ])
            return self.export_message(filename=file.name, file_path=output_path)
