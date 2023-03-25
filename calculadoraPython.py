
from tkinter import Tk, StringVar, Label, Entry, Button
import tkinter as tk

def apertaTecla(novoConteudo):
    varentry.set(varentry.get() + novoConteudo)

def apertaIgual():
    global i
    expressao = varentry.get()
    varentry.set("")
    if expressao != "":
        i = 0
        respostas = E(expressao)
        historico = varresult.get()
        if len(historico.split("\n")) == 5:
            historico = "\n".join(historico.split("\n")[1:])
        respostas = str(respostas).replace(".", ",")
        varresult.set(f"{'' if historico == '' else historico}\n{expressao} = {respostas}")

def E(expressao):
    valorF = F(expressao)
    valorElinha = Elinha(expressao, valorF)
    return valorElinha

def Elinha(expressao, valor):
    global i
    if i < len(expressao) and expressao[i] == "+":
        i = i + 1
        valorF = F(expressao)
        valorElinha = Elinha(expressao, valorF)
        return valor + valorElinha
    elif i < len(expressao) and expressao[i] == "-":
        i = i + 1
        valorF = F(expressao)
        valorElinha = Elinha(expressao, valorF)
        return valor - valorElinha
    return valor

def F(expressao):
    valorG = G(expressao)
    valorFlinha = Flinha(expressao, valorG)
    return valorFlinha

def Flinha(expressao, valor):
    global i
    if i < len(expressao) and expressao[i] == "*":
        i = i + 1
        valorG = G(expressao)
        valorFlinha = Flinha(expressao, valorG)
        return valor * valorFlinha
    elif i < len(expressao) and expressao[i] == "/":
        i = i + 1
        valorG = G(expressao)
        valorFlinha = Flinha(expressao, valorG)
        return valor / valorFlinha
    return valor

def G(expressao):
    global i
    if i < len(expressao) and expressao[i] == "-":
        i = i + 1
        valorG = G(expressao)
        valorGlinha = Glinha(expressao, valorG)
        return -valorGlinha
    if i < len(expressao) and expressao[i] == "√":
        i = i + 1
        valorG = G(expressao)
        valorGlinha = Glinha(expressao, valorG)
        i = i + 1
        return valorGlinha ** 0.5
    elif i < len(expressao) and expressao[i] == "f":
        i = i + 2
        valorG = G(expressao)
        valorGlinha = Glinha(expressao, valorG)
        if i == len(expressao) or expressao[i] != ")":
            return "Expressao inválida! =(" 
        else:
            i = i + 1
            #k = xx(valorGlinha)
            return 8
    else:
        valorH = H(expressao)
        valorGlinha = Glinha(expressao, valorH)
        return valorGlinha

def Glinha(expressao, valor):
    global i
    if i < len(expressao) and expressao[i] == "^":
        i = i + 1
        valorG = G(expressao)
        valorGlinha = Glinha(expressao, valorG)
        return valor ** valorGlinha
    elif i < len(expressao) and expressao[i] == "!":
        i = i + 1
        valorGlinha = Glinha(expressao, valor)
        return fatorial(valorGlinha)
    return valor

def H(expressao):
    global i
    if i < len(expressao) and expressao[i] == "(":
        i = i + 1
        valorE = E(expressao)
        if i == len(expressao) or expressao[i] != ")":
            return "Expressao inválida! =("
        else:
            i = i + 1
            return valorE
    else:
        return I(expressao)

def I(expressao):
    global i
    tamanho = len(expressao)
    numero = ""
    tipo = int
    while i < tamanho and (expressao[i].isdigit() or expressao[i] == "."):
        numero = numero + expressao[i]
        if expressao[i] == ".":
            tipo = float
        i = i + 1
    return tipo(numero)

def xx():
    tela2 = tk.Toplevel()
    tela2.title("Caculo de função")
    tela2.geometry("700x700")

    historico = StringVar()
    resultado = Label(tela2, textvariable=historico)
    resultado.grid(row=0, columnspan=4, padx=10, pady=10)
    historico.set("Valor de A:")

    varentry2 = StringVar()
    entrada = Entry(tela2, bd=2.75, textvariable=varentry2, width=43)
    entrada.grid(row=1,columnspan=4, padx=10, pady=10)

    historico4 = StringVar()
    resultado4 = Label(tela2, textvariable=historico4)
    resultado4.grid(row=3, columnspan=4, padx=10, pady=10)
    historico4.set("Valor de B:")

    varentry4 = StringVar()
    entrada4 = Entry(tela2, bd=2.75, textvariable=varentry4, width=43)
    entrada4.grid(row=4,columnspan=4, padx=10, pady=10)

    historico5 = StringVar()
    resultado5 = Label(tela2, textvariable=historico5)
    resultado5.grid(row=5, columnspan=4, padx=10, pady=10)
    historico5.set("Valor de C:")

    varentry5 = StringVar()
    entrada5 = Entry(tela2, bd=2.75, textvariable=varentry5, width=43)
    entrada5.grid(row=6,columnspan=4, padx=10, pady=10)


    historico6 = StringVar()
    resultado6 = Label(tela2, textvariable=historico6)
    resultado6.grid(row=7, columnspan=4, padx=10, pady=10)
    historico6.set("Valor de X:")

    varentry6 = StringVar()
    entrada6 = Entry(tela2, bd=2.75, textvariable=varentry6, width=43)
    entrada6.grid(row=8,columnspan=4, padx=10, pady=10)

    botaol4 = Button (tela2, text="calcular",background='red',command=lambda: xxx(float(varentry4.get()), float(varentry5.get()), float(varentry2.get()), float(varentry6.get())))
    botaol4.grid(row=9,column=2)

    
    def xxx(b,c,a,x):
        y = x*(a**2) + b*x + c
        print( f"f({x}) = {y}")
        y = str(y)
        varentry.set(varentry.get() + y)
        tela2.destroy()

       
def fatorial(valor):
    resultado = 1
    for j in range(2, valor + 1):
        resultado = resultado * j
    return resultado

def fatorial2ano(valor):
    if valor == 0:
        return 1
    return valor * fatorial2ano(valor - 1)

def limpaTudo():
    varentry.set("")

def limpaUm():
    atual = varentry.get()
    varentry.set(atual[0:len(atual)-1])

telinha = Tk()
telinha.title("Calculadora AED I")
telinha.geometry("375x375")

varresult = StringVar()
resultado = Label(telinha, width=52, height=5, textvariable=varresult)
resultado.grid(row=0,  columnspan=7, padx=10, pady=10)

varentry = StringVar()
entrada = Entry(telinha, bd=3, width=52, textvariable=varentry, state="readonly")
entrada.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

botao1 = Button(telinha, text="1", width=5, command=lambda: apertaTecla("1"))
botao1.grid(row=4, column=0, padx=10, pady=10)

botao2 = Button(telinha, text="2", width=5, command=lambda: apertaTecla("2"))
botao2.grid(row=4, column=1, padx=10, pady=10)

botao3 = Button(telinha, text="3", width=5, command=lambda: apertaTecla("3"))
botao3.grid(row=4, column=2, padx=10, pady=10)

botao4 = Button(telinha, text="4", width=5, command=lambda: apertaTecla("4"))
botao4.grid(row=5, column=0, padx=10, pady=10)

botao5 = Button(telinha, text="5", width=5, command=lambda: apertaTecla("5"))
botao5.grid(row=5, column=1, padx=10, pady=10)

botao6 = Button(telinha, text="6", width=5, command=lambda: apertaTecla("6"))
botao6.grid(row=5, column=2, padx=10, pady=10)

botao7 = Button(telinha, text="7", width=5, command=lambda: apertaTecla("7"))
botao7.grid(row=6, column=0, padx=10, pady=10)

botao8 = Button(telinha, text="8", width=5, command=lambda: apertaTecla("8"))
botao8.grid(row=6, column=1, padx=10, pady=10)

botao9 = Button(telinha, text="9", width=5, command=lambda: apertaTecla("9"))
botao9.grid(row=6, column=2, padx=10, pady=10)

botao0 = Button(telinha, text="0", width=5, command=lambda: apertaTecla("0"))
botao0.grid(row=7, column=1, padx=10, pady=10)

botaoLimpaUm = Button(telinha, text="c", width=5, command=lambda: limpaUm())
botaoLimpaUm.grid(row=7, column=0, padx=10, pady=10)

botaoLimpaTudo = Button(telinha, text="ce", width=5, command=lambda: limpaTudo())
botaoLimpaTudo.grid(row=7, column=2, padx=10, pady=10)

botaoMais = Button(telinha, text="+", width=5, command=lambda: apertaTecla("+"))
botaoMais.grid(row=4, column=3, padx=10, pady=10)

botaoMenos = Button(telinha, text="-", width=5, command=lambda: apertaTecla("-"))
botaoMenos.grid(row=5, column=3, padx=10, pady=10)

botaoMultiplicao = Button(telinha, text="x", width=5, command=lambda: apertaTecla("*"))
botaoMultiplicao.grid(row=6, column=3, padx=10, pady=10)

botaoDivisao = Button(telinha, text="/", width=5, command=lambda: apertaTecla("/"))
botaoDivisao.grid(row=7, column=3, padx=10, pady=10)

botaoFuncao = Button(telinha, text="f(x)", width=5, command=lambda: xx())
botaoFuncao.grid(row=8, column=0, padx=10, pady=10)

botaoFatorial = Button(telinha, text="x!", width=5, command=lambda: apertaTecla("!"))
botaoFatorial.grid(row=8, column=1, padx=10, pady=10)

botaoRaiz = Button(telinha, text="√", width=5, command=lambda: apertaTecla("√"))
botaoRaiz.grid(row=8, column=2, padx=10, pady=10)

botaoExponenciacao = Button(telinha, text="x^y", width=5, command=lambda: apertaTecla("^"))
botaoExponenciacao.grid(row=8, column=3, padx=10, pady=10)

botaoAbrePar = Button(telinha, text="(", width=5, command=lambda: apertaTecla("("))
botaoAbrePar.grid(row=4, column=4, padx=10, pady=10)

botaoFechaPar = Button(telinha, text=")", width=5, command=lambda: apertaTecla(")"))
botaoFechaPar.grid(row=5, column=4, padx=10, pady=10)

botaoVirgula = Button(telinha, text=",", width=5, command=lambda: apertaTecla(","))
botaoVirgula.grid(row=6, column=4, padx=10, pady=10)

botaoIgual = Button(telinha, text="=", width=5, height=4, command=lambda: apertaIgual(), background='red')
botaoIgual.grid(row=7, rowspan=2, column=4, padx=10, pady=10)


telinha.mainloop()