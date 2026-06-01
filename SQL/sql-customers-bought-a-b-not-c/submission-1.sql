-- Write your query below
with a as(select distinct customer_id from orders where product_name ='A')
,b as(select distinct customer_id from orders where product_name ='B') 
,c as (select distinct customer_id from orders where product_name ='C')
,d as(select customers.* from a inner join b on a.customer_id = b.customer_id inner join customers on a.customer_id = customers.customer_id)--inner join c on c.customer_id != a.customer_id and c.customer_id != b.customer_id

select * from d where d.customer_id not in (Select distinct customer_id from c ) order by d.customer_name
