import requests
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_cr_label(event):
    global code
    code = cr_combobox.get()
    name = cripto[code]
    cr_label.config(text=f"{code} ({name})")


def update_t_label(event):
    global t_code_api
    global t_code
    t_code = t_combobox.get()
    t_code_api = (t_code).lower()
    t_name = cur[t_code]
    t_label.config(text=t_name)
    print(t_code_api)


def update_rate_label():
    rate_label.config(text=f"Курс: {exchange_rate:.2f} {t_code} за 1 {code}")


def cripto_rate():
    global exchange_rate

    cr_code = (cr_combobox.get()).lower()

    if cr_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={cr_code}&vs_currencies={t_code_api}')
            response.raise_for_status()
            data = response.json()
            if cr_code in data:
                exchange_rate = data[cr_code][t_code_api]
                update_rate_label()
            else:
                mb.showerror("Ошибка", f"Криптовалюта {cr_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", f"Введите код валюты!")

cripto = {
    "Bitcoin": "BTC",
    "Ethereum": "ETH",
    "Ripple": "XRP",
    "Litecoin": "LTC",
    "Cardano": "ADA",
    }

cur = {
    "EUR": "Евро",
    "JPY": "Японская йена",
    "GBP": "Британский фунт стерлингов",
    "AUD": "Австралийский доллар",
    "CAD": "Канадский доллар",
    "CHF": "Швейцарский франк",
    "CNY": "Китайский юань",
    "RUB": "Российский рубль",
    "KZT": "Казахстанский тенге",
    "UZS": "Узбекский сум",
    "USD": "Американский доллар"
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

Label(text="Целевая валюта").pack(padx=10, pady=10)
t_combobox = ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс выбранной криптовалюты", command=cripto_rate).pack(padx=10, pady=10)

rate_label = ttk.Label()
rate_label.pack(padx=10, pady=10)

window.mainloop()
