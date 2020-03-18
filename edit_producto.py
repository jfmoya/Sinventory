import tkinter
from tkinter import messagebox
import scale_sql_p3
import CONF_APUNTO
import decimal

color = ('#99c6f0', '#9fd6f0', '#c6e3f9', '#ecf8f9', '#ecf1f2', '#f25235', '#eee860', '#64f28a', '#3749ac')
cac_nombre = scale_sql_p3.cac_nombre_r()  # DEFAULT
cac_codigo = scale_sql_p3.cac_codigo_r()  # DEFAULT
prd_codigo = CONF_APUNTO.prd_codigo  # SETTING


class EPrd:
    def actualizar(self):
        """Funcion command del boton actualizar"""
        codigo = prd_codigo
        try:
            nombre = self.txt_in2.get()
            preciogk = decimal.Decimal(self.txt_in3.get())
            taragaveta = decimal.Decimal(self.txt_in4.get())
            merma = decimal.Decimal(self.txt_in5.get())/100
            # print(codigo, nombre, preciogk, taragaveta, merma)
            if messagebox.askyesno('Apunto', 'Está a punto de actualizar información.\n¿Desea continuar?',
                                   default='no'):
                ms = scale_sql_p3.producto_u(codigo, nombre, preciogk, taragaveta, merma)
                self.mensaje.insert(0, ms[0])
                self.mensaje.insert(0, f'{ms[1][0]} $/Kg:{ms[1][1]} Tara/Gaveta:{ms[1][2]}Kg Merma:{ms[1][3]*100}%')
        except decimal.InvalidOperation:
            self.mensaje.insert(0, 'Formato Incorrecto')

    def consultar(self):
        codigo = prd_codigo
        # print(codigo)
        producto = scale_sql_p3.producto_r(codigo)[0]
        # print(producto)
        if producto == []:
            self.mensaje.insert(0, 'CODIGO no existente')
            self.borrar()
        else:
            self.mensaje.insert(0, f'cod:{producto[0]} --{producto[1]}-- $/Kg:{producto[2]} '
                                   f'- Tara:{producto[3]}Kg - Merma: {producto[4]*100}%')
            self.txt_in1.config(text=f'{producto[0]}')
            self.txt_in2.delete(0, 'end')
            self.txt_in2.insert(0, f'{producto[1]}')
            self.txt_in3.delete(0, 'end')
            self.txt_in3.insert(0, f'{producto[2]}')
            self.txt_in4.delete(0, 'end')
            self.txt_in4.insert(0, f'{producto[3]}')
            self.txt_in5.delete(0, 'end')
            self.txt_in5.insert(0, f'{producto[4]*100}')

    def borrar(self):
        self.txt_in1.config(text='')
        self.txt_in2.delete(0, 'end')
        self.txt_in3.delete(0, 'end')
        self.txt_in4.delete(0, 'end')
        self.txt_in5.delete(0, 'end')

    def __init__(self, master):
        win = tkinter.Frame(master)

        lbl = tkinter.Label(win, text=cac_nombre, bg=color[0], font='arial 14', fg=color[8])
        lbl.grid(columnspan=3, pady=10, sticky="EW")

        lbl_1 = tkinter.Label(win, text="C. PRODUCTO : ", bg=color[2], font='arial 10')
        lbl_1.grid(row=2, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in1 = tkinter.Label(win, width=13, font='arial 12')
        self.txt_in1.grid(row=2, column=1, columnspan=2, pady=5, sticky="W")

        lbl_2 = tkinter.Label(win, text="PRODUCTO : ", bg=color[2], font='arial 10')
        lbl_2.grid(row=3, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in2 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in2.grid(row=3, column=1, columnspan=2, pady=5, sticky="W")

        lbl_3 = tkinter.Label(win, text="PRECIO $/KG : ", bg=color[2], font='arial 10')
        lbl_3.grid(row=4, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in3 = tkinter.Entry(win, width=10, font='arial 12')
        self.txt_in3.grid(row=4, column=1, columnspan=2, pady=5, sticky="W")

        lbl_4 = tkinter.Label(win, text="TARA GAVETA KG : ", bg=color[2], font='arial 10')
        lbl_4.grid(row=5, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in4 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in4.grid(row=5, column=1, columnspan=2, pady=5, sticky="W")

        lbl_5 = tkinter.Label(win, text="% MERMA : ", bg=color[2], font='arial 10')
        lbl_5.grid(row=6, column=0, pady=5, padx=10, sticky="EW")
        self.txt_in5 = tkinter.Entry(win, width=40, font='arial 12')
        self.txt_in5.grid(row=6, column=1, columnspan=2, pady=5, sticky="W")

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
        self.mensaje.insert("end", 'PRECIONE CONSULTAR')
        self.mensaje.grid(row=9, columnspan=3, padx=10, pady=10)

        win.pack()


# root = tkinter.Tk()
# app = EPrd(root)
# root.mainloop()
