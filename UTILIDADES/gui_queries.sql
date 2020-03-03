
select num , hora, weight from transaccion 
	where idnum = 79 and hora in 
    (select max(hora) from transaccion where idnum = 79);
    

#select date(concat(year(curdate()),'-',month(curdate()),'-',26 ));
#select date(concat(year(curdate()-interval 1 month),'-',month(curdate()-interval 1 month),'-',26 ));
#select date(concat(year(curdate()),'-',month(curdate()),'-',11 ));

#select if(26<= day(curdate()) and day(curdate())<=31, date(concat(year(curdate()),'-',month(curdate()),'-',26 )),null),
#    if(1<= day(curdate()) and day(curdate())<=10, date(concat(year(curdate()-interval 1 month),'-',month(curdate()-interval 1 month),'-',26 )), null),
#    if(11<= day(curdate()) and day(curdate())<=25, date(concat(year(curdate()),'-',month(curdate()),'-',11 )), null);

select if(26<= day(curdate()) and day(curdate())<=31,
	date(concat(year(curdate()),'-',month(curdate()),'-',26 )),
	if(1<= day(curdate()) and day(curdate())<=10, 
	date(concat(year(curdate()-interval 1 month),'-',month(curdate()-interval 1 month),'-',26 )), 
	if(11<= day(curdate()) and day(curdate())<=25, 
	date(concat(year(curdate()),'-',month(curdate()),'-',11 )), null)));



select round(sum(weight),2) from transaccion
	where idnum = 95 and curdate()>= 
    if(26<= day(curdate()) and day(curdate())<=31,
	date(concat(year(curdate()),'-',month(curdate()),'-',26 )),
	if(1<= day(curdate()) and day(curdate())<=10, 
	date(concat(year(curdate()-interval 1 month),'-',month(curdate()-interval 1 month),'-',26 )), 
	if(11<= day(curdate()) and day(curdate())<=25, 
	date(concat(year(curdate()),'-',month(curdate()),'-',11 )), null)));


SELECT SUM(weight) FROM transaccion WHERE idnum = 60 AND DATE(hora) >= 
	IF (26 <= DAY(CURDATE()) AND DAY(CURDATE()) <= 31, DATE_FORMAT(CURDATE(),'%Y-%m-26'),
    IF (1 <= DAY(CURDATE()) AND DAY(CURDATE()) <= 10, DATE_FORMAT(CURDATE(),'%Y-%m-26') - INTERVAL 1 MONTH,
    IF (11 <= DAY(CURDATE()) AND DAY(CURDATE()) <= 25, DATE_FORMAT(CURDATE(),'%Y-%m-11'), NULL)));

