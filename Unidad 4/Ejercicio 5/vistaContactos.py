import tkinter as tk
from tkinter import messagebox
from peliculas import Peliculas

class ContactList(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = tk.Listbox(self, **kwargs)
        scroll = tk.Scrollbar(self, command=self.lb.yview)
        self.lb.config(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

    def insertar(self, contacto, index=tk.END):
        text = "{}".format(contacto.get_titulo())
        self.lb.insert(index, text)


class ContactForm(tk.LabelFrame):
    fields = ("Titulo", "resumen", "Lenguaje", "Fecha", "Generos")
    def __init__(self, master, **kwargs):
        super().__init__(master, text="Pelicula", padx=10, pady=10, **kwargs)
        self.frame = tk.Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()
    def crearCampo(self, field):
        position, text = field
        label = tk.Label(self.frame, text=text)
        entry = tk.Entry(self.frame, width=25)
        label.grid(row=position, column=0, pady=5)
        entry.grid(row=position, column=1, pady=5)
        return entry
    def mostrarEstadoContactoEnFormulario(self, pelicula):
        # a partir de un contacto, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (pelicula.get_titulo(), pelicula.get_resumen(),
                  pelicula.get_lenguaje(), pelicula.get_fecha(), pelicula.get_generos())
        for entry, value in zip(self.entries, values):
            entry.delete(0, tk.END)
            entry.insert(0, value)

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, tk.END)


class ContactsView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de peliculas")
        self.list = ContactList(self, height=15)
        self.form = UpdateContactForm(self)
        self.list.pack(side=tk.LEFT, padx=10, pady=10)
        self.form.pack(padx=10, pady=10)
        #self.btn_new.pack(side=tk.BOTTOM, pady=5)
    def setControlador(self, ctrl):
        #vincula la vista con el controlador
        self.list.bind_doble_click(ctrl.seleccionarContacto)

    def agregarContacto(self, contacto):
        self.list.insertar(contacto)
    #Ver estado de Contacto en formulario de contactos
    def verContactoEnForm(self, contacto):
        self.form.mostrarEstadoContactoEnFormulario(contacto)


class UpdateContactForm(ContactForm):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.btn_save = tk.Button(self, text="Guardar")
        self.btn_delete = tk.Button(self, text="Borrar")
        self.btn_save.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
        self.btn_delete.pack(side=tk.RIGHT, ipadx=5, padx=5, pady=5)
    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)