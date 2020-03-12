import tkinter
from tkinter import messagebox
import datetime
import csv
import scale_sql_p3
import os

color = ('#99c6f0', '#9fd6f0', '#c6e3f9', '#ecf8f9', '#ecf1f2', '#f25235', '#eee860', '#64f28a', '#3749ac')
cac_nombre = scale_sql_p3.cac_nombre_r()  # DEFAULT
cac_codigo = scale_sql_p3.cac_codigo_r()  # DEFAULT


class RTrans:
    def exportar(self):
        # print(len(self.lista))
        if len(self.lista) > 1:
            if messagebox.askyesno('Apunto', 'Exportar Reporte?', default='no'):
                deskpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                inicio = datetime.datetime.strptime(self.inicio, '%Y-%m-%d').strftime('%Y%m%d')
                final = datetime.datetime.strptime(self.final, '%Y-%m-%d').strftime('%Y%m%d')
                path = f'{deskpath}\\TRA{inicio}-{final}.csv'
                with open(path, 'w', newline='') as r_file:
                    writer = csv.writer(r_file, delimiter=';')
                    for line in self.lista:
                        writer.writerow(line)
                        # print(line)
                messagebox.showinfo('Apunto', f'Reporte Exitoso\n{path}')
        else:
            self.mensaje.delete(0, 'end')
            self.mensaje.insert(0, 'Generar reporte para exportar')

    def consultar(self):
        self.lista = []
        self.inicio = self.txt_in1.get()
        self.final = self.txt_in2.get()
        try:
            datetime.datetime.strptime(self.inicio, '%Y-%m-%d')
            datetime.datetime.strptime(self.final, '%Y-%m-%d')
            if self.inicio > self.final:
                raise ValueError
            else:
                columns = (0, 1, 5, 6, 7, 8, 9, 10, 11)
                r0, r1 = scale_sql_p3.reporte_t(self.inicio, self.final)
                # print(len(r1))
                if len(r1) != 0:
                    encabezado = [r0[i][0] for i in columns]
                    self.lista.append(encabezado)
                    # print(encabezado)
                    for line in r1:
                        linea = [f'{line[i]}' for i in columns]
                        self.lista.append(linea)
                        # print(linea)
                    self.mensaje.delete(0, 'end')
                    for linea in self.lista:
                        self.mensaje.insert('end', ' :: '.join(linea))
                else:
                    self.mensaje.delete(0, 'end')
                    self.mensaje.insert(0, 'Consulta no genero resultados')
        except ValueError:
            self.mensaje.delete(0, 'end')
            self.mensaje.insert(0, 'Formato de fecha incorrecto')

    def __init__(self, master):
        win = tkinter.Frame(master)
        
        lbl_1 = tkinter.Label(win, text='text', bg=color[0], font='arial 14', fg=color[8])
        lbl_1.grid(columnspan=2, pady=10)

        lbl_2 = tkinter.Label(win, text="REPORTE DE TRANSACCIONES", bg=color[0], font='arial 16')
        lbl_2.grid(columnspan=2, pady=10)

        lbl_3 = tkinter.Label(win, text="Desde AAAA-MM-DD", bg=color[2], font='arial 10')
        lbl_3.grid(column=0, row=3, pady=5)

        lbl_4 = tkinter.Label(win, text="Hasta AAAA-MM-DD", bg=color[2], font='arial 10')
        lbl_4.grid(column=1, row=3, pady=5)

        self.txt_in1 = tkinter.Entry(win, width=10, font='arial 12')
        self.txt_in1.grid(row=4, column=0, pady=10)
        self.txt_in1.focus_set()

        self.txt_in2 = tkinter.Entry(win, width=10, font='arial 12')
        self.txt_in2.grid(row=4, column=1, pady=10)

        btn_consultar = tkinter.Button(win, text="GENERAR", command=self.consultar, width=12, font='arial 11', height=1)
        btn_consultar.grid(row=5, column=0, pady=20)
        btn_consultar.configure(bg=color[0])

        btn_exportar = tkinter.Button(win, text="EXPORTAR", command=self.exportar, width=12, font='arial 11', height=1)
        btn_exportar.grid(row=5, column=1, pady=20)
        btn_exportar.configure(bg=color[7])

        self.mensaje = tkinter.Listbox(win, height=20, width=70, font='arial 11')
        self.mensaje.insert("end", 'Generar reporte para exportar')
        self.mensaje.grid(row=6, columnspan=2, padx=10, pady=10)

        self.lista = []
        self.inicio = ''
        self.final = ''
        
        win.pack()


root = tkinter.Tk()
app = RTrans(root)
root.mainloop()
