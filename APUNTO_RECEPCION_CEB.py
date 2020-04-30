import tkinter
import scale_serial_CAS_p3 as scale_serial_p3
import scale_sql_p3
import scale_ep_p3
import CONF_APUNTO


caso = [0]
idnum = [0]
name = ['']
# peso_neto, num_gavetas, peso_gaveta, tara, peso_bruto
peso_l = [0, 0, 0, 0, 0, 0]
cac_codigo = scale_sql_p3.cac_codigo_r()  # DEFAULT
cac_nombre = scale_sql_p3.cac_nombre_r()  # DEFAULT
prd_codigo = CONF_APUNTO.prd_codigo  # SETTING
rate = scale_sql_p3.prd_preciokg_r(prd_codigo)  # QUERY DE prd_codigo
peso_gaveta = scale_sql_p3.tara_r()  # QUERY DE prd_codigo
f_merma = scale_sql_p3.merma_r()  # QUERY DE prd_codigo
totdia = [scale_sql_p3.totdia()]
# FUNCIONES


def caso0():
    """Verifica comunicacion con balanza usando scale_serial_p3.zero(), zeroes scale,  verifica
    existencia de pro_codigo ingresado en base, recobra nombre relacionado,
    pregunta veracidad del nombre,  si name[0] vacío borra y caso[0] no cambia,
    registra numero en caso a seguir"""
    lbl_3.config(text=f'Peso Neto:...Kg \t\t Gavetas:...')
    lbl_4.config(text=f'Peso Bruto:...Kg \t\t Tara:...Kg \t Merma:...Kg')
    line = scale_serial_p3.scale_zero(CONF_APUNTO.sc_com)
    mensaje.config(bg='white')
    if line == 'RX fail' or line == f'{CONF_APUNTO.sc_com} fail':
        mensaje.delete(0, 'end')
        txt_in.delete(0, 'end')
        mensaje.insert('end', line + '. Revise coneccion de balanza')
    else:
        idnum[0] = txt_in.get()
        name[0] = scale_sql_p3.namer(idnum[0])
        if name[0] != '':
            txt_in.delete(0, 'end')
            lbl_2.config(text=f"#{idnum[0]} {name[0]}")
            mensaje.delete(0, 'end')
            mensaje.insert('end', 'Verificar Codigo y Nombre correctos?')
            caso[0] = 1
        else:
            txt_in.delete(0, 'end')
            lbl_2.config(text="#SOCIO")
            mensaje.delete(0, 'end')
            mensaje.insert("end", ' VERIFIQUE QUE LA BALANZA ESTE VACÍA.')
            mensaje.insert("end", ' Ingrese número de SOCIO...')


def caso1():
    """Exhibe mensaje nombre colocar producto, ingresar numero de gavetas
    en pantalla, registra numero en caso a seguir"""
    # print ('caso1')
    if txt_in.get() == '':
        mensaje.delete(0, 'end')
        mensaje.insert('end', ' - Colocar producto en la balanza, esperar estabilidad en lector')
        mensaje.insert('end', ' - INGRESAR EL NÚMERO DE GABETAS')
        caso[0] = 2
    else:
        caso[0] = 0
        seguir()


def caso2():
    """Retorna texto en boton seguir, recobra peso registrado en balanza,
    imprime mensaje del registro a grabar, inserta transaccion en base de datos,
     imprime transaccion, reanuda boton cancelar"""
    # print ('caso2')
    num_gavetas = txt_in.get()
    try:
        # print('tryyy', num_gavetas, type(num_gavetas))
        num_gavetas = int(num_gavetas)
        txt_in.delete(0, 'end')
        if num_gavetas < 25:
            peso_bruto = scale_serial_p3.scale_parse(scale_serial_p3.scale_read(CONF_APUNTO.sc_com))  # DEC(6,2)
            tara = peso_gaveta * num_gavetas
            peso_neto0 = peso_bruto - tara
            merma = peso_neto0 * f_merma
            peso_neto = round(peso_neto0 - merma, 3)  # DEC(*,3)
            peso_l[0], peso_l[1], peso_l[2], peso_l[3], peso_l[4], peso_l[5] = \
                peso_neto, num_gavetas, peso_gaveta, tara, peso_bruto, merma
            # print('peso_l', peso_l)
            mensaje.delete(0, 'end')
            mensaje.insert('end', ' - Verifique el Control de Calidad y Valores de la Transacción ')
            mensaje.insert('end', ' - Continuar para Grabar - Cancelar para Retroceder')
            lbl_3.config(text=f'Peso Neto: {peso_neto} Kg\tGavetas: {num_gavetas}')
            lbl_4.config(text=f'Peso Bruto: {peso_bruto} Kg\tTara: {tara} Kg\tMerma: {round(merma, 3)} Kg')
            caso[0] = 3
        else:
            # print('else')
            raise Exception('num_gavetas > 25')
    except:
        txt_in.delete(0, 'end')
        caso[0] = 1
        seguir()
        # print('exccc')


def caso3():
    if txt_in.get() == '':
        if chk_var1.get() and chk_var2.get():
            pro_codigo = int(idnum[0][-3:])
            pro_cacreg = idnum[0][:-3]+'000'
            # cac_codigo = scale_sql_p3.cac_codigo_r()
            # prd_codigo = CONF_APUNTO.prd_codigo # Usar con query en caso de cambio de producto
            # rate = scale_sql_p3.prd_preciokg_r(prd_codigo) # Usar en caso de prd_preciokg tiempo real
            tra_valor = round(peso_l[0] * rate, 2)  # ROUND context decimal.ROUND_HALF_EVEN , Round to nearest
            # with ties going to nearest even integer
            ope_codigo = CONF_APUNTO.ope_codigo
            # print(pro_codigo, pro_cacreg, cac_codigo, prd_codigo, peso_l[4], peso_l[2], peso_l[3], peso_l[0],
            #       tra_valor, ope_codigo)
            scale_sql_p3.saver(pro_codigo, pro_cacreg, cac_codigo, prd_codigo, peso_l[4], peso_l[1], peso_l[3],
                               peso_l[0], tra_valor, ope_codigo, peso_l[5])
            mensaje.delete(0, 'end')
            mensaje.config(bg='#eee860')
            mensaje.insert('end', ' - Transaccion Grabada.       RETIRE EL PRODUCTO')
            mensaje.insert('end', ' - Ingrese número de SOCIO...')
            (tra_fecreg, tra_codigo, tra_pesoneto) = scale_sql_p3.entrega()
            total_ac = scale_sql_p3.acum(idnum[0])
            totdia[0] = scale_sql_p3.totdia()
            lbl_5.config(text=f"TOTAL DÍA: {totdia[0]}Kg                 ")
            scale_ep_p3.epsonprint(cac_nombre, idnum[0], name[0], tra_fecreg, tra_codigo, tra_pesoneto, tra_valor,
                                   total_ac)
            caso[0] = 0
    else:
        caso[0] = 2
        seguir()


flist = [caso0, caso1, caso2, caso3]


def seguir():
    """Ejecuta funcion caso # segun registro en lista"""
    flist[caso[0]]()
    chck_1.deselect()
    chck_2.deselect()


def cancelar():
    """Retorna a inicio caso 0"""
    if caso[0] == 0:
        seguir()
    elif caso[0] == 1:
        caso[0] = 0
        seguir()
    elif caso[0] == 2:
        caso[0] = 0
        seguir()
    elif caso[0] == 3:
        caso[0] = 2
        lbl_3.config(text=f'Peso Neto:...Kg \t\t Gavetas:...')
        lbl_4.config(text=f'Peso Bruto:...Kg \t\t Tara:...Kg \t Merma:...Kg')
        seguir()


def returnkey(a):
    """ Handler del bind al key Return
    ejecuta seguir() retorna "break" para no pasar el char asignado """
    # print ('You pressed ENTER', a, ':',a.keysym)
    seguir()
    return "break"


def minuskey(a):
    """ Handler del bind al key minus
    ejecuta cancelar() retorna "break" para no pasar el char asignado """
    # print ('You pressed - :', a, ':',a.keysym)
    cancelar()
    return "break"


def pluskey(a):
    if chk_var1.get() == 0:
        chck_1.select()
        chck_2.select()
    else:
        chck_1.deselect()
        chck_2.deselect()
    return "break"


color = {'azul': '#14397e', 'celeste': '#40b1e5', 'naranja': '#f5861f', 'fucsia': '#d60761',
         'rojo': '#9d0000', 'verde': '#228b22', 'd_gris': '#30313D', 'l_gris': '#8487A8'}

win_ST = [1]


def minwin(key):
    if win_ST[0]:
        win.attributes("-fullscreen", False)
        win_ST[0] = 0
        # print('minwin', ST[0])
    else:
        win.attributes("-fullscreen", True)
        win_ST[0] = 1
        # print('minwin', ST[0])


# GUI  ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: ###
win = tkinter.Tk()
win.attributes("-fullscreen", True)
win.bind("<F11>", minwin)
win.configure(bg=color['azul'])
try:
    win.iconbitmap(CONF_APUNTO.icon_path)
except:
    pass
win.title("APunto")
size = CONF_APUNTO.size
sd = {'S': ['1366x768', 10, 7, 6, 2, 12, 2, 15, 12, 2, 15, 1316, 65, 10, 10],
      'M': ['1550x800', 20, 15, 10, 5, 15, 3, 10, 15, 3, 10, 1550, 70, 20, 20]}
win.geometry(sd[size][0])
# -----------------------------------------------------------------------------------------
lbl_1 = tkinter.Label(win, text=f'  {cac_nombre}', anchor="w", bg=color['azul'], font='arial 16',
                      fg=color['celeste'])
lbl_1.grid(columnspan=2, pady=5, sticky="EW")
# -----------------------------------------------------------------------------------------
txt_in = tkinter.Entry(win, width=6, font='arial 50')
"""binder klick"""
txt_in.bind('<Return>', returnkey)
txt_in.bind('<minus>', minuskey)
txt_in.bind('<+>', pluskey)
"""end binder klick"""
txt_in.focus_set()
txt_in.grid(columnspan=2, padx=15, pady=10, sticky="w")
# -----------------------------------------------------------------------------------------
lbl_2 = tkinter.Label(win, text="#SOCIO", bg=color['azul'], font='arial 42 bold', anchor="w",
                      fg=color['celeste'])
lbl_2.grid(columnspan=2, pady=sd[size][1], sticky="EW")
# -----------------------------------------------------------------------------------------
mensaje = tkinter.Listbox(win, height=2, font='arial 30')
mensaje.insert("end", ' VERIFIQUE QUE LA BALANZA ESTE VACÍA.')
mensaje.insert("end", ' Ingrese número de SOCIO...')
mensaje.grid(columnspan=2, padx=sd[size][2], sticky="EW")
# -----------------------------------------------------------------------------------------
lbl_3 = tkinter.Label(win, height=2, text="Peso Neto:...Kg \t\t Gavetas:...", bg=color['azul'],
                      font='arial 35 bold', anchor="w", fg=color['celeste'])
lbl_3.grid(columnspan=2, pady=sd[size][3], sticky="EW")
# -----------------------------------------------------------------------------------------
lbl_4 = tkinter.Label(win, height=2, text="Peso Bruto:...Kg \t\t Tara:...Kg \t Merma:...Kg", bg=color['azul'],
                      font='arial 16', anchor="nw", fg=color['celeste'])
lbl_4.grid(columnspan=2, pady=sd[size][4], sticky="EW")
# -----------------------------------------------------------------------------------------
chk_var1 = tkinter.IntVar()
chck_1 = tkinter.Checkbutton(win, text="Control de Calidad Aprobado", variable=chk_var1, onvalue=1, offvalue=0,
                             font='arial 10 bold', bg=color['l_gris'], width=30, anchor="w")
chck_1.grid(padx=30, sticky="W")
# -----------------------------------------------------------------------------------------
chk_var2 = tkinter.IntVar()
chck_2 = tkinter.Checkbutton(win, text="Peso Neto y Transaccion Aprobada", variable=chk_var2, onvalue=1, offvalue=0,
                             font='arial 10 bold', bg=color['l_gris'], width=30, anchor="w")
chck_2.grid(padx=30, sticky="W")
# -----------------------------------------------------------------------------------------
lbl_5 = tkinter.Label(win, height=1, text=f"TOTAL DÍA: {totdia[0]}Kg                 ", bg=color['azul'],
                      font='arial 15 bold', fg=color['l_gris'], anchor='e')
lbl_5.grid(column=1, row=6, rowspan=2, sticky="EW")
# -----------------------------------------------------------------------------------------
btn_cancelar = tkinter.Button(win, text="CANCELAR", command=cancelar, width=sd[size][5], font='arial 15 bold',
                              fg=color['l_gris'], height=sd[size][6])
btn_cancelar.grid(row=8, column=0, pady=sd[size][7])
btn_cancelar.configure(bg=color['rojo'])
# -----------------------------------------------------------------------------------------
btn_enter = tkinter.Button(win, text="CONTINUAR", command=seguir, width=sd[size][8], font='arial 15 bold',
                           fg=color['d_gris'], height=sd[size][9])
btn_enter.grid(row=8, column=1, pady=sd[size][10])
btn_enter.configure(bg=color['verde'])
# -----------------------------------------------------------------------------------------
try:
    logo2 = tkinter.PhotoImage(file=CONF_APUNTO.logo2_path)
    lbl_6 = tkinter.Label(win, image=logo2, width=sd[size][11], height=sd[size][12], anchor="e")
    lbl_6.grid(pady=sd[size][13], columnspan=2)
except:
    lbl_6 = tkinter.Label(win, text=f'  {cac_nombre}', width=132, anchor="e", bg='dark blue', font='arial 16',
                          fg=color['celeste'])
    lbl_6.grid(columnspan=2, pady=sd[size][14], sticky="EW")

win.mainloop()
