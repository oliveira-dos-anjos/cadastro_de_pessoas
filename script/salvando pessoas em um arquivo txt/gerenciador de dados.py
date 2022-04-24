from datetime import *
from operator import index
from tkinter import *
from matplotlib import image


def ArquivoExist(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
  
    
def Criar_Arq(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')


def segunda_janela():
    janela2 = Toplevel()
    janela2.title('dados cadastrados')
    janela2.geometry('600x300+200+200')

    logo = Label(janela2, image=imagem)
    logo.place(x=0, y=0)
    
    janela2.resizable(False,False)

    h = Scrollbar(janela2, orient = 'horizontal') 

    h.pack(side = BOTTOM, fill = X) 


    v = Scrollbar(janela2) 

    v.pack(side = RIGHT, fill = Y) 

    t = Text(janela2, width = 10, height = 10, wrap = NONE, 
    xscrollcommand = h.set,  
    yscrollcommand = v.set) 

    try:
        a = open(arq, "rt")
    except:
        t.insert(END,"Erro ao ler o arquivo")
    else:
        t.insert(END,"NOME           | SEXO| NASCIMENTO  | PESO  | CONTATO    \n")
        t.insert(END,"__" * 28)
        t.insert(END, "\n")
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n", "")
            t.insert(END,f"{dado[0]:<15}| {dado[1]:<4}| {dado[2]:<12}| {dado[3]:<6}| {dado[4]}\n")
            
    finally:
        a.close()

    t.pack(side=LEFT, ipadx=200, ipady=200, padx=10, pady=10) 


    h.config(command=t.xview) 


    v.config(command=t.yview) 


    btn = Button(janela2, text= 'fechar janela3', command= janela2.destroy,  width=11, height=2, bg= 'red', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    btn.place(x=495, y=240)


def terceira_janela():
    janela3 = Toplevel()
    janela3.geometry('500x250+400+400')

    logo = Label(janela3, image=imagem)
    logo.place(x=0, y=0)

    janela3.title('adicionar novos dados')
    janela3.resizable(False, False)




    # recebendo os dados a partir da terceira janela3
    label_nome = Label(janela3, text="nome")
    label_nome.place(x=10, y=10)
    nome = Entry(janela3, width=20)
    nome.place(x=105, y=10)

    label_sexo = Label(janela3, text="sexo [F/M]")
    label_sexo.place(x=10, y=35)
    sexo = Entry(janela3, width=20)
    sexo.place(x=105, y=35)

    label_dia = Label(janela3, text="nascimento")
    label_dia.place(x=10, y=60)
    dia = Entry(janela3, width=4)
    dia.place(x=105, y=60)

    label_mes = Label(janela3, text="/")
    label_mes.place(x=133, y=59)
    mes = Entry(janela3, width=4)
    mes.place(x=144, y=60)

    label_ano = Label(janela3, text="/")
    label_ano.place(x=171, y=59)
    ano = Entry(janela3, width=7)
    ano.place(x=182, y=60)

    label_peso = Label(janela3, text="peso")
    label_peso.place(x=10, y=85)
    peso = Entry(janela3, width=20)
    peso.place(x=105, y=85)

    label_contato = Label(janela3, text="contato")
    label_contato.place(x=10, y=110)
    contato = Entry(janela3, width=20)
    contato.place(x=105, y=110)




    def leiaCont(ct):
        try:
            if ct.isnumeric():
                c = ct
        except:
            index()
        return c




    def salvar():
        contt = 0
        nm = nome.get()
        if nm == "" or nm.isspace():
            label_nm = Label(janela3, text="?", bg='red')
            label_nm.place(x=232, y=10)
        else:
            n = str(nm).upper()
            

            label_n = Label(janela3, text="  ", bg= 'cyan')
            label_n.place(x=232, y=10)



        sx = str(sexo.get()).upper().strip()
        if sx == 'F' or sx == 'M':
            s = str(sx)
            label_sx = Label(janela3, text="  ", bg= 'cyan')
            label_sx.place(x=232, y=35)

        else:
            label_sx = Label(janela3, text="?", bg='red')
            label_sx.place(x=232, y=35)
           
        try:

            ps = str(peso.get()).replace(',', '.')
            try:
                p = float(ps)
                label_p = Label(janela3, text="  ", bg= 'cyan')
                label_p.place(x=232, y=85)


            except:
                label_p = Label(janela3, text="?", bg='red')
                label_p.place(x=232, y=85)
            
            ct = contato.get().strip()
            
            if len(ct) <= 9:
                label_ct = Label(janela3, text="?", bg='red')
                label_ct.place(x=232, y=110)
            else:

                c = leiaCont(ct)
                label_ct = Label(janela3, text="  ", bg= 'cyan')
                label_ct.place(x=232, y=110)
                contt = 1


            try:
                d = int(dia.get())
                m = int(mes.get())
                a = int(ano.get())

                nasc = date(a, m, d)

                idd = date.today() - nasc
                calculo_idade = idd.days / 365.25
                idade = int(calculo_idade)
                if nasc <= date.today():
                    label_nasc = Label(janela3, text="  ", bg= 'cyan')
                    label_nasc.place(x=232, y=60)

                    nascimento = str(f"{d}/{m}/{a}")

                    label_nasc = Label(janela3, text="  ", bg= 'cyan')
                    label_nasc.place(x=232, y=60)



            except:

  
                label_ano = Label(janela3, text="?", bg='red')
                label_ano.place(x=232, y=60)

        except:
            index()

        try:
            a = open(arq, 'at')
        except:
            label_msg = Label(janela3, text="Houve um erro ao abrir o arquivo!")
            label_msg.place(x=10, y=170)
        else:
            try:
                if nascimento:
                    if p:
                        if s:
                            if n:
                                if contt == 1:
                                    try:
                                        a.write(f"{n};{s};{nascimento};{p:.1f};{ct}\n")
                                        label_msg = Label(janela3, text=f'Novo registro de \'{n}\' adicionado com sucesso.', bg='green')
                                        label_msg.place(x=10, y=170)
                                        limpar_tela()

 
                                    except:
                                        index()()
            except:

                label_msg = Label(janela3, text="Preencha todos os campos corretamente", bg= 'red')
                label_msg.place(x=10, y=170)
            else:

                a.close()


    def limpar_tela():
        nome.delete(0, END)
        sexo.delete(0, END)
        dia.delete(0, END)
        mes.delete(0, END)
        ano.delete(0, END)
        peso.delete(0, END)
        contato.delete(0, END)



    # definindo botoes da terceira janela3
    btn = Button(janela3, text= 'salvar', command= salvar, width=10, height=2, bg= 'green', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    btn.place(x=20, y=200)

    btn = Button(janela3, text= "limpar", command= limpar_tela, width=10, height=2, bg= 'orange', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    btn.place(x=115, y=200)


    btn = Button(janela3, text= "fechar janela", command= janela3.destroy, width=10, height=2, bg= 'red', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
    btn.place(x=410, y=200)



# programa principal


# Verifica se o arquivo existe, se não, o arquivo é criado
arq = 'Dados cadastrais'
if not ArquivoExist(arq):
    Criar_Arq(arq)



# layout da janela3 principal
janela = Tk()
janela.title("gerenciador de dados pessoais")
janela['bg'] = 'gray'
img = PhotoImage(file= 'C:\\Users\\RAFAEL\Desktop\\adição e manipulacão de dados\\dependências\\imagem\\icone.png')
janela.iconphoto(True, img)

imagem = PhotoImage(file= 'C:\\Users\\RAFAEL\\Documents\\minhas-ideias\\tkinter\\imagens\\img.GIF')

image = imagem.subsample(0,0)
logo = Label(janela, image=imagem)
logo.place(x=0, y=0)




#dimensões da janela3 principal
largura = 500
altura = 250

# resolução do sistema
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

# faz com que a janela principal sempre apareça no centro
posx = (largura_screen / 2) - (largura / 2)
posy = (altura_screen / 2) - (altura / 2)

#define a geometria da janela principal
janela.geometry('%dx%d+%d+%d' % (largura, altura, posx, posy))
janela.resizable(False, False)

#adicionando botoes na janela3 principal
btn = Button(janela, text= '1 - ver pessoas cadastrados',command=segunda_janela, width=25, height=2, bg= 'yellow', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=15, y=40)

btn = Button(janela, text= '2 - cadastrar novas pessoas', command=terceira_janela, width=25, height=2, bg= 'green', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=15, y=90)

btn = Button(janela, text= '3 - sair do sistema', command= janela.destroy, width=25, height=2, bg= 'red', fg= 'black', font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
btn.place(x=15, y=140)




janela.mainloop()