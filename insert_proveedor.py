import tkinter as tk
from tkinter import messagebox
import scale_sql_p3
import datetime

color = ('#99c6f0', '#9fd6f0', '#c6e3f9', '#ecf8f9', '#ecf1f2', '#f25235', '#eee860', '#64f28a', '#3749ac')


class IPro:
    def grabar(self):
        """Funcion command del boton grabar, COMPARA MENSAJE DE scale_sql_p3.update PARA EJECUTAR IF STATEMENT"""
        ruc = self.txt_in1.get()
        if ruc == '':
            self.mensaje.insert(0, 'Inserte RUC')
        for digit in ruc:
            if digit not in '0123456789' or len(ruc) != 13:
                ruc = ''
                self.mensaje.insert(0, 'Formato de RUC incorrecto')
                break
        nombre = self.txt_in2.get()
        if nombre == '':
            self.mensaje.insert(0, 'Inserte nombre')
            ruc = ''
        fecnac = self.txt_in3.get()
        try:
            datetime.datetime.strptime(fecnac, '%Y-%m-%d')
        except ValueError:
            self.mensaje.insert(0, 'Formato de fecha incorrecto')
            ruc = ''
        direccion = self.txt_in4.get()
        telf = self.txt_in5.get()
        correo = self.txt_in6.get()
        sap = self.txt_in8.get()
        for digit in sap:
            if digit not in '0123456789' or len(sap) != 9:
                ruc = ''
                self.mensaje.insert(0, 'Formato SAP incorrecto. Ingrese codigo SAP.')
                break
        if ruc != '' and messagebox.askyesno('Apunto', 'Crear proveedor?', default='no'):
            ms = scale_sql_p3.p_loader(self.cac_codigo, ruc, nombre, fecnac, direccion, telf, correo, sap)
            self.mensaje.insert(0, f'{ms[0]} -- {ms[1][0]}: {ms[1][1]}')
            self.lbl_7.config(text=f'{ms[1][0]}')

    def borrar(self):
        self.txt_in1.delete(0, 'end')
        self.txt_in2.delete(0, 'end')
        self.txt_in3.delete(0, 'end')
        self.txt_in4.delete(0, 'end')
        self.txt_in5.delete(0, 'end')
        self.txt_in6.delete(0, 'end')
        self.txt_in8.delete(0, 'end')
        self.lbl_7.config(text='')

    def __init__(self, master, cac_nombre, cac_codigo):
        win = tk.Frame(master)

        lbl = tk.Label(win, text=cac_nombre, bg=color[0], font='arial 14', fg=color[8])
        lbl.grid(columnspan=2, pady=10, sticky="EW")

        lbl_1 = tk.Label(win, text="RUC : ", bg=color[2], font='arial 10')
        lbl_1.grid(row=1, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in1 = tk.Entry(win, width=13, font='arial 12')
        self.txt_in1.grid(row=1, column=1, pady=5, sticky="W")
        self.txt_in1.focus_set()

        lbl_2 = tk.Label(win, text="APELLIDOS Y NOMBRES : ", bg=color[2], font='arial 10')
        lbl_2.grid(row=2, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in2 = tk.Entry(win, width=40, font='arial 12')
        self.txt_in2.grid(row=2, column=1, pady=5, sticky="W")

        lbl_3 = tk.Label(win, text="FECHA NAC. aaaa-mm-dd : ", bg=color[2], font='arial 10')
        lbl_3.grid(row=3, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in3 = tk.Entry(win, width=10, font='arial 12')
        self.txt_in3.grid(row=3, column=1, pady=5, sticky="W")

        lbl_4 = tk.Label(win, text="DIRECCION : ", bg=color[2], font='arial 10')
        lbl_4.grid(row=4, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in4 = tk.Entry(win, width=40, font='arial 12')
        self.txt_in4.grid(row=4, column=1, pady=5, sticky="W")

        lbl_5 = tk.Label(win, text="# TELEFONO : ", bg=color[2], font='arial 10')
        lbl_5.grid(row=5, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in5 = tk.Entry(win, width=40, font='arial 12')
        self.txt_in5.grid(row=5, column=1, pady=5, sticky="W")

        lbl_6 = tk.Label(win, text="CORREO : ", bg=color[2], font='arial 10')
        lbl_6.grid(row=6, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in6 = tk.Entry(win, width=40, font='arial 12')
        self.txt_in6.grid(row=6, column=1, pady=5, sticky="W")

        lbl_7 = tk.Label(win, text="CODIGO ASIGNADO: ", bg=color[7], font='arial 15')
        lbl_7.grid(row=8, column=0, pady=5, padx=10, sticky="EW")
        self.lbl_7 = tk.Label(win, width=6, bg=color[7], font='arial 15')
        self.lbl_7.grid(row=8, column=1, pady=5, sticky="w")

        lbl_8 = tk.Label(win, text="C. SAP : ", bg=color[2], font='arial 10')
        lbl_8.grid(row=7, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in8 = tk.Entry(win, width=40, font='arial 12')
        self.txt_in8.grid(row=7, column=1, columnspan=2, pady=5, sticky="W")

        btn_borrar = tk.Button(win, text="BORRAR", command=self.borrar, width=10, font='arial 12', height=1)
        btn_borrar.grid(row=9, column=0, pady=15)
        btn_borrar.configure(bg=color[5])

        btn_grabar = tk.Button(win, text="GRABAR", command=self.grabar, width=10, font='arial 12', height=1)
        btn_grabar.grid(row=9, column=1, pady=15)
        btn_grabar.configure(bg=color[7])

        self.mensaje = tk.Listbox(win, height=6, width=80, font='arial 11')
        self.mensaje.insert("end", 'Ingrese la informacion a registrar')
        self.mensaje.grid(row=10, columnspan=2, padx=10, pady=10)

        self.cac_codigo = cac_codigo

        win.pack()


# root = tk.Tk()
# app = IPro(root, 'prueba', 1000)
# root.mainloop()
