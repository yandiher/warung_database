drop database if exists warung_kebun_kita;

create database warung_kebun_kita;

use warung_kebun_kita;

-- table for lookup products

create table product_lookup (
    barcode int primary key,
    product_name varchar(50) not null,
    price_per_unit int not null,
    product_unit int not null
);

-- table for product out

create table product_sales (
    barcode int,
    time_sale datetime not null,
	foreign key (barcode) references product_lookup(barcode) on delete cascade
);

-- table for product in

create table product_stock (
    barcode int,
    box int not null,
    product_in date not null,
    price_per_box int not null,
	foreign key (barcode) references product_lookup(barcode) on delete cascade
);

-- table for missing products

create table product_missing (
    barcode int,
    product_unit int not null,
    date_of_knowing date not null,
	foreign key (barcode) references product_lookup(barcode) on delete cascade
);