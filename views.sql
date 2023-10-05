create view missing_view as
select lookup.product_name, sum(missing.product_item) as missing_item
from missing
join lookup
on lookup.barcode = missing.barcode
group by product_name;

create view sales_view as
select lookup.product_name, sales.time_sales
from sales
join lookup on lookup.barcode = sales.barcode;