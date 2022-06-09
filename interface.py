import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd

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

combobox_selecaododia = ttk.Combobox(values=lista_moeda)
combobox_selecaododia.grid(row=2, column=2, padx=10, pady=10, sticky="nswe")

label_dia = tk.Label(text="A cotação da moeda selecionada do dia tal é de tanto")
label_dia.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

label_cotacaomoeda2 = tk.Label(text="cotação de multiplas moedas", borderwidth=2, relief="solid")
label_cotacaomoeda2.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)
janela.mainloop()
