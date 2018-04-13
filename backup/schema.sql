--schema.sql

drop database if exists awesome

create database awesome

use awesome

grant select, insert, update, delete on awesome.* to 'root'@'localhost' identified by '68582188'

create table users(
    `id` varchar(50) not null
    `email` varchar(50) not null,
    
)