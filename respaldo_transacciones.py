import tkinter as tk
from tkinter import messagebox
import scale_sql_p3
import mysql.connector
import datetime
import csv
import CONF_APUNTO

class Res:
    def respaldo(self):
        if messagebox.askyesno('Apunto', 'Puede demorar varios minutos.\n¿Desea continuar?'):
            hoy = datetime.datetime.now().strftime('%Y-%m-%d')
            path = 'RESPALDO_'+hoy+'.csv'

            with open(path, 'w', newline='') as r_file:
                writer = csv.writer(r_file, delimiter = ';')

                cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                              host = CONF_APUNTO.host, database = CONF_APUNTO.database)
                curs = cnx.cursor()
                Q = 'SELECT * from transaccion'
                curs.execute(Q)
                for r in curs:
                    linea = []
                    for w in r:
                        w = str(w)
                        # w = str(w).replace('.',',')
                        # print (w, end='')
                        linea.append(w)
                    writer.writerow(linea)
                    # print ('')
                curs.close()
                cnx.close()
            messagebox.showinfo('Apunto', f'Respaldo Exitoso\n{path}')
            
    def __init__(self, master):
        color = ('#99c6f0','#9fd6f0','#c6e3f9','#ecf8f9','#ecf1f2','#f25235','#eee860','#64f28a','#3749ac')
        win = tk.Frame(master)

        lbl_1 = tk.Label(win, text=CONF_APUNTO.cliente,
                                bg = color[0], font = 'arial 14', fg = color[8])
        lbl_1.grid(columnspan = 2, pady=20)

        lbl_2 = tk.Label(win, text="GENERAR RESPALDO DE TRANSACCIONES",
                                bg = color[0], font = 'arial 16')
        lbl_2.grid(columnspan = 2, pady=20)

        btn_respaldo = tk.Button(win , text = "RESPALDAR", command = self.respaldo, width = 18,font = 'arial 12', height=2)
        btn_respaldo.grid(row=5, columnspan = 2, pady=20)
        btn_respaldo.configure(bg = color[7])

        win.pack()
