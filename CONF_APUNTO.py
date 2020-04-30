import configparser

config = configparser.ConfigParser()
config.read('CONF_APUNTO.ini')

user = config['DB']['USER']
password = config['DB']['PASSWORD']
host = config['DB']['HOST']
database = config['DB']['DATABASE']

sc_com = config['SERIAL']['SCALE_COM']
pr_com = config['SERIAL']['PRINTER_COM']

size = config['SCREEN']['SIZE']

icon_path = config['ICON']['ICON_PATH']

emulador = config['MODO']['EMULADOR']

logo_path = config['IMAGE']['IMAGE_PATH']  # APUNTO

logo2_path = config['IMAGE']['IMAGE2_PATH']  # RECEPCION

prd_codigo = config['PRODUCTO']['PRD_CODIGO']

ope_codigo = config['OPERADOR']['OPE_CODIGO']

# for pw in (cliente, user, password, host, database, sc_com, pr_com, icon_path, emulador, logo_path):
#     print(pw)
