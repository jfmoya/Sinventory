import serial
import time
import CONF_APUNTO

"""Envia comandos al arduino, emulador de balanza. R para pedir datos,
Z para poner balanza en 0, y Q o q para salir. Imprime mensaje enviado, tipo y mensaje
recivido del emulador."""


TX = ''
scale = serial.Serial(CONF_APUNTO.sc_com, timeout = 0.2)

while TX != 'Q' and TX != 'q':
    TX = input('Input DATA: ')
    if TX != 'Q' and TX != 'q':
        if TX == 'Z' or TX == 'R':
##            TX = TX.encode()
            print(TX, type(TX))
            scale.write(TX.encode())
            print ('Msg SENT:', TX, type(TX))
            time.sleep(0.2)
            print ('Delay 0.2s')
            line = scale.readline()
            print ('Line read:', line, ' LEN:', len(line))
    

    
print ('Bye Bye')
scale.close()
time.sleep(2)




