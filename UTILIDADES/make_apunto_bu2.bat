@echo off
cd "C:\Program Files\MySQL\MySQL Server 8.0\bin"
mysqldump -u jfmoya -pjfm apunto --result-file="C:\Users\JUANFER\Documents\PYTHON 3\APUNTO 2.0\UTILIDADES\APBU2"%date:~11,4%%date:~8,2%%date:~5,2%_%time:~0,2%%time:~3,2%.sql