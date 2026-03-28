from tkinter import *

class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30

    window = Tk()
    window.wm_title("PYSQL versão 1.0")

    nome = StringVar()
    user = StringVar()
    email = StringVar()
    cpf = StringVar()

    lbl_nome = Label(window, text='Nome')
    lbl_user = Label(window, text='User')
    lbl_email = Label(window, text='Email')
    lbl_cpf = Label(window, text = 'CPF')

    ent_nome = Entry(window, textvariable=nome, width=width_entry)
    ent_user = Entry(window, textvariable=user, width=width_entry)
    ent_email = Entry(window, textvariable=email, width=width_entry)
    ent_cpf = Entry(window, textvariable=cpf, width=width_entry)

    list_clientes = Listbox(window, width=100)
    scroll_clientes = Scrollbar(window)

    but_view_all = Button(window, text='Ver todos')
    but_buscar = Button(window, text='Buscar')
    but_inserir = Button(window, text='Inserir')
    but_atualizar = Button(window, text='Atualizar')
    but_del = Button(window, text='Deletar Usuários')
    but_fechar = Button(window, text='Fechar')

    lbl_nome.grid(row=0, column=0)
    lbl_user.grid(row=1, column=0)
    lbl_email.grid(row=2, column=0)
    lbl_cpf.grid(row=3, column=0)

    ent_nome.grid(row=0, column=1, padx=50, pady=50)
    ent_user.grid(row=1, column=1)
    ent_email.grid(row=2, column=1)
    ent_cpf.grid(row=3, column=1)

    list_clientes.grid(row=0, column=2, rowspan=10)
    scroll_clientes.grid(row=0, column=6, rowspan=10)

    but_view_all.grid(row=4, column=0, columnspan=2)
    but_buscar.grid(row=5, column=0, columnspan=2)
    but_inserir.grid(row=6, column=0, columnspan=2)
    but_view_all.grid(row=5, column=0, columnspan=2)
    but_atualizar.grid(row=7, column=0, columnspan=2)
    but_del.grid(row=8, column=0, columnspan=2)
    but_fechar.grid(row=9, column=0, columnspan=2)

    list_clientes.configure(yscrollcommand=scroll_clientes.set)
    scroll_clientes.configure(command=list_clientes.yview)

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky="WE", padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    def run(self):
        Gui.window.mainloop()