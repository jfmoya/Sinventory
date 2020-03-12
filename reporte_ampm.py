import tkinter
import scale_sql_p3
import csv
import CONF_APUNTO

class RAmPm:
    def grabar(self):
        f1, f2 = self.txt_in1.get(),self.txt_in2.get()
        rep = scale_sql_p3.reporte2(f1, f2)
        if type(rep[0]) == list:
            rep[0].insert(0,rep[1])
            path = 'R_AM-PM_'+f1+'_'+f2+'.csv'
            r_file = open(path, 'w', newline='')
            writer = csv.writer(r_file, delimiter = ';')
            self.mensaje.delete(0, 'end')
            for line in rep[0]:
                linea = []
                for word in line:
                    if word is None:
                        linea.append('0')
                    else:
                        linea.append(str(word).replace('.',','))

                writer.writerow(linea)
                m_line = ''
                for i in linea:
                    m_line += str(i)+' - '
                self.mensaje.insert('end', m_line[:-2])
    ##            print linea
            r_file.close()
        else:
            # print rep[0]
            self.mensaje.delete(0, 'end')
            self.mensaje.insert('end', rep[0])


    def borrar(self):
        self.mensaje.delete(0, 'end')
        self.txt_in1.delete(0, 'end')
        self.txt_in2.delete(0, 'end')

    def __init__(self, master):

        color = ('#99c6f0','#9fd6f0','#c6e3f9','#ecf8f9','#ecf1f2','#f25235','#eee860','#64f28a','#3749ac')
        win = tkinter.Frame(master)
        
        lbl_1 = tkinter.Label(win, text='text',
                                bg = color[0], font = 'arial 14', fg = color[8])
        lbl_1.grid(columnspan = 2, pady=10)

        lbl_2 = tkinter.Label(win, text="REPORTE DE PRODUCTO ENTREGADO, POR SOCIO, \n TOTAL POR TURNO, PERIODO MÁXIMO 16 DÍAS",
                                bg = color[0], font = 'arial 16')
        lbl_2.grid(columnspan = 2, pady=10)

        lbl_3 = tkinter.Label(win, text="Desde AAAA-MM-DD", bg = color[2],font = 'arial 10')
        lbl_3.grid(column = 0 ,row = 3, pady=5)
        lbl_4 = tkinter.Label(win, text="Hasta AAAA-MM-DD", bg = color[2],font = 'arial 10')
        lbl_4.grid(column = 1,row = 3, pady=5)

        self.txt_in1 = tkinter.Entry(win, width = 10, font = 'arial 12')
        self.txt_in1.focus_set()
        self.txt_in1.grid(row = 4,column = 0, pady=10)
        self.txt_in2 = tkinter.Entry(win, width = 10, font = 'arial 12')
        self.txt_in2.grid(row = 4,column = 1, pady=10)

        btn_grabar = tkinter.Button(win , text = "Crear CSV", command = self.grabar, width = 10,font = 'arial 12', height=2)
        btn_grabar.grid(row=5, column=1, pady=20)
        btn_grabar.configure(bg = color[7])

        btn_borrar = tkinter.Button(win , text = "BORRAR", command = self.borrar, width = 10,font = 'arial 10', height=1)
        btn_borrar.grid(row=5, column=0, pady=20)
        btn_borrar.configure(bg = color[5])

        self.mensaje = tkinter.Listbox(win, height = 18, width = 70 , font = 'arial 12' )
        self.mensaje.grid(row = 6, columnspan = 2, padx=10)

        win.pack()


root = tkinter.Tk()
app = RAmPm(root)
root.mainloop()
