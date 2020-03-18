import CONF_APUNTO
import tkinter as tk

from tkinter import messagebox

import report_total_proveedores
import report_transacciones
import report_transacciones_proveedor

import insert_proveedor
import edit_proveedor
import report_proveedores

import edit_producto


class App:
    def __init__(self, master):

        container = tk.Frame(master)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for F in (RTotProF, RTraProF, RTraF, IProF, EProF, RProF, EPrdF, InicioF):
            frame = F(container)
            self.frames[F] = frame

        menubar = tk.Menu(master)

        menubar.add_command(label='Inicio', command=lambda: self.show_frame(InicioF))

        m_produccion = tk.Menu(menubar)
        m_produccion.add_command(label='Totales x Proveedores', command=lambda: self.show_frame(RTotProF))
        m_produccion.add_command(label='Entregas x Proveedor', command=lambda: self.show_frame(RTraProF))
        m_produccion.add_command(label='Transacciones', command=lambda: self.show_frame(RTraF))
        menubar.add_cascade(label='Producción', menu=m_produccion)
        
        m_proveedor = tk.Menu(menubar)
        m_proveedor.add_command(label='Crear Nuevo Proveedor', command=lambda: self.show_frame(IProF))
        m_proveedor.add_command(label='Editar Proveedor', command=lambda: self.show_frame(EProF))
        m_proveedor.add_command(label='Reporte de Proveedores', command=lambda: self.show_frame(RProF))
        menubar.add_cascade(label='Proveedores', menu=m_proveedor)

        m_producto = tk.Menu(menubar)
        m_producto.add_command(label='Editar Producto', command=lambda: self.show_frame(EPrdF))
        menubar.add_cascade(label='Producto', menu=m_producto)

        root.config(menu=menubar)

    def show_frame(self, key):
        frame = self.frames[key]
        frame.tkraise()


class RTotProF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = report_total_proveedores.RTotPro(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class RTraProF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = report_transacciones_proveedor.RTraPro(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class RTraF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = report_transacciones.RTra(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class IProF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = insert_proveedor.IPro(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class EProF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = edit_proveedor.EPro(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class RProF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = report_proveedores.RPro(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class EPrdF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        sframe = edit_producto.EPrd(self.frame)

    def tkraise(self):
        self.frame.tkraise()


class InicioF:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid(row=0, column=0, sticky="nsew")
        label = tk.Label(self.frame, text="Apunto de PCServ - 0987090445 - J. Moya")
        label.pack()
        try:
            label_2 = tk.Label(self.frame, image=logo)
            label_2.pack()
        except:
            pass

    def tkraise(self):
        self.frame.tkraise()


root = tk.Tk()
root.title("APunto")
try:
    root.iconbitmap(CONF_APUNTO.icon_path)
except:
    pass
try:
    logo = tk.PhotoImage(file=CONF_APUNTO.logo_path)
except:
    pass


app = App(root)

root.mainloop()
try:
    root.destroy()
except:
    pass


# button = tk.Button(root, text = 'Hola', command = root.quit)
# button.pack()
