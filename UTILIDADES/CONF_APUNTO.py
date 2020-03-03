import configparser

config = configparser.ConfigParser()
config.read('CONF_APUNTO.ini')


cliente = config['NOMBRE']['NOMBRE']

user = config['DB']['USER']
password = config['DB']['PASSWORD']
host = config['DB']['HOST']
database = config['DB']['DATABASE']

sc_com = config['SERIAL']['SCALE_COM']
pr_com = config['SERIAL']['PRINTER_COM']

icon_path = config['ICON']['ICON_PATH']

emulador = config['MODO']['EMULADOR']

logo_path = config['IMAGE']['IMAGE_PATH']

# for pw in (cliente, user, password, host, database, sc_com, pr_com, icon_path, emulador, logo_path):
#     print(pw)
