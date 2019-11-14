create database library;
use library;

create table books ( book_id int primary key auto_increment, title varchar(30) not null, genre varchar(20) not null, price int not null, available int not null );
create table author ( author_id int primary key auto_increment, name varchar(20) not null );
create table writen ( book_id int not null, author_id int not null );
create table librarian ( employee_id int primary key auto_increment, name varchar(20) not null, salary int not null );
create table issued ( book_id int not null, employee_id int not null );
create table publisher ( pub_id int primary key auto_increment, name varchar(20) not null );
create table published ( pub_id int not null, book_id int not null, author_id int not null );
create table member ( member_id int primary key auto_increment, name varchar(20) not null, phone long, membership_level varchar(10) not null, total_issued int not null );
create table borrowed ( member_id int not null, book_id int not null, issue_date date not null );

alter table writen add foreign key ( book_id ) references books ( book_id );
alter table writen add foreign key ( author_id ) references author ( author_id );
alter table issued add foreign key ( book_id ) references books ( book_id );
alter table issued add foreign key ( employee_id ) references librarian ( employee_id );
alter table published add foreign key ( book_id ) references books ( book_id );
alter table published add foreign key ( author_id ) references author ( author_id );
alter table published add foreign key ( pub_id ) references publisher ( pub_id );
alter table borrowed add foreign key ( member_id ) references member ( member_id );
alter table borrowed add foreign key ( book_id ) references books ( book_id );