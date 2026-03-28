from tkinter import *

class Gui():
    def __init__(self):
        self.x_pad = 5
        self.y_pad = 3
        self.width_entry = 30

        self.window = Tk()
        self.window.wm_title("PYSQL versão 1.0")

        self.nome = StringVar(self.window)
        self.user = StringVar(self.window)
        self.email = StringVar(self.window)
        self.cpf = StringVar(self.window)

        Label(self.window, text='Nome').grid(row=0, column=0)
        Label(self.window, text='User').grid(row=1, column=0)
        Label(self.window, text='Email').grid(row=2, column=0)
        Label(self.window, text='CPF').grid(row=3, column=0)

        Entry(self.window, textvariable=self.nome, width=self.width_entry).grid(row=0, column=1)
        Entry(self.window, textvariable=self.user, width=self.width_entry).grid(row=1, column=1)
        Entry(self.window, textvariable=self.email, width=self.width_entry).grid(row=2, column=1)
        Entry(self.window, textvariable=self.cpf, width=self.width_entry).grid(row=3, column=1)

        self.list_clientes = Listbox(self.window, width=100)
        self.list_clientes.grid(row=0, column=2, rowspan=10)

        scroll = Scrollbar(self.window)
        scroll.grid(row=0, column=3, rowspan=10)

        self.list_clientes.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.list_clientes.yview)

        Button(self.window, text='Ver todos').grid(row=4, column=0, columnspan=2)
        Button(self.window, text='Buscar').grid(row=5, column=0, columnspan=2)
        Button(self.window, text='Inserir').grid(row=6, column=0, columnspan=2)
        Button(self.window, text='Atualizar').grid(row=7, column=0, columnspan=2)
        Button(self.window, text='Deletar Usuários').grid(row=8, column=0, columnspan=2)
        Button(self.window, text='Fechar', command=self.window.destroy).grid(row=9, column=0, columnspan=2)

    def run(self):
        self.window.mainloop()


# execução
app = Gui()
app.run()