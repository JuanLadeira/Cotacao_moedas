import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd

def pegar_cotacao():
    pass


janela = Tk()
lista_moeda = ["R$", "USD", "EUR"]

janela.title('Ferramenta para cotação de moeda')

label_cotacaomoeda = tk.Label(text="Cotação de uma moeda especifica", borderwidth=2, relief="solid")
label_cotacaomoeda.grid(row=0, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar moeda")
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moeda)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky="nswe")
label_selecaododia = tk.Label(text="Selecionar o dia que deseja pegar a cotação")
label_selecaododia.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky="nswe")

label_textocotacao= tk.Label(text="")
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_cotacao = tk.Button(text='Pegar Cotação', command=pegar_cotacao)
botao_cotacao.grid(row=3, column=2, padx=10, pady=10, sticky="nswe")

#cotação de multiplas moedas
label_cotacaomoeda2 = tk.Label(text="cotação de multiplas moedas", borderwidth=2, relief="solid")
label_cotacaomoeda2.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)
janela.mainloop()
