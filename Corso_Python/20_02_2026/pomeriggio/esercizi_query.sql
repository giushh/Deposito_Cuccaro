/* scrivere una query che restituisca solo i record dalla tabella "products" con un prezzo superiore a 50*/

select * from products where buyPrice > 50
order by buyPrice DESC;

-- query che elimini tutti gli ordini da orders con stato cancelled
create table orders_copy as select * from orders;

-- SET SQL_SAFE_UPDATES = 0;

select status from orders_copy where status = "Cancelled";
delete from orders_copy where status = 'Cancelled';
-- drop table orders_copy;
SET SQL_SAFE_UPDATES = 1;

/* restano dei record orfani cosi, perche gli stessi ordini sono in orderdetails
quindi fai

delete from ordersdetails
where ordernumber IN (
	select ordernumber from orders where status = "Cancelled"
    )
e non lascia nessuna informazione penzolante*/