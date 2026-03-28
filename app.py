from front import Gui
from back import ClienteDAO
from tkinter import END


class Controller:
    def __init__(self):
        self.view = Gui()
        self.dao = ClienteDAO()
        self.selected = None

        # Eventos
        self.dao.create_table()
        self.view_all()
        self.view.listClientes.bind('<<ListboxSelect>>', self.on_select)

        # Botões
        self.view.btnViewAll.config(command=self.view_all)
        self.view.btnBuscar.config(command=self.search)
        self.view.btnInserir.config(command=self.insert)
        self.view.btnUpdate.config(command=self.update)
        self.view.btnDel.config(command=self.delete)

    def view_all(self):
        rows = self.dao.view()
        self.update_list(rows)

    def search(self):
        rows = self.dao.search(
            self.view.nome.get(),
            self.view.user.get(),
            self.view.email.get(),
            self.view.cpf.get()
        )
        self.update_list(rows)

    def insert(self):
        self.dao.insert(
            self.view.nome.get(),
            self.view.user.get(),
            self.view.email.get(),
            self.view.cpf.get()
        )
        self.view_all()

    def update(self):
        if self.selected:
            self.dao.update(
                self.selected[0],
                self.view.nome.get(),
                self.view.user.get(),
                self.view.email.get(),
                self.view.cpf.get()
            )
            self.view_all()

    def delete(self):
        if self.selected:
            self.dao.delete(self.selected[0])
            self.view_all()

    def on_select(self, event):
        try:
            index = self.view.listClientes.curselection()[0]
            self.selected = self.view.listClientes.get(index)

            self.view.entNome.delete(0, END)
            self.view.entNome.insert(END, self.selected[1])

            self.view.entUser.delete(0, END)
            self.view.entUser.insert(END, self.selected[2])

            self.view.entEmail.delete(0, END)
            self.view.entEmail.insert(END, self.selected[3])

            self.view.entCPF.delete(0, END)
            self.view.entCPF.insert(END, self.selected[4])

        except IndexError:
            self.selected = None

    def update_list(self, rows):
        self.view.listClientes.delete(0, END)
        for r in rows:
            self.view.listClientes.insert(END, r)

    def run(self):
        self.view.run()


if __name__ == "__main__":
    app = Controller()
    app.run()