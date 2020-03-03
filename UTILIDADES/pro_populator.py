import mysql.connector
import random
import datetime
import CONF_APUNTO

cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password,
                                      host = CONF_APUNTO.host, database = CONF_APUNTO.database1)
cursor = cnx.cursor()
q1 = 'SELECT idnum, nname FROM plist'
# print(q1)
cursor.execute(q1)

pro = []
for r in cursor:
    # print(r)
    pro.append(r)
cursor.close()
cnx.close()

pro = random.sample(pro, 15)
cnx = mysql.connector.connect(user=CONF_APUNTO.user, password=CONF_APUNTO.password,
                              host=CONF_APUNTO.host, database=CONF_APUNTO.database2)
cursor = cnx.cursor()
for p in pro:
    # print(p)
    codigo = p[0]
    cedula = random.randint(1700000000, 1799999999)
    nombre = p[1]
    ruc = (cedula*1000)+1
    fecnac = datetime.date(year=1900, month=1, day=1) + datetime.timedelta(days=random.randint(18264, 36526))
    genero = random.choice(('M', 'F'))
    sap = 100000000 + codigo

    q2 = f"INSERT INTO proveedor (pro_codigo, pro_cacreg, pro_cedula, pro_nombre, pro_ruc, pro_fecnac, pro_genero, " \
         f"pro_estado, pro_sap, ope_codigo) VALUES( {codigo}, 1000, {cedula}, '{nombre}', {ruc}, '{fecnac}', " \
         f"'{genero}', 1, {sap}, 711)"
    print(q2)
    cursor.execute(q2)
    cnx.commit()
cursor.close()
cnx.close()




