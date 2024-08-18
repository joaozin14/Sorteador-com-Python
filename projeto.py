from tkinter import *
from tkinter import messagebox
import random
import tkinter as tk

janela = Tk()

#Definindo nome, dimensão e cor da janela.
janela.title("Sorteador")
janela.geometry("900x900")
janela.configure(bg="#000000")

#Texto dando boas vindas ao sorteador.
texto_entrada = Label(janela,
                 text="Seja Bem Vindo ao Sorteador!",
                 font="Arial 30 bold",
                 background="#000000",
                 foreground="#FFFAFA")
texto_entrada.pack(pady=20)

#texto informando como usar o sorteador.
informacao = Label(janela,
                 text="Pode ser usado tanto para nomes quanto para números.\nPara o uso Correto do sorteador, faça assim: Pedro,\nThiago, Letícia, Wanda, Lucas",
                 font="Arial 25 bold",
                 background="#000000",
                 foreground="#FFFAFA")
informacao.pack(pady=20)

#Caixa de texto para escrita.
entrada = tk.Text(janela, font="Arial 20 bold", width=50, height=2)
entrada.pack(pady=5)

#Função para sotear ao clicar no botão de sorteio.
def sortear():
    texto = entrada.get("1.0", "end-1c")  #Obtém o texto do widget Text (da posição 1.0 até o fim).
    valores = texto.split(",")  #Divide o texto em uma lista de valores, separando por vírgula.
    sorteado = random.choice(valores)  #Sorteia um valor da lista.
    resultado_Label.config(text=f"Valor sorteado! \n {sorteado}") 

#Botão que ao clicado, sorteia o valor.
botao_sortear = Button(janela,
               text="Sortear",
               font="Arial 20 bold",
               background="#000000",
               foreground="#FFFAFA",
               command=sortear
               )
botao_sortear.pack(pady=15)

#Função sair que faz com que ao clicar no botão sair, a janela seja fechada.
def sair():
    messagebox.showinfo("Sair",
                        "Até mais!")
    janela.destroy()

#Botão que ao clicado, fecha a janela.
botao_sair = Button(janela,
               text="Sair",
               font="Arial 20 bold",
               command= lambda: sair(),
               background="#000000",
               foreground="#FFFAFA"
               )
botao_sair.pack()

#Label para mostrar o resultado do sorteio
resultado_Label = Label(janela,
                        text="",
                        font="Arial 25 bold",
                        background="#000000",
                        foreground="#FFFAFA")
resultado_Label.pack(pady=20)

janela. mainloop()