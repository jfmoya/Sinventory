import mysql.connector
import CONF_APUNTO
import csv

nombre = input(" ingrese el nombre del archivo: ")+".csv"
archivo = open(nombre)
reader = csv.reader(archivo)
#header = next(reader)
data = [row for row in reader]
#print(header)
#print(data)
cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password ,
                              host = CONF_APUNTO.host , database = CONF_APUNTO.database)
cursor = cnx.cursor()

cursor.execute("SELECT idnum FROM plist")
idnum_L = [i[0] for i in cursor]
#print(idnum_L)

cursor.execute("SELECT num FROM transaccion")
num_L = [n[0] for n in cursor]
#print(num_L)

F_idnum = []

for r in data:
    line = r[0].split(';')
    #print(line[0], ',', end = '')
    if (int(line[0]) % 1000) == 0:
      print(line[0])
    if int(line[0]) not in num_L:
      if int(line[2]) in idnum_L:
        if line[5] == 'None':
          line[5] = 'null'
        else:
          line[5] = '"'+line[5]+'"'
        # print (line[0],line[1],line[2],line[3],line[4],line[5])
        Q = 'INSERT INTO transaccion (num, hora, idnum , weight, oper, t_stamp) VALUES("'+\
                line[0]+'","'+line[1]+'","'+line[2]+'","'+line[3]+'","'+line[4]+'",'+line[5]+')'
        cursor.execute(Q)
        cnx.commit()
        print(Q)
      else:
        if line[2] not in F_idnum:
          F_idnum.append(line[2])
          #print ('ID no registrado: ', line[2])
    #else:
      #print ("Duplicado NUM: ", line[0])

cursor.close()
cnx.close()

for j in F_idnum:
  print(j)
input("press to finish")
