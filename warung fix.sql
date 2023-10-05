drop database if exists warung_kebun_kita;

create database warung_kebun_kita;

use warung_kebun_kita;

-- table for lookup products

create table product_lookup (
    barcode int primary key,
    product_name varchar(50) not null,
    price_per_item int not null,
    item_per_box int not null
);

-- table for product out

create table product_sales (
    sales_id int auto_increment,
    barcode int,
    time_sale datetime not null,
    primary key (sales_id),
	foreign key (barcode) references product_lookup(barcode) on delete cascade
);

-- table for product in

create table product_stock (
    stock_id int auto_increment,
    barcode int,
    box int not null,
    product_in datetime not null,
    price_per_box int not null,
    primary key (stock_id),
	foreign key (barcode) references product_lookup(barcode) on delete cascade
);

-- table for missing products

create table product_missing (
    missing_id int auto_increment,
    barcode int,
    product_item int not null,
    date_of_knowing datetime not null,
    primary key (missing_id),
	foreign key (barcode) references product_lookup(barcode) on delete cascade
);