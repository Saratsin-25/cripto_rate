import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_cr_label(event):
    code = cr_combobox.get()
    name = cripto[code]
    cr_label.config(text=f"{code} ({name})")


def cripto_rate():
    pass


cripto = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "Ripple": "XRP",
    "Litecoin": "LTC",
    "Cardano": "ADA",
    }


window = Tk()
window.title("Обменные курсы криптовалют")
window.geometry("400x400")

Label(text="Выберите криптовалюту").pack(padx=10, pady=10)
cr_combobox = ttk.Combobox(values=list(cripto.keys()))
cr_combobox.pack(padx=10, pady=10)

cr_combobox.bind("<<ComboboxSelected>>", update_cr_label)

cr_label = ttk.Label()
cr_label.pack(padx=10, pady=10)

Button(text="Получить курс выбранной криптовалюты", command=cripto_rate).pack(padx=10, pady=10)

window.mainloop()