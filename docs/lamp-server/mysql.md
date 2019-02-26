# MySQL Database

MySQL has become one of the most popular database management systems in the world. It can be used for small development projects to large and prestigious sites on the web. MySQL has proven itself to be solid, reliable, fast and trusted to all sorts of data storage needs.

MySQL and MariaDB are open source and free to use. This makes it one of the most popular databases. It is also the best supported and best documented database for web based projects. For example with PHP.

![MariaDB vs MySQL](./img/mariadb-vs-mysql.jpg)

> #### MySQL vs MariaDB
> 
> MySQL is maintained by Oracle. MySQL is free to use but not entirely open source. Some parts are closed source. This was not the vision of the original developers. Therefor they created a fork that replaces the closed source parts with open source alternatives. This fork is called MariaDB, and guarantees to stay open source.
>
> MariaDB and MySQL are therefor compatible. All MySQL command are compatible with MariaDB and vica versa.

## What is a database? 

The word database is used in many ways. For our purpose we will use the following definition:

> A database is a collection of data stored in some organized fashion

You can think of a database as some kind of cabinet. It is simply a physical location to store data, regardless of what data is or how it is stored.

## DataBase Management System - DBMS

The term `database` does not refer to the database software that is used. This might create much confusion if not used correctly. The database software is called the Database Management System or DBMS.

The database is the container that is created and can be manipulated using the DBMS. MySQL in this case is a DBMS system, not the fysical database.

A database might be a file on a hard drive, but it might not. It is not even significant as you never access a database directly anyway. You always use the DBMS that accesses the database for you.

![DBMS](./img/dbms.jpg)

## Tables

When storing information in a filing cabinet, you don’t just toss it in a drawer. You create files within the cabinet. You file related data in specific files.

In the database world, the file is called a table. A table is a structured file that can store data of a specific type. A table may contain a list of customers, a product catalog or any other list of information.

![Filing cabinet](./img/filing-cabinet.jpg)

### Columns and datatypes
Tables are made up of columns. Columns contain a particular piece of information within the table. You can envision database tables as grids (like spreadsheets). Each column on the grid contains a particular piece of information.

Each column in a database has an associated **datatype**. It defines what the type the data the column can contain

Eg: Numeric, date, text, currency,…

Datatypes are very important for a database. They restrict the type of data that can be stored in the column, preventing wrong information to be stored. It can also help sorting the data correctly and efficiently. They play an important role in optimizing disk usage.

### Rows

Data in a table is stored in rows. Each record saved is stored in its own row.

Eg: A customer table might store one customer per row

The number of rows in the table is the number of records in it. Record and row are used interchangeably but row is technically the correct term.

##  SQL
SQL pronounced as:

* Letters: S-Q-L 
* Or as SEQUEL (Structured English Query Language) original name.

Stands for Structured Query Language and is a language that is designed specifically for communicating with databases. Unlike other languages (spoken languages, or programming languages such as Java or C++) SQL is made up of very few words. This is deliberate. SQL is designed to do one thing, and do it very well. SQL provides you with a simple and efficient way to read and write data from a database.

### Advantages

SQL is not proprietary. It is not used by specific database vendors. Almost every major DBMS system supports SQL. This enables you to interact with just about every database you’ll run into.

SQL is easy to learn. The statements are all made up of descriptive English words (and there aren’t many of them). Despite its apparent simplicity, SQL is actually very powerful. Cleverly using its language elements, you can perform very complex and sophisticated database operations.

### Data definition

Data definition language (DDL) statements are used for creating tables, relationships and other structures.

```sql
CREATE DATABASE bookstore;

CREATE TABLE books (
   isbn CHAR(13) NOT NULL UNIQUE,
   name VARCHAR(64) NOT NULL,
   description TEXT,
   price DECIMAL(6,2)
);
```

## Data manipulation

Data manipulation language (DML) statements are used for queries and data modification.

Create, Read, Update and Delete

### Create

```sql
INSERT INTO books (isbn, name, description, price) VALUES
  ("9781449303969", "Learning MySQL", "Good book", 33.50);
```

### Read

```sql
SELECT isbn, name, description, price FROM books;
```

```
+---------------+----------------+-------------+-------+
| isbn          | name           | description | price |
+---------------+----------------+-------------+-------+
| 9781449303969 | Learning MySQL | Good book   | 33.50 |
+---------------+----------------+-------------+-------+
```

### Update

```sql
UPDATE books SET price = 23.50 WHERE isbn = "9781449303969";
```

### Delete

```sql
DELETE FROM books WHERE isbn = "9781449303969";
```

## Installation

MySQL can be installed using the apt package manager with the following command:

```shell
sudo apt install mysql-server php-mysql -y
sudo service apache2 restart
```

### MySQL client

```
sudo mysql -u root
```

