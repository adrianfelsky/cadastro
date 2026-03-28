from front import Gui
from back import ClienteDAO


class AppController:
    def __init__(self):
        self.view = Gui()
        self.dao = ClienteDAO()
        self.selected = None

        self.view.list_clientes.bind('<<ListboxSelect>>', self.on_select)

        self.view.btn_view_all.config(command=self.view_all)
        self.view.btn_buscar.config(command=self.search)
        self.view.btn_inserir.config(command=self.insert)
        self.view.btn_atualizar.config(command=self.update)
        self.view.btn_deletar.config(command=self.delete)
        self.view.btn_fechar.config(command=self.view.window.destroy)

    def view_all(self):
        rows = self.dao.view()
        self._update_list(rows)

    def search(self):
        rows = self.dao.search(
            self.view.nome.get(),
            self.view.user.get(),
            self.view.email.get(),
            self.view.cpf.get()
        )
        self._update_list(rows)

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

        if self.selected:
            self.dao.delete(self.selected[0])
            self.view_all()

    def on_select(self, event):
        try:
            index = self.view.list_clientes.curselection()[0]
            self.selected = self.view.list_clientes.get(index)

            self.view.set_fields(
                self.selected[1],
                self.selected[2],
                self.selected[3],
                self.selected[4]
            )
        except IndexError:
            self.selected = None

    def _update_list(self, rows):
        self.view.list_clientes.delete(0, 'end')
        for r in rows:
            self.view.list_clientes.insert('end', r)

    def run(self):
        self.view.run()

if __name__ == "__main__":
    app = AppController()
    app.run()