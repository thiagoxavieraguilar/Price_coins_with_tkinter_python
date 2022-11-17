import tkinter as tk
from tkinter import ttk
import requests
import json


# faz a requisição na api e armazena o dicionario com as moedas
cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
dic_lista_moedas = cotacoes.json()


#criando a janela
janela  = tk.Tk()

janela.title("Cotações de moedas")
janela.rowconfigure(0, weight=1)
janela.columnconfigure([0, 1], weight=1)

mensagem = tk.Label(text="Sistema de cotação de moedas", fg='white', bg='black', width= 35, height=5)
mensagem.grid(row=0, column=0, columnspan=2, sticky="NSEW")


mensagem2 = tk.Label(text='Selecione a moeda desejada')
mensagem2.grid(row=1, column=0)


#opções com todas as moedas
opcoes_moedas = list(dic_lista_moedas.keys())

#Remove as criptomoedas, nesse exemplo só usei moedas fiduciárias 
opcoes_moedas.remove('USDT')
opcoes_moedas.remove('BTC')
opcoes_moedas.remove('ETH')
opcoes_moedas.remove('DOGE')
opcoes_moedas.remove('LTC')
opcoes_moedas.remove('XRP')

#define as opções das moedas no tkinter com os valores do dict
lista_moedas = ttk.Combobox(janela, values=opcoes_moedas)
lista_moedas.grid(row=1, column=1)


#faz o get da moeda escolhida e a faz a requisição 

def pegar_cotacao():
    try:
        moeda_preenchida = lista_moedas.get()
        link = f"https://economia.awesomeapi.com.br/last/{moeda_preenchida}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao =float(dic_requisicao[f"{moeda_preenchida}BRL"]['bid'])
        mensagem3 = tk.Label(text= f'O valor do(a) {moeda_preenchida} é de R${cotacao:,.2f}')
        mensagem3.grid(row=2, column=0)
        return cotacao
    except:
        return print("erro, escolha uma das opções")

       
    



botao = tk.Button(text='Buscar cotação', command=pegar_cotacao)
botao.grid(row=2, column=1)
janela.mainloop()