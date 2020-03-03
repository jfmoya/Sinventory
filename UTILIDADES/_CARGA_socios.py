import mysql.connector
import CONF_APUNTO
# #codec = 'cp1252'

log = []
fname = input('Ingrese el nombre del archivo: ') + '.txt'
fdata = open(fname, 'r')

document =[]
line = True
while line :
  line = fdata.readline()
  if line != '' and line != '\n':
    pair = line[:-1].split("\t")
    if len(pair) == 2:
      #pair[0], pair[1] = pair[0].decode(codec), pair[1].decode(codec)
      #print(pair)
      document.append(pair)
#print(document)

cnx = mysql.connector.connect(user = CONF_APUNTO.user, password = CONF_APUNTO.password ,
                              host = CONF_APUNTO.host , database = CONF_APUNTO.database)
cursor = cnx.cursor()

cursor.execute("SELECT idnum FROM plist")
idnum_L = [i[0] for i in cursor]
# print(type(idnum_L[0]))

for idn in document:
  try:
    if int(idn[0]) not in idnum_L:
      # query = u'INSERT INTO plist(idnum ,nname) VALUES(' + pair[0] + u',"' + pair[1] + u'")'
      query = 'INSERT INTO plist(idnum ,nname) VALUES(' + idn[0] + ', "' + idn[1] + '")'
      cursor.execute(query)
      cnx.commit()
      print (query)
    # print(idn[0]) 
  except:
    log_i = 'Error de formato: ' + idn[0] + ' - ' + idn[1]
    print(log_i)
    log.append(log_i)
        
cursor.close()
cnx.close()

for l in log:
  print(l)

input('Presione ENTER para salir')
