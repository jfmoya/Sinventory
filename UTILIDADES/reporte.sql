select idnum, sum(weight) from transaccion 
	where date(hora) = '2018-02-26'
    group by idnum;

select date(hora), plist.idnum, nname, sum(weight)
	from transaccion inner join plist
	on transaccion.idnum = plist.idnum
	where date(hora) = date('2018-02-26')
    group by idnum;
    

select plist.idnum, nname, weight
	from transaccion2 inner join plist
	on transaccion2.idnum = plist.idnum
	where date(hora) = date('2018-02-20')
    order by idnum;

select  idnum ,date(hora),sum(weight),count(*) from
	(select idnum, weight, hora
		from transaccion2)e
		#where date(hora) = date('2018-02-01'))e
        #group by idnum;
        ;
   
select idnum , 
	sum(case when day(hora) = 1 then weight else 0 end) as '1',
    sum(case when day(hora) = 2 then weight else 0 end) as '2',
    sum(case when day(hora) = 3 then weight else 0 end) as '3',
    sum(case when day(hora) = 4 then weight else 0 end) as '4'
    from transaccion2
    group by idnum;
    
#total dia de todos socios
select date(hora), idnum, sum(weight) ,count(idnum)
	from transaccion
	where date(hora) = '2018-03-01'
    group by idnum;
    
select date(hora), plist.idnum, nname, sum(weight)
	from plist inner join transaccion
	on transaccion.idnum = plist.idnum
	where date(hora) = date('2018-03-01')
    group by idnum;

select curdate();

select round(sum(weight),2) from transaccion where date(hora) > curdate()- interval 1 day;

select round(sum(weight),2) from transaccion where date(hora) = curdate();