import tkinter
import scale_sql_p3
import CONF_APUNTO

class CaSoc:
    def grabar(self):
        datos = scale_sql_p3.loader(self.txt_in1.get())
        # print datos
        if datos[0] == 0:
            # print datos [1]
            self.mensaje.insert('end', datos[1])
            for w in datos[2]:
                # print w
                self.mensaje.insert('end', w)
        else:
            # print datos[0]
            for w in datos[1]:
                # print w
                self.mensaje.insert('end', w)
            self.mensaje.insert('end', datos[0])

    def __init__(self, master):

        color = ('#99c6f0','#9fd6f0','#c6e3f9','#ecf8f9','#ecf1f2','#f25235','#eee860','#64f28a','#3749ac')
        win = tkinter.Frame(master)

        lbl_1 = tkinter.Label(win, text=CONF_APUNTO.cliente,
                                bg = color[0], font = 'arial 14', fg = color[8])
        lbl_1.grid(columnspan = 2, pady=10)

        lbl_2 = tkinter.Label(win, text="Actualización de nuevos socios",
                                bg = color[0], font = 'arial 16')
        lbl_2.grid(columnspan = 2, pady=10)

        lbl_3 = tkinter.Label(win, text="NOMBRE DE ARCHIVO", bg = color[2],font = 'arial 10')
        lbl_3.grid(row = 3,columnspan = 2, pady=5)

        self.txt_in1 = tkinter.Entry(win, width = 20, font = 'arial 12')
        self.txt_in1.focus_set()
        self.txt_in1.grid(row = 4,columnspan = 2, pady=10)

        btn_grabar = tkinter.Button(win , text = "ACTUALIZAR BASE", command = self.grabar, width = 18,font = 'arial 12', height=2)
        btn_grabar.grid(row=5, columnspan = 2, pady=20)
        btn_grabar.configure(bg = color[7])

        self.mensaje = tkinter.Listbox(win, height = 18, width = 70 , font = 'arial 12' )
        self.mensaje.grid(row = 6, columnspan = 2, padx=10)

        win.pack()
