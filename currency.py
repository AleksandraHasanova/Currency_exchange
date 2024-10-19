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
        'EGP': 'Египетский фунт',
        'USD': 'Доллар США'
}
def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/'+b_code)
            response.raise_for_status()
            data = response.json()
            if t_code in data["rates"]:
                exchange_rate = data["rates"][t_code]
                t_name = currency[t_code]
                b_name = currency[b_code]
                mb.showinfo('Курс обмена',f'Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}')
            else:
                mb.showerror('Ошибка', f'Валюта {t_code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Внимание!','Введите код валюты')

def update_t_currency_label(event):
    t_code = t_combobox.get()
    t_name = currency[t_code]
    t_currency_label.config(text=t_name)

def update_b_currency_label(event):
    b_code = b_combobox.get()
    b_name = currency[b_code]
    b_currency_label.config(text=b_name)

window = Tk()
window.title('Курсы обмена валют')
window.geometry('360x350')

Label(text='Базовая валюта').pack(padx=10, pady=10)

b_combobox = ttk.Combobox(value=list(currency.keys()))
b_combobox.pack(padx=10, pady=10)

b_currency_label = ttk.Label()
b_currency_label.pack(padx=10, pady=10)
b_combobox.bind('<<ComboboxSelected>>', update_b_currency_label)

Label(text='Целевая валюта').pack(padx=10, pady=10)

t_combobox = ttk.Combobox(value=list(currency.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind('<<ComboboxSelected>>', update_t_currency_label)

t_currency_label = ttk.Label()
t_currency_label.pack(padx=10, pady=10)

Button(text='Получить курс обмена', command=exchange).pack(padx=10, pady=10)

window.mainloop()