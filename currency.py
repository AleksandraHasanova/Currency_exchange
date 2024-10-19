import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


currency = { 'EUR': 'Евро',
        'RUB': 'Российский рубль',
        'GBP': 'Британский фунт стерлингов',
        'JPE': 'Японская йена',
        'CNY': 'Китайская юань',
        'KZT': 'Казахский тенге',
        'UZS': 'Узбекский сум',
        'CHF': 'Швейцарский франк',
        'AED': 'Дирхан ОАЭ',
        'CAD': 'Канадский доллар',
        'EGP': 'Египетский фунт'
}
def exchange():
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                c_name = currency[code]
                mb.showinfo('Курс обмена',f'Курс: {exchange_rate:.2f} {c_name} за 1$')
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Внимание!','Введите код валюты')

def update_currency_label(event):
    code = combobox.get()
    name = currency[code]
    currency_label.config(text=name)

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')

Label(text='Выберите код валюты').pack(padx=10, pady=10)

combobox = ttk.Combobox(value=list(currency.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind('<<ComboboxSelected>>', update_currency_label)

currency_label = ttk.Label()
currency_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()