import tkinter
import scale_sql_p3
import CONF_APUNTO

class CCod:
    def grabar(self):
        """Funcion command del boton grabar, COMPARA MENSAJE DE scale_sql_p3.update PARA EJECUTAR IF STATEMENT"""
        t_num, t_idnum, t_weight, new_idnum = self.txt_in1.get(),self.txt_in2.get(),self.txt_in3.get(),self.txt_in4.get()
        try:
            float(t_num), float(t_idnum), float(t_weight), float(new_idnum)
            self.mensaje.delete(0, 'end')
            msg0 = scale_sql_p3.t_update(new_idnum, t_num, t_idnum, t_weight)
            # print (msg0)
            self.mensaje.insert('end', msg0)
            if msg0 != 'Numero de socio incorrecto' and msg0 != 'Transaccion no puede ser modificada':
                msg1 = new_idnum +'-'+scale_sql_p3.namer(new_idnum)
                new_ticket = scale_sql_p3.entrega(new_idnum)
                msg2 = 'T#'+ str(new_ticket[1]) +'  Litros : ' + str(new_ticket[2])
                self.mensaje.insert('end', msg1)
                self.mensaje.insert('end', msg2)
                # print (msg1)
                # print (msg2)

        except:
            self.mensaje.delete(0, 'end')
            self.mensaje.insert('end', 'Llene todos los casilleros...')


    def borrar(self):
        self.txt_in1.delete(0, 'end')
        self.txt_in2.delete(0, 'end')
        self.txt_in3.delete(0, 'end')
        self.txt_in4.delete(0, 'end')


    def __init__(self, master):
        
        color = ('#99c6f0','#9fd6f0','#c6e3f9','#ecf8f9','#ecf1f2','#f25235','#eee860','#64f28a','#3749ac')
        win = tkinter.Frame(master)
        
        lbl_1 = tkinter.Label(win, text=CONF_APUNTO.cliente,
                                bg = color[0], font = 'arial 14', fg = color[8])
        lbl_1.grid(columnspan = 4, pady=10)

        lbl_2 = tkinter.Label(win, text="INGRESE LA INFORMACION DE LA TRANSACCION A CORREGIR:",
                                bg = color[0], font = 'arial 16')
        lbl_2.grid(columnspan = 4, pady=10)

        lbl_3 = tkinter.Label(win, text="Ticket #:", bg = color[2],font = 'arial 10')
        lbl_3.grid(column=0,row = 3, pady=5)
        lbl_4 = tkinter.Label(win, text="Socio #:", bg = color[2],font = 'arial 10')
        lbl_4.grid(column=1,row = 3, pady=5)
        lbl_5 = tkinter.Label(win, text="Litros L.:", bg = color[2],font = 'arial 10')
        lbl_5.grid(column=2,row = 3, pady=5)
        lbl_6 = tkinter.Label(win, text="Socio # CORRECTO:", bg = color[7],font = 'arial 12')
        lbl_6.grid(column=3,row = 3, pady=5)

        self.txt_in1 = tkinter.Entry(win, width = 6, font = 'arial 12')
        self.txt_in1.focus_set()
        self.txt_in1.grid(row = 4,column = 0, pady=10)
        self.txt_in2 = tkinter.Entry(win, width = 6, font = 'arial 12')
        self.txt_in2.grid(row = 4,column = 1, pady=10)
        self.txt_in3 = tkinter.Entry(win, width = 6, font = 'arial 12')
        self.txt_in3.grid(row = 4,column = 2, pady=10)
        self.txt_in4 = tkinter.Entry(win, width = 6, font = 'arial 16')
        self.txt_in4.grid(row = 4,column = 3, pady=10)

        btn_grabar = tkinter.Button(win , text = "GRABAR", command = self.grabar, width = 10,font = 'arial 12', height=2)
        btn_grabar.grid(row=5, column=3, pady=20)
        btn_grabar.configure(bg = color[7])

        btn_borrar = tkinter.Button(win , text = "BORRAR", command = self.borrar, width = 10,font = 'arial 10', height=1)
        btn_borrar.grid(row=5, column=0, pady=20)
        btn_borrar.configure(bg = color[5])

        self.mensaje = tkinter.Listbox(win, height = 6, width = 70 , font = 'arial 12' )
        self.mensaje.insert("end" , ' Registre esta información...')
        self.mensaje.grid(row = 7, columnspan = 4, padx=10)

        win.pack()
