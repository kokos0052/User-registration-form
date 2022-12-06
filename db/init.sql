CREATE DATABASE servicedb_database;
CREATE USER admin WITH PASSWORD 'password';
GRANT CONNECT ON DATABASE servicedb_database TO admin;
GRANT USAGE ON SCHEMA public TO admin;
GRANT INSERT ON ALL TABLES IN SCHEMA public TO admin;
