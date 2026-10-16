CREATE USER movie_user WITH PASSWORD 'movie_password';
CREATE DATABASE movie OWNER movie_user;
CREATE USER customer_user WITH PASSWORD 'customer_password';
CREATE DATABASE customer OWNER customer_user;
