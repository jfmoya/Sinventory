import mysql.connector
import CONF_APUNTO
import random

cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password ,
                              host = CONF_APUNTO.host , database = CONF_APUNTO.database)
cursor = cnx.cursor()

cursor.execute("SELECT idnum FROM plist")
idnum_L = [i[0] for i in cursor]


for num in idnum_L:
  ci = ''
  for digit in range(10):
    ci += str(random.randint(0,9))

  query = 'UPDATE plist SET ci ="'+ ci +'"WHERE idnum = '+ str(num)
  cursor.execute(query)
  cnx.commit()
  print (query)
   
cursor.close()
cnx.close()



input('Presione ENTER para salir')
