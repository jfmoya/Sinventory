#lista de socios activos
select idnum, nname from plist;

#total transacciones por dia, incluye correcciones del dia 
select idnum, date(hora), weight from transaccion
	where date(hora) = '2018-3-1';

# total por dia por idnum todos idnum que entregaron el dia
select idnum, date(hora), sum(weight) as tot_dia 
	from transaccion
	where date(hora) = '2018-3-1'
    group by idnum;
    
#join de plist con total dia por socio
select a.idnum, a.nname, b.tot_dia 
	from plist a left join (	select idnum, date(hora), sum(weight) as tot_dia
						from transaccion
						where date(hora) = '2018-3-3'
						group by idnum)b
	using (idnum);

#total join de 2 subqueries 
select idnum, nname, a.tot_dia as tot_dia_a , b.tot_dia as tot_dia_b
	from plist left join (select idnum,  sum(weight) as tot_dia from transaccion where date(hora) = '2018-3-3' group by idnum) a using (idnum) left join 
						 (select idnum,  sum(weight) as tot_dia from transaccion where date(hora) = '2018-3-4' group by idnum) b using (idnum);
                         
select idnum, nname, d3.tot as '2018-03-03' , d4.tot as '2018-03-04', t.total
	from plist left join (select idnum,  sum(weight) as tot from transaccion where date(hora) = '2018-3-3' group by idnum) d3 using (idnum) left join 
						 (select idnum,  sum(weight) as tot from transaccion where date(hora) = '2018-3-4' group by idnum) d4 using (idnum) left join
                         (select idnum, sum(weight) as total from transaccion where date(hora) >= '2018-03-03' and date(hora) <= '2018-03-04' group by idnum) t using (idnum);
         
         
select idnum, date(hora), sum(weight) as tot_dia from transaccion	where date(hora) = '2018-3-2' group by idnum;



select idnum, sum(weight) as total from transaccion where date(hora) >= '2018-03-03' and date(hora) <= '2018-03-03' group by idnum;