import tkinter
from tkinter import messagebox
import scale_sql_p3
import datetime

color = ('#99c6f0', '#9fd6f0', '#c6e3f9', '#ecf8f9', '#ecf1f2', '#f25235', '#eee860', '#64f28a', '#3749ac')
cac_nombre = scale_sql_p3.cac_nombre_r()  # DEFAULT
cac_codigo = scale_sql_p3.cac_codigo_r()  # DEFAULT


class EPro:
    def actualizar(self):
        """Funcion command del boton grabar, COMPARA MENSAJE DE scale_sql_p3.update PARA EJECUTAR IF STATEMENT"""

        ruc = self.txt_in1.cget("text")
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
        if ruc != '':
            if messagebox.askyesno('Apunto', 'Está a punto de actualizar información.\n¿Desea continuar?',
                                   default='no'):
                ms = scale_sql_p3.p_update(ruc, nombre, fecnac, direccion, telf, correo)
                self.mensaje.insert(0, f'{ms[0]} -- {ms[1][0]} {ms[1][1]} {ms[1][2]}')

    def consultar(self):
        codigo = self.txt_in7.get()
        # print(codigo)
        proveedor = scale_sql_p3.proveedor_r(codigo)
        # print(proveedor)
        if proveedor == '':
            self.mensaje.insert(0, 'CODIGO no existente')
            self.borrar()
        else:
            self.mensaje.insert(0, f'C:{proveedor[0]}, {proveedor[1]}, {proveedor[2]}, {proveedor[3]}, '
                                   f'{proveedor[4]}, {proveedor[5]}')
            self.txt_in1.config(text=f'{proveedor[0]}')
            self.txt_in2.delete(0, 'end')
            self.txt_in2.insert(0, f'{proveedor[1]}')
            self.txt_in3.delete(0, 'end')
            self.txt_in3.insert(0, f'{proveedor[2]}')
            self.txt_in4.delete(0, 'end')
            self.txt_in4.insert(0, f'{proveedor[3]}')
            self.txt_in5.delete(0, 'end')
            self.txt_in5.insert(0, f'{proveedor[4]}')
            self.txt_in6.delete(0, 'end')
            self.txt_in6.insert(0, f'{proveedor[5]}')

    def borrar(self):
        self.txt_in1.config(text='')
        self.txt_in2.delete(0, 'end')
        self.txt_in3.delete(0, 'end')
        self.txt_in4.delete(0, 'end')
        self.txt_in5.delete(0, 'end')
        self.txt_in6.delete(0, 'end')
        self.txt_in7.delete(0, 'end')

    def __init__(self, master):
        win = tkinter.Frame(master)

        lbl = tkinter.Label(win, text=cac_nombre, bg=color[0], font='arial 14', fg=color[8])
        lbl.grid(columnspan=3, pady=10, sticky="EW")

        lbl_1 = tkinter.Label(win, text="RUC : ", bg=color[2], font='arial 10')
        lbl_1.grid(row=2, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in1 = tkinter.Label(win, width=13, font='arial 12')
        self.txt_in1.grid(row=2, column=1, columnspan=2, pady=5, sticky="W")

        lbl_2 = tkinter.Label(win, text="APELLIDOS Y NOMBRES : ", bg=color[2], font='arial 10')
        lbl_2.grid(row=3, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in2 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in2.grid(row=3, column=1, columnspan=2, pady=5, sticky="W")

        lbl_3 = tkinter.Label(win, text="FECHA NAC. aaaa-mm-dd : ", bg=color[2], font='arial 10')
        lbl_3.grid(row=4, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in3 = tkinter.Entry(win, width=10, font='arial 12')
        self.txt_in3.grid(row=4, column=1, columnspan=2, pady=5, sticky="W")

        lbl_4 = tkinter.Label(win, text="DIRECCION : ", bg=color[2], font='arial 10')
        lbl_4.grid(row=5, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in4 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in4.grid(row=5, column=1, columnspan=2, pady=5, sticky="W")

        lbl_5 = tkinter.Label(win, text="# TELEFONO : ", bg=color[2], font='arial 10')
        lbl_5.grid(row=6, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in5 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in5.grid(row=6, column=1, columnspan=2, pady=5, sticky="W")

        lbl_6 = tkinter.Label(win, text="CORREO : ", bg=color[2], font='arial 10')
        lbl_6.grid(row=7, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in6 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in6.grid(row=7, column=1, columnspan=2, pady=5, sticky="W")

        lbl_7 = tkinter.Label(win, text="CODIGO : ", bg=color[7], font='arial 15')
        lbl_7.grid(row=1, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in7 = tkinter.Entry(win, width=6, font='arial 15')
        self.txt_in7.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
        self.txt_in7.focus_set()

        btn_borrar = tkinter.Button(win, text="LIMPIAR", command=self.borrar, width=12, font='arial 11', height=1)
        btn_borrar.grid(row=8, column=0, pady=15)
        btn_borrar.configure(bg=color[5])

        btn_consultar = tkinter.Button(win, text="CONSULTAR", command=self.consultar, width=12, font='arial 11',
                                       height=1)
        btn_consultar.grid(row=8, column=1, pady=15)
        btn_consultar.configure(bg=color[0])

        btn_actualizar = tkinter.Button(win, text="ACTUALIZAR", command=self.actualizar, width=12, font='arial 11',
                                        height=1)
        btn_actualizar.grid(row=8, column=2, pady=15)
        btn_actualizar.configure(bg=color[7])

        self.mensaje = tkinter.Listbox(win, height=6, width=80, font='arial 11')
        self.mensaje.insert("end", 'Consulta con CODIGO o RUC')
        self.mensaje.grid(row=9, columnspan=3, padx=10, pady=10)

        win.pack()


# root = tkinter.Tk()
# app = EPro(root)
# root.mainloop()
