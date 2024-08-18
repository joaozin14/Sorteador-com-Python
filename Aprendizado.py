#####Algumas coisas que eu aprendi com esse projeto#####


#foreground "cor de texto"
#background "fundo"
#relief "borda decorativa"
#padx e pady "espaçamento"
#master representa a tela principal "master= janela" 
#borderwidth grossura das bordas
#frame funciona como o container do html
#side define em qual lado o widget ficara


#atribuindo uma imagem a um botão (se a imagem ja estiver na mesma pasta do projeto, adianta)
'''imagem = ImageTk.PhotoImage(Image.open("caption.jpg"))
botaoimg = Button(image=imagem)
botaoimg.pack(side=BOTTOM)'''

#Para colocar uma imagem de fundo na janela
'''imagem = (Image.open("PapeldeParedeJacaranda.jpg"))
img = ImageTk.PhotoImage(imagem)
hjk = tkinter.Label(image=img)
hjk.pack()'''

#Para deixar a imagem bem rente a janela
'''fundo = tkinter.Label(image=img)
fundo.place(x=0, y=0)'''
