from tkinter.messagebox import showinfo

from pyperclip import copy


def copy_password(password: str = ''):
    # todo: This function is for copy password in clipboard
    copy(password)
    return showinfo('Message', 'Yours password successful copy'.upper())



