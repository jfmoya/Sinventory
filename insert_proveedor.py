import tkinter
from tkinter import messagebox
import scale_sql_p3
import datetime

color = ('#99c6f0', '#9fd6f0', '#c6e3f9', '#ecf8f9', '#ecf1f2', '#f25235', '#eee860', '#64f28a', '#3749ac')
cac_nombre = scale_sql_p3.cac_nombre_r()  # DEFAULT
cac_codigo = scale_sql_p3.cac_codigo_r()  # DEFAULT


class InsProv:
    def grabar(self):
        """Funcion command del boton grabar, COMPARA MENSAJE DE scale_sql_p3.update PARA EJECUTAR IF STATEMENT"""
        ruc = self.txt_in1.get()
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
        telf = self.txt_in4.get()
        correo = self.txt_in5.get()
        if ruc != '' and messagebox.askyesno('Apunto', 'Crear proveedor?', default='no'):
            ms = scale_sql_p3.p_loader(cac_codigo, ruc, nombre, fecnac, telf, correo)
            self.mensaje.insert(0, f'{ms[0]} -- {ms[1][0]}: {ms[1][1]}')
            self.lbl_6.config(text=f'{ms[1][0]}')

    def borrar(self):
        self.txt_in1.delete(0, 'end')
        self.txt_in2.delete(0, 'end')
        self.txt_in3.delete(0, 'end')
        self.txt_in4.delete(0, 'end')
        self.txt_in5.delete(0, 'end')
        self.lbl_6.config(text='')

    def __init__(self, master):
        win = tkinter.Frame(master)

        lbl = tkinter.Label(win, text=cac_nombre, bg=color[0], font='arial 14', fg=color[8])
        lbl.grid(columnspan=2, pady=10, sticky="EW")

        lbl_1 = tkinter.Label(win, text="RUC : ", bg=color[2], font='arial 10')
        lbl_1.grid(row=1, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in1 = tkinter.Entry(win, width=13, font='arial 12')
        self.txt_in1.grid(row=1, column=1, pady=5, sticky="W")
        self.txt_in1.focus_set()

        lbl_2 = tkinter.Label(win, text="APELLIDOS Y NOMBRES : ", bg=color[2], font='arial 10')
        lbl_2.grid(row=2, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in2 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in2.grid(row=2, column=1, pady=5, sticky="W")

        lbl_3 = tkinter.Label(win, text="FECHA NAC. aaaa-mm-dd : ", bg=color[2], font='arial 10')
        lbl_3.grid(row=3, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in3 = tkinter.Entry(win, width=10, font='arial 12')
        self.txt_in3.grid(row=3, column=1, pady=5, sticky="W")

        lbl_4 = tkinter.Label(win, text="# TELEFONO : ", bg=color[2], font='arial 10')
        lbl_4.grid(row=4, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in4 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in4.grid(row=4, column=1, pady=5, sticky="W")

        lbl_5 = tkinter.Label(win, text="CORREO : ", bg=color[2], font='arial 10')
        lbl_5.grid(row=5, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in5 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in5.grid(row=5, column=1, pady=5, sticky="W")

        lbl_6 = tkinter.Label(win, text="CODIGO ASIGNADO: ", bg=color[7], font='arial 15')
        lbl_6.grid(row=6, column=0, pady=5, padx=10, sticky="EW")
        self.lbl_6 = tkinter.Label(win, width=6, bg=color[7], font='arial 15')
        self.lbl_6.grid(row=6, column=1, pady=5, sticky="w")

        btn_borrar = tkinter.Button(win, text="BORRAR", command=self.borrar, width=10, font='arial 12', height=1)
        btn_borrar.grid(row=7, column=0, pady=15)
        btn_borrar.configure(bg=color[5])

        btn_grabar = tkinter.Button(win, text="GRABAR", command=self.grabar, width=10, font='arial 12', height=1)
        btn_grabar.grid(row=7, column=1, pady=15)
        btn_grabar.configure(bg=color[7])

        self.mensaje = tkinter.Listbox(win, height=6, width=70, font='arial 12')
        self.mensaje.insert("end", 'Ingrese la informacion a registrar')
        self.mensaje.grid(row=8, columnspan=2, padx=10, pady=10)

        win.pack()


root = tkinter.Tk()
app = InsProv(root)
root.mainloop()
