from tkinter import *
from tkinter import ttk

cor1 = "#3b3b3b"
cor2 = "#feffff"
cor3 = "#38576b"
cor4 = "#ECEFF1"
cor5 = '#FFAB40'

janela = Tk()
janela.title("Calculadora")
janela.geometry("310x395")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=310, height=130, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=310, height=395)
frame_corpo.grid(row=1, column=0)

todos_valores = ''

def entrada_valores(valor):
    
    global todos_valores
    todos_valores = todos_valores + str(valor)
    valor_texto.set(todos_valores)
    
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")
    
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 21'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


b_1 = Button(frame_corpo, command = limpar_tela, text="C", width=13, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command = lambda: entrada_valores('%'), text="%", width=6, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=150, y=0)
b_3 = Button(frame_corpo, command = lambda: entrada_valores('/'),text="/", width=6, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=225, y=0)


b_4 = Button(frame_corpo, command = lambda: entrada_valores('7'),text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_corpo, command = lambda: entrada_valores('8'),text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=75, y=52)
b_6 = Button(frame_corpo, command = lambda: entrada_valores('9'),text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=150, y=52)
b_7 = Button(frame_corpo, command = lambda: entrada_valores('*'),text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=225, y=52)

b_8 = Button(frame_corpo, command = lambda: entrada_valores('4'),text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_corpo, command = lambda: entrada_valores('5'),text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=75, y=104)
b_10 = Button(frame_corpo, command = lambda: entrada_valores('6'),text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=150, y=104)
b_11 = Button(frame_corpo, command = lambda: entrada_valores('-'),text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=225, y=104)

b_12 = Button(frame_corpo, command = lambda: entrada_valores('1'),text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_corpo, command = lambda: entrada_valores('2'),text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=75, y=156)
b_14 = Button(frame_corpo, command = lambda: entrada_valores('3'),text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=150, y=156)
b_15 = Button(frame_corpo, command = lambda: entrada_valores('+'),text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=225, y=156)

b_16 = Button(frame_corpo, command = lambda: entrada_valores('0'),text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_corpo, command = lambda: entrada_valores('.'),text=".", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=150, y=208)
b_18= Button(frame_corpo, command = calcular, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=225, y=208)



janela.mainloop()
