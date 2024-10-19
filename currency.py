import pprint
import requests
import json
from tkinter import *
from tkinter import messagebox as mb



window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Введите код валют').pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()