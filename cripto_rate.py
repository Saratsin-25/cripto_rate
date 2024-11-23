import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_cr_label(event):
    global code
    code = cr_combobox.get()
    name = cripto[code]
    cr_label.config(text=f"{code} ({name})")

def update_rate_label():
    rate_label.config(text=f"Курс: {exchange_rate:.2f} usd за 1 {code}")



def cripto_rate():
    global exchange_rate
    cr_code = (cr_combobox.get()).lower()



    if cr_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={cr_code}&vs_currencies=usd')
            response.raise_for_status()
            data = response.json()
            exchange_rate = data[cr_code]['usd']
            update_rate_label()







        except Exception as err:
            print(err)







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

rate_label = ttk.Label()
rate_label.pack(padx=10, pady=10)

window.mainloop()