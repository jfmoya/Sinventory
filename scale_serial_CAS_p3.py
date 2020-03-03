import serial
import time
import CONF_APUNTO
import decimal
# import itertools

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
            scale.write(b'\x00')
            time.sleep(0.1)
            line = scale.readline()
            # print('Line read:', line, '9:17 = ', line[9:17], ' LEN:', len(line))
            scale.close()
            if line == '':
                    line = 'RX fail'
            # print (line)
            return line
        except:
            # print (f'{port} fail')
            return f'{port} fail'


# print(scale_read('com5'))


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
            scale.write(b'\x00')
            time.sleep(0.1)
            line = scale.readline()
            scale.close()
            if line == b'':
                    return 'RX fail'
            # print (line)
            return line
        except:
            # print (f'{port} fail')
            return f'{port} fail'

# print(scale_zero('COM5'))

def scale_parse(line):
        """Variable recibe line y retorna numero decimal del peso en KG
        o False si no es numero"""
        # print(line.decode('1252'))
        line = line[9:17].decode('1252').replace(' ', '')
        value = decimal.Decimal(line)
        return value


# print(scale_parse(scale_read('com5')))
# print(scale_parse(scale_zero('com5')))


# n = 0
# hex_chars = 'abcd'
# hex_comands = [n2+n1 for n2 in hex_chars for n1 in hex_chars]
# for i in hex_comands:
#     n += 1
#     print(n, ' ', i)
# n = 0
# hex_comands2 = itertools.product('ABCD', repeat=2)
# for i in hex_comands2:
#     n += 1
#     print(n, ' ', i)
# scale.write(b'\x00')
# scale.write(bytes.fromhex('00'))


