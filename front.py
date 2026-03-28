from tkinter import *

class Gui():
    def __init__(self):
        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        self.nome = StringVar()
        self.user = StringVar()
        self.email = StringVar()
        self.cpf = StringVar()

        Label(self.window, text='Nome').grid(row=0, column=0)
        Label(self.window, text='User').grid(row=1, column=0)
        Label(self.window, text='Email').grid(row=2, column=0)
        Label(self.window, text='CPF').grid(row=3, column=0)

        self.entNome = Entry(self.window, textvariable=self.nome)
        self.entUser = Entry(self.window, textvariable=self.user)
        self.entEmail = Entry(self.window, textvariable=self.email)
        self.entCPF = Entry(self.window, textvariable=self.cpf)

        self.entNome.grid(row=0, column=1)
        self.entUser.grid(row=1, column=1)
        self.entEmail.grid(row=2, column=1)
        self.entCPF.grid(row=3, column=1)

        self.listClientes = Listbox(self.window, width=100)
        self.listClientes.grid(row=0, column=2, rowspan=10)

        scroll = Scrollbar(self.window)
        scroll.grid(row=0, column=3, rowspan=10)

        self.listClientes.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.listClientes.yview)

        self.btnViewAll = Button(self.window, text='Ver todos')
        self.btnBuscar = Button(self.window, text='Buscar')
        self.btnInserir = Button(self.window, text='Inserir')
        self.btnUpdate = Button(self.window, text='Atualizar')
        self.btnDel = Button(self.window, text='Deletar')
        self.btnClose = Button(self.window, text='Fechar', command=self.window.destroy)

        self.btnViewAll.grid(row=4, column=0, columnspan=2)
        self.btnBuscar.grid(row=5, column=0, columnspan=2)
        self.btnInserir.grid(row=6, column=0, columnspan=2)
        self.btnUpdate.grid(row=7, column=0, columnspan=2)
        self.btnDel.grid(row=8, column=0, columnspan=2)
        self.btnClose.grid(row=9, column=0, columnspan=2)

    def run(self):
        self.window.mainloop()