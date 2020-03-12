import mysql.connector
import datetime
import CONF_APUNTO
import decimal


def isin(pro_codigo):
    """Argumento pro_codigo cifra en texto, prueba int para evitar insert attack, retorna 1 o 0 si pro_
    codigo existe en tabla proveedor"""
    try:
        int(pro_codigo)
    except:
        # print('not int')
        return 0
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT ' + pro_codigo + ' IN(SELECT pro_codigo + pro_cacreg FROM proveedor)'
    # print (q1)
    cursor.execute(q1)
    for (r,) in cursor:
        # print('cursor: ', cursor, '\n', r)
        pass
    cursor.close()
    cnx.close()
    return r


def namer(pro_codigo):
    """Argumento pro_codigo en str, retorna nombre si tabla existe en tabla proveedor o '' si no existe en tabla"""
    if isin(pro_codigo):
        cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                      host=CONF_APUNTO.host, database=CONF_APUNTO.database)
        cursor = cnx.cursor()
        q1 = 'SELECT pro_nombre FROM proveedor WHERE pro_codigo + pro_cacreg =' + pro_codigo
        # print (q1)
        cursor.execute(q1)
        for r in cursor:
            # print('cursor: ', cursor, r, r[0])
            pass
        cursor.close()
        cnx.close()
        return r[0]
    else:
        return ''


def proveedor_r(codigo):
    """Argumento codigo en str, retorna datos de proveedor tabla existe en tabla proveedor
     ó '' si no existe en tabla"""
    if isin(codigo):
        cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                      host=CONF_APUNTO.host, database=CONF_APUNTO.database)
        cursor = cnx.cursor()
        q1 = f'SELECT CAST(pro_ruc AS CHAR), pro_nombre, pro_fecnac, pro_direccion, pro_telf, pro_correo ' \
             f'FROM proveedor WHERE pro_codigo + pro_cacreg = {codigo}'
        # print (q1)
        cursor.execute(q1)
        for r in cursor:
            # print('cursor: ', cursor, r, r[0])
            pass
        cursor.close()
        cnx.close()
        # print(r)
        return r
    else:
        return ''


def proveedores_r(cac_codigo):
    """Argumento cac_codigo en str, retorna lista de proveedores en tabla """
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    Q = f'SELECT pro_codigo + pro_cacreg, CAST(pro_ruc AS CHAR), pro_nombre, pro_fecnac, pro_direccion, pro_telf, ' \
        f'pro_correo FROM proveedor WHERE pro_cacreg = {cac_codigo}'
    # print (Q)
    cursor.execute(Q)
    r = cursor.fetchall()
    cursor.close()
    cnx.close()
    # for line in r:
    #     print(line)
    return r


def saver(pro_codigo, pro_cacreg, cac_codigo, prd_codigo, tra_pesobruto, tra_numgavetas, tra_tara, tra_pesoneto,
          tra_valor, ope_codigo, tra_merma):
    """Graba TRANSACCION , argumentos pro_codigo, weight y oper en tabla transaccion"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = f'INSERT INTO transaccion (pro_codigo, pro_cacreg, cac_codigo, prd_codigo, tra_pesobruto, ' \
         f'tra_numgavetas, tra_tara, tra_pesoneto, tra_valor, tra_estado, tra_liquidado, tra_visual, ' \
         f'tra_insectos, tra_limpieza, tra_aceptado, ope_codigo, tra_merma ) VALUES({pro_codigo}, {pro_cacreg}, ' \
         f'{cac_codigo}, {prd_codigo}, {tra_pesobruto}, {tra_numgavetas}, {tra_tara}, {tra_pesoneto}, ' \
         f'{tra_valor}, 1, 0, 1, 1, 1, 1, {ope_codigo}, {tra_merma})'
    # print(q1)
    cursor.execute(q1)
    cnx.commit()
    cursor.close()
    cnx.close()


def totdia():
    """Retorna la suma total del producto entregado en el presente dia, Type decimal"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT SUM(tra_pesoneto) FROM transaccion WHERE DATE(tra_fecreg) = CURDATE()'
    # print (q1)
    cursor.execute(q1)
    for r in cursor:
        pass
    cursor.close()
    cnx.close()
    return r[0]


def entrega():
    """Argumento pro_codigo , retorna tuple(hora, num, weight) de la ultima
    transaccion relacionada con pro_codigo"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT CONCAT(tra_fecreg), tra_codigo, tra_pesoneto FROM transaccion ' \
         'WHERE tra_codigo = (SELECT MAX(tra_codigo) FROM transaccion)'
    # print('entrega', q1)
    cursor.execute(q1)
    for r in cursor:
        # print('entrega', r)
        pass
    cursor.close()
    cnx.close()
    return r


def acum(idnum):
    """Argumento pro_codigo, retorna total acumulado desde el ultimo corte actual para pro_codigo"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = f"SELECT sum(tra_pesoneto) FROM transaccion WHERE pro_cacreg + pro_codigo = {idnum} " \
         f"AND tra_fecreg > last_saturday()"  # last_monday() funcion en MYSQL
    # print (q1)
    cursor.execute(q1)
    for r in cursor:
        pass
    cursor.close()
    cnx.close()
    # print(r[0])
    return r[0]


def t_verify(t_num, t_pro_codigo, t_weight):
    """Argumento t_num , t_pro_codigo y t_weight verifica la valides de los datos del record ,
    1 y fecha si es correcto 0 si falso"""
    t_num, t_pro_codigo, t_weight = int(t_num), int(t_pro_codigo), decimal.Decimal(t_weight)
    cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                  host = CONF_APUNTO.host, database = CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT num, hora, pro_codigo, weight, oper FROM transaccion WHERE num = ' + str(t_num)
    # print (q1)
    cursor.execute(q1)
    r = [r for r in cursor]
    cursor.close()
    cnx.close()
    if len(r) == 0:
        return 0, ''
    num, date, pro_codigo, weight, oper = r[0][0], r[0][1], r[0][2], r[0][3], r[0][4]
    # print(num,date,pro_codigo,type(weight), type(t_weight),oper)
    if t_num == num and t_pro_codigo == pro_codigo and t_weight == weight and oper != 2:
        return 1, str(date)
    else:
        return 0, ''


def t_update(new_pro_codigo, t_num, t_pro_codigo, t_weight ):
    """Argumento new_pro_codigo, t_num, t_pro_codigo, t_weight utiliza t_verify() para comprobar veracidad de ticket,
    isin() para comprobar existencia de new_pro_codigo, actualiza pro_codigo con new_pro_codigo, atualiza oper a valor 2,
    inserta 2 rows para anular invalido y validar nuevo row en transaccion"""
    if isin(new_idnum):
        test = t_verify(t_num, t_idnum, t_weight)
        if test[0]:
            fecha = test[1]
            cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                          host = CONF_APUNTO.host, database = CONF_APUNTO.database)
            cursor = cnx.cursor()
            q1 = 'UPDATE transaccion SET oper = 2 , hora = timestamp("' + str(fecha) + '"), t_stamp = now() WHERE num = ' + t_num
            q2 = 'INSERT INTO transaccion (hora, idnum, weight, oper, t_stamp) VALUES (timestamp("' + fecha + '"),' + t_idnum + ', -' + t_weight + ', 2, now())'
            q3 = 'INSERT INTO transaccion (hora, idnum, weight, oper, t_stamp) VALUES (timestamp("' + fecha + '"),' + new_idnum + ',' + t_weight + ', 3, now())'
            # print q1
            # print q2
            # print q3
            cursor.execute(q1)
            cnx.commit()
            cursor.execute(q2)
            cnx.commit()
            cursor.execute(q3)
            cnx.commit()
            cursor.close()
            cnx.close()
            return 'Corrección exitosa'

        else:
            return 'Transaccion no puede ser modificada'
    else:
        return 'Numero de socio incorrecto'


def loader(archivo):
    """Argumento archivo, lee lista de socios formato con separacion tab, utiliza isin,
    carga nuevos socios a tabla proveedor, retorna mensaje y lista de socios cargados a proveedor,
    para al primer error de formato"""
    try:
        socios = []
        # codec = 'cp1252'
        fname = archivo+'.txt'
        fdata = open(fname, 'r')
        line = ' '
        cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                      host=CONF_APUNTO.host, database=CONF_APUNTO.database)
        curs = cnx.cursor()

        curs.execute("SELECT idnum FROM proveedor")
        idnum_L = [i[0] for i in curs]
        # for n in idnum_L:
        #     print(n, type(n))
        while line != '':
            line = fdata.readline()
            # print (line)
            if line != '':
                pair = line.split("\t")
                pair[1] = pair[1].strip()
                # pair[0], pair[1] = pair[0].decode(codec), pair[1].decode(codec)
                # print (pair[0], pair[1])
                if  int(pair[0]) not in idnum_L:
                    Q = 'INSERT INTO proveedor(idnum ,nname) VALUES(' + pair[0] + ',"' + pair[1]+'")'
                    # Q = u'INSERT INTO proveedor(idnum ,nname) VALUES(' + pair[0] + u',"' + pair[1]+u'")'
                    curs.execute(Q)
                    cnx.commit()
                    socios.append((pair[0]+'  '+pair[1]))
                    # print (Q)
        curs.close()
        cnx.close()
        # print ('CARGA EXITOSA')
        return 'CARGA EXITOSA', socios
    except:
        # print ('ARCHIVO NO TIENE EL FORMATO')
        return 0, 'ARCHIVO NO TIENE EL FORMATO', socios


def p_loader(pro_cacreg='', pro_ruc='', pro_nombre='', pro_fecnac='', pro_direccion='', pro_telf='', pro_correo=''):
    """Ingresa proveedor argumnetos ruc, nombre, fecnac, telf, correo. Verifica que no exista ruc previamente."""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    curs = cnx.cursor()

    Q = f'SELECT {pro_ruc} IN(SELECT pro_ruc FROM proveedor)'
    curs.execute(Q)
    (r,) = curs.fetchone()
    if not r:
        Q = f'INSERT INTO proveedor (pro_cacreg, pro_ruc, pro_nombre, pro_fecnac, ' \
            f'pro_direccion, pro_telf, pro_correo) ' \
            f'VALUES ({pro_cacreg}, "{pro_ruc}", "{pro_nombre}", "{pro_fecnac}", ' \
            f'"{pro_direccion}", "{pro_telf}", "{pro_correo}") '
        # print(Q)
        curs.execute(Q)
        cnx.commit()
        ms = 'Registro exitoso'
    else:
        ms = 'RUC ya registrado'
        # print(ms)

    Q = f'SELECT pro_codigo + pro_cacreg, pro_nombre FROM proveedor WHERE pro_ruc = {pro_ruc} '
    curs.execute(Q)
    r = curs.fetchone()
    # print(r)

    curs.close()
    cnx.close()
    return ms, r


def p_update(pro_ruc='', pro_nombre='', pro_fecnac='', pro_direccion='', pro_telf='', pro_correo=''):
    """Ingresa proveedor argumnetos ruc, nombre, fecnac, telf, correo. Verifica que no exista ruc previamente."""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    curs = cnx.cursor()

    Q = f'UPDATE proveedor ' \
        f'SET pro_nombre = "{pro_nombre}", ' \
        f'pro_fecnac = "{pro_fecnac}", ' \
        f'pro_direccion = "{pro_direccion}", ' \
        f'pro_telf = "{pro_telf}", ' \
        f'pro_correo = "{pro_correo}" ' \
        f'WHERE pro_ruc = {pro_ruc}'
    # print(Q)
    curs.execute(Q)
    cnx.commit()
    ms = 'Actualización exitosa'

    Q = f'SELECT pro_codigo + pro_cacreg, pro_ruc, pro_nombre FROM proveedor WHERE pro_ruc = {pro_ruc}'
    # print(Q)
    curs.execute(Q)
    r = curs.fetchone()
    # print(r)

    curs.close()
    cnx.close()
    return ms, r


def t_correct(new_weight, t_num, t_idnum, t_weight ):
    """Argumento new_idnum, t_num, t_idnum, t_weight utiliza t_verify() para comprobar veracidad de ticket,
    isin() para comprobar existencia de new_idnum, modifica row user = 2, inserta 2 rows para anular invalido
    y validar nuevo row en transaccion"""
    # print ('tcorrect:', new_weight, t_num, t_idnum, t_weight)
    test = t_verify(t_num, t_idnum, t_weight)
    # print (test)
    if test[0]:
        fecha = test[1]
        cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                      host = CONF_APUNTO.host, database = CONF_APUNTO.database)
        cursor = cnx.cursor()
        q1 = 'UPDATE transaccion SET oper = 2 , hora = timestamp("' + str(fecha) + '"), t_stamp = now() WHERE num = ' + t_num
        q2 = 'INSERT INTO transaccion (hora, idnum, weight, oper, t_stamp) VALUES (timestamp("' + fecha + '"),' + t_idnum + ', -(' + t_weight + '), 2, now())'
        q3 = 'INSERT INTO transaccion (hora, idnum, weight, oper, t_stamp) VALUES (timestamp("' + fecha + '"),' + t_idnum + ',' + new_weight + ', 3, now())'
        # print (q1)
        # print (q2)
        # print (q3)
        cursor.execute(q1)
        cnx.commit()
        cursor.execute(q2)
        cnx.commit()
        cursor.execute(q3)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 'Corrección exitosa'

    else:
        return 'Transaccion no puede ser modificada'


def t_insert(fecha, idnum, weight):
    """Argumento fecha, idnum, weight, oper, usa isin() para comprobar existencia de idnum,
    inserta 1 row en transaccion con los datos"""
    # print ('t_insert:', fecha, idnum, weight)
    test = isin(idnum)
    # print (test)
    if test:
         cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                       host = CONF_APUNTO.host, database = CONF_APUNTO.database)
         cursor = cnx.cursor()
         Q = 'INSERT INTO transaccion (hora, idnum, weight, oper, t_stamp) VALUES (timestamp("'+fecha+'"),'+idnum+','+weight+', 3, now())'
         # print (Q)
         cursor.execute(Q)
         cnx.commit()
         cursor.close()
         cnx.close()
         return 'Inserción exitosa'

    else:
         return 'Transaccion no puede ser insertada'


def reporte(inicio, final):
    """Realiza query maximo de 16 dias con fecha inicial y final
    retorna lista de tuples con idnum, nname, sum(weight) por dia
    o retorna mensajes de error cuando las fechas son ilegibles"""
    q1, q2, q3, q4 = 'select idnum, nname', '', ' from proveedor ', ''
    header = ('Socio#','Nombre')
    try:
        dia_i = datetime.datetime.strptime(inicio, '%Y-%m-%d')
        dia_f = datetime.datetime.strptime(final, '%Y-%m-%d')
    except:
        #print ('Fecha incorrecta')
        return 'Fecha incorrecta',''
    inicio, final = dia_i, dia_f
    t_dias = (dia_f-dia_i).days + 1
    # print (dia_i, dia_f, t_dias, inicio, final)
    if dia_f >= dia_i and t_dias <= 16:
        d = 1
        q5 = ' left join(select idnum, round(sum(weight),2) as total from transaccion2 \
        where date(hora) >= "'+dia_i.strftime('%Y-%m-%d')+'" \
        and date(hora) <= "'+dia_f.strftime('%Y-%m-%d')+'" group by idnum) t using(idnum)'
        while dia_i <= dia_f:
            q2 = q2 + ', d'+str(d)+'.tot as "'+dia_i.strftime('%Y-%m-%d')+'"\n'
            q4 = q4 + 'left join (select idnum,  round(sum(weight),2) as tot from transaccion2\
             where date(hora) = "'+dia_i.strftime('%Y-%m-%d')+'" group by idnum) d'+str(d)+' using (idnum)\n'
            # print (dia_i)
            header += (dia_i.strftime('%Y-%m-%d'),)
            dia_i += datetime.timedelta(1)
            d += 1
        header += ('Total periodo',)
        q2 += ' , t.total '
        Q = q1 + '\n' + q2 + q3 + '\n' + q4 + q5
        # print (Q)
        cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                      host = CONF_APUNTO.host, database = CONF_APUNTO.database)
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM transaccion2")
        cursor.execute(f"INSERT INTO  transaccion2 SELECT num, hora, idnum, weight, oper, t_stamp FROM transaccion\
        WHERE DATE(hora) >= DATE('{inicio}') AND DATE(hora) <= DATE('{final}')")
        # cnx.commit()
        cursor.execute(Q)
        rep = []
        for r in cursor:
            rep.append(r)
            # print (r)
        cursor.close()
        cnx.close()
        return rep, header
    else:
        # print ('Rango de fechas incorrecto')
        return 'Rango de fechas incorrecto o excede 16 días',''


def reporte2(inicio, final):
    """Realiza query maximo de 16 dias con fecha inicial y final retorna lista de tuples con idnum, nname,
    sum(weight) por dia AM o PM, o retorna mensajes de error cuando las fechas son ilegibles"""
    q1, q2, q3, q4 = 'select idnum, nname', '', ' from proveedor ', ''
    header = ('Socio#','Nombre')
    try:
        dia_i = datetime.datetime.strptime(inicio, '%Y-%m-%d')
        dia_f = datetime.datetime.strptime(final, '%Y-%m-%d')
    except:
        #print ('Fecha incorrecta')
        return 'Fecha incorrecta',''
    inicio, final = dia_i, dia_f
    t_dias = (dia_f-dia_i).days + 1
    # print (dia_i, dia_f, t_dias)
    if dia_f >= dia_i and t_dias <= 16:
        d = 1
        q5 = ' left join(select idnum, round(sum(weight),2) as total from transaccion2 \
        where date(hora) >= "'+dia_i.strftime('%Y-%m-%d')+'" \
        and date(hora) <= "'+dia_f.strftime('%Y-%m-%d')+'" group by idnum) t using(idnum)'
        while dia_i <= dia_f:
            q2 = q2 + ', d'+str(d)+'am.tot as "'+dia_i.strftime('%Y-%m-%d')+'A"\n'\
                 + ', d'+str(d)+'pm.tot as "'+dia_i.strftime('%Y-%m-%d')+'P"\n'

            AM = '"' + dia_i.strftime('%Y-%m-%d') + ' 00:00:00" and ' + '"' + dia_i.strftime('%Y-%m-%d') + ' 12:00:00"'
            PM = '"' + dia_i.strftime('%Y-%m-%d') + ' 12:00:00" and ' + '"' + dia_i.strftime('%Y-%m-%d') + ' 23:59:59"'

            q4 = q4 + 'left join (select idnum,  round(sum(weight),2) as tot from transaccion2 where \
            (hora between ' + AM + ') group by idnum) d'+str(d)+'am using (idnum)\n'\
            + 'left join (select idnum,  round(sum(weight),2) as tot from transaccion2 where \
            (hora between ' + PM + ') group by idnum) d' + str(d) + 'pm using (idnum)\n'
            # print (dia_i)
            header += (dia_i.strftime('%Y-%m-%d')+'AM',)
            header += (dia_i.strftime('%Y-%m-%d')+'PM',)
            dia_i += datetime.timedelta(1)
            d += 1
        header += ('Total periodo',)
        q2 += ' , t.total '
        Q = q1 + '\n' + q2 + q3 + '\n' + q4 + q5
        # print (Q)
        cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                      host = CONF_APUNTO.host, database = CONF_APUNTO.database)
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM transaccion2")
        cursor.execute(f"INSERT INTO  transaccion2 SELECT num, hora, idnum, weight, oper, t_stamp FROM transaccion\
        WHERE DATE(hora) >= DATE('{inicio}') AND DATE(hora) <= DATE('{final}')")
        # cnx.commit()
        cursor.execute(Q)
        rep = []
        for r in cursor:
            rep.append(r)
            # print (r)
        cursor.close()
        cnx.close()
        return rep, header
    else:
        # print ('Rango de fechas incorrecto')
        return 'Rango de fechas incorrecto o excede 16 días',''


def reporte_t(inicio, final):
    """Reporte transacciones, * query con fecha inicio y dinal, retorna lista de tuples con transacciones"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    Q = f'SELECT column_name FROM information_schema.columns ' \
        f'WHERE table_schema = "apunto_ceb" AND table_name = "transaccion"'
    cursor.execute(Q)
    r0 = cursor.fetchall()
    Q = f'SELECT * FROM transaccion ' \
        f'WHERE DATE(tra_fecreg) >= "{inicio}" AND DATE(tra_fecreg) <= "{final}"'
    # print(Q)
    cursor.execute(Q)
    r1 = cursor.fetchall()
    cursor.close()
    cnx.close()
    return r0, r1


def t_socio(idnum, inicio, final):
    """Realiza query  con idnum,  fecha inicial y final, str, retorna lista de transacciones tuples con num,
     hora y weight o retorna mensajes de error cuando las fechas son ilegibles, lista de transacciones en un
     rango de fechas"""
    try:
        dia_i = datetime.datetime.strptime(inicio, '%Y-%m-%d')
        dia_f = datetime.datetime.strptime(final, '%Y-%m-%d')
        # print (dia_i, dia_f)
    except ValueError:
        # print ('Fecha incorrecta')
        return 'Fecha incorrecta',''
    if dia_f < dia_i:
        return 'RANGO DE FECHAS incorrecto',''
    elif isin(idnum):
        header = namer(idnum)
        cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                      host = CONF_APUNTO.host, database = CONF_APUNTO.database)
        cursor = cnx.cursor()
        Q = 'SELECT num, hora, weight FROM transaccion WHERE idnum = '+idnum+' \
        and date(hora)>= "'+dia_i.strftime('%Y-%m-%d')+'" and date(hora)<="'+dia_f.strftime('%Y-%m-%d')+'" \
        order by hora'
        # print (Q)
        cursor.execute(Q)
        rep = []
        for r in cursor:
            r1 = (r[0], str(r[1]), r[2])
            # print (r1)
            rep.append(r1)
        cursor.close()
        cnx.close()
        return rep, header
    else:
        return ('Numero de socio incorrecto',)


def cac_codigo_r():
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT cac_codigo FROM centro_acopio'
    # print (q1)
    cursor.execute(q1)
    for (r,) in cursor:
        # print('cursor: ', cursor, '\n', r)
        pass
    cursor.close()
    cnx.close()
    return r


def cac_nombre_r():
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT cac_nombre FROM centro_acopio'
    # print (q1)
    cursor.execute(q1)
    for (r,) in cursor:
        # print('cursor: ', cursor, '\n', r)
        pass
    cursor.close()
    cnx.close()
    return r


def producto_u(prd_codigo, prd_nombre, prd_preciokg, prd_taragaveta, prd_merma):
    """Actualiza producto argumnetos codigo, nombre, preciokg, taragaveta, merma"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    curs = cnx.cursor()
    Q = f'UPDATE producto ' \
        f'SET prd_nombre = "{prd_nombre}", ' \
        f'prd_preciokg = {prd_preciokg}, ' \
        f'prd_taragaveta = {prd_taragaveta}, ' \
        f'prd_merma = {prd_merma} ' \
        f'WHERE prd_codigo = {prd_codigo}'
    # print(Q)
    curs.execute(Q)
    cnx.commit()
    ms = 'Actualización exitosa'
    Q = f'SELECT prd_nombre, prd_preciokg, prd_taragaveta, prd_merma FROM producto WHERE prd_codigo = {prd_codigo}'
    # print(Q)
    curs.execute(Q)
    r = curs.fetchone()
    # print(r)
    curs.close()
    cnx.close()
    return ms, r


def producto_r(prd_codigo=''):
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = f'SELECT * FROM producto WHERE prd_codigo = {prd_codigo}'
    # print (q1)
    cursor.execute(q1)
    r = cursor.fetchall()
    cursor.close()
    cnx.close()
    # print(r)
    return r


def prd_preciokg_r(prd_codigo):
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = f'SELECT prd_preciokg FROM producto WHERE prd_codigo = {prd_codigo}'
    # print (q1)
    cursor.execute(q1)
    for (r,) in cursor:
        # print('cursor: ', cursor, '\n', r)
        pass
    cursor.close()
    cnx.close()
    return r


def merma_r(prd_codigo=''):
    """Gets tara de gaveta from product table"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT prd_merma FROM producto WHERE prd_codigo = 100001'
    # print (q1)
    cursor.execute(q1)
    for (r,) in cursor:
        # print('cursor: ', cursor, '\n', r)
        pass
    cursor.close()
    cnx.close()
    # print(r)
    return r


def tara_r(prd_codigo=''):
    """Gets tara de gaveta from product table"""
    cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                                  host=CONF_APUNTO.host, database=CONF_APUNTO.database)
    cursor = cnx.cursor()
    q1 = 'SELECT prd_taragaveta FROM producto WHERE prd_codigo = 100001'
    # print (q1)
    cursor.execute(q1)
    for (r,) in cursor:
        # print('cursor: ', cursor, '\n', r)
        pass
    cursor.close()
    cnx.close()
    return r
