@echo off
chcp 65001
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" apunto -e "select * from plist" > "C:\Users\JUANFER\Documents\PYTHON 3\APUNTO 2.0\UTILIDADES\lsocios.txt"
"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql" apunto -e "select * from transaccion" > "C:\Users\JUANFER\Documents\PYTHON 3\APUNTO 2.0\UTILIDADES\ltrans.txt"
pause