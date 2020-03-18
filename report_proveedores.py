import tkinter
from tkinter import messagebox
import datetime
import csv
import scale_sql_p3
import os

color = ('#99c6f0', '#9fd6f0', '#c6e3f9', '#ecf8f9', '#ecf1f2', '#f25235', '#eee860', '#64f28a', '#3749ac')
cac_nombre = scale_sql_p3.cac_nombre_r()  # DEFAULT
cac_codigo = scale_sql_p3.cac_codigo_r()  # DEFAULT


class RPro:
    def exportar(self):
        if messagebox.askyesno('Apunto', 'Exportar Lista?', default='no'):
            if len(self.lista) != 0:
                deskpath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
                hoy = datetime.datetime.now().strftime('%Y-%m-%d')
                path = f'{deskpath}\\PRO-{hoy}.csv'
                with open(path, 'w', newline='') as r_file:
                    writer = csv.writer(r_file, delimiter=';')
                    for line in self.lista:
                        linea = [str(line[i]).strip() for i in range(7)]
                        writer.writerow(linea)
                        # print(linea)
                messagebox.showinfo('Apunto', f'Reporte Exitoso\n{path}')
            else:
                self.mensaje.insert('end', 'Generar lista para exportar')

    def consultar(self):
        self.lista = scale_sql_p3.proveedores_r(cac_codigo)
        # print(self.lista)
        self.mensaje.delete(0, 'end')
        for line in self.lista:
            # print(line)
            self.mensaje.insert('end', f'{line[0]};{line[1]};{line[2]};{line[3]};{line[4]};{line[5]};{line[6]}')

    def __init__(self, master):
        win = tkinter.Frame(master)

        lbl = tkinter.Label(win, text=cac_nombre, bg=color[0], font='arial 14', fg=color[8])
        lbl.grid(columnspan=2, pady=10, sticky="EW")

        btn_consultar = tkinter.Button(win, text="GENERAR", command=self.consultar, width=12, font='arial 11', height=1)
        btn_consultar.grid(row=7, column=0, pady=5)
        btn_consultar.configure(bg=color[0])

        btn_exportar = tkinter.Button(win, text="EXPORTAR", command=self.exportar, width=12, font='arial 11', height=1)
        btn_exportar.grid(row=7, column=1, pady=5)
        btn_exportar.configure(bg=color[7])

        self.mensaje = tkinter.Listbox(win, height=25, width=80, font='arial 11')
        self.mensaje.insert("end", 'Generar lista para exportar')
        self.mensaje.grid(row=8, columnspan=2, padx=10, pady=10)

        self.lista = []

        win.pack()


# root = tkinter.Tk()
# app = RPro(root)
# root.mainloop()
