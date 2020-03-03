import serial
import time
import CONF_APUNTO
import decimal

if CONF_APUNTO.emulador == 'ON':
        delay = 1.5
else:
        delay = 0.05

# print('Emulador:', delay)


def scale_read(port='COM1'):
        """Variable recibe nombre de puerto, COM1 por omicion,
        adquiere valor balanza, retorna line, RX fail si no hay respuesta,
        COM fail si no encuentra puerto"""
        try:            
                scale = serial.Serial(port, timeout=0.1)
                # print ("Port:",scale.name," ready...")
                time.sleep(delay)
                scale.write('R'.encode())
                time.sleep(0.1)
                line = scale.readline()
                # print('Line read:', line, ' LEN:', len(line))
                scale.close()
                if line == '':
                        line = 'RX fail'
                # print (line)
                return line.decode()
        except:
                # print (f'{port} fail')
                return f'{port} fail'


def scale_zero(port='COM1'):
        """Variable recibe nombre de puerto, COM1 por omicion,
        encera balanza,retorna line, RX fail si no hay respuesta,
        COM fail si no encuentra puerto"""
        try:
                scale = serial.Serial(port, timeout=0.1)
                # print ("Port:",o_scale.name," ready...")
                time.sleep(delay)
                scale.write('Z'.encode())
                time.sleep(0.1)
                scale.write('R'.encode())
                time.sleep(0.1)
                line = scale.readline()
                scale.close()
                if line == b'':
                        return 'RX fail'
                # print (line)
                return line.decode()
        except:
                # print (f'{port} fail')
                return f'{port} fail'


def scale_parse(line):
        """Variable recibe line y retorna numero decimal del peso en KG
        o False si no es numero"""
        # print line[2:10],line
        line = line
        if line[1] == '-':
                value = decimal.Decimal('-' + line[2:10].strip(' '))
        else:
                value = decimal.Decimal(line[2:10].strip(' '))
        return value
