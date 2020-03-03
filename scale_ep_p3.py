import serial
import CONF_APUNTO


def epsonprint(cac_nombre, idnum, pro_nombre, tra_fecreg, tra_codigo, tra_pesoneto, tra_valor, total_ac):
    """Usa 3 line variables, emite comando ESC/POS setea impresora codec
    cp1252, imprime ticket"""

    epson = serial.Serial(CONF_APUNTO.pr_com)

    epson.write('\x1b\x74\x10'.encode('cp1252'))
    epson.write('\x1b\x72\x01'.encode('cp1252'))
    epson.write(f'-El Ordeño- {cac_nombre}\n'.encode('cp1252'))
    epson.write('\x1b\x72\x00'.encode('cp1252'))

    lines = f'{idnum}-{pro_nombre}\n' \
            f'{tra_fecreg}     T#{tra_codigo}\n' \
            f'Entrega: {tra_pesoneto}Kg  ${tra_valor}  Acum: {total_ac}\n'

    epson.write(lines.encode('cp1252'))

    for i in range(5):
        epson.write('\n'.encode('cp1252'))

    epson.close()
