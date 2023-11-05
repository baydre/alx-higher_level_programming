# 0x0D-SQL_introduction
## Learning Objectives
At the end of this, the below concepts were explained and understood.
- Database.
- Relational Database.
- SQL and MySQL.
- Creation of Database and Queries in MySQL.
- Use of `CREATE or ALTER`, `SELECT`, and `INSERT, UPDATE or DELETE` in a table.
- Subqueries and use of MySQL functions.

A **database** is an organized collection of data, typically stored and accessed electronically from a computer system. Databases are used to store and manage various forms of data, such as customer information, product catalogs, employee records, and much more. They are a fundamental part of modern computing and are essential for various applications, including websites, mobile apps, business software, and scientific research.

A **Relational Database Management System (RDBMS)** is a type of database management system that organizes data into structured tables with rows and columns. These tables are related to each other based on predefined relationships.

**SQL (Structured Query Language)** is a specialized programming language used to manage and manipulate relational databases. SQL allows users to perform tasks such as querying data, updating records, inserting new data, and deleting data from a database.

Some key concepts related to databases and SQL:

### 1. **Database Structure:**
   - **Tables:** Databases consist of one or more tables, which are structured collections of data.
   - **Rows:** Each row in a table represents a specific record or data entity.
   - **Columns:** Columns define the attributes or fields of a table and hold specific types of data, like text, numbers, dates, etc.
   - **Keys:** Tables often have primary keys (unique identifiers) and foreign keys (to establish relationships with other tables).

### 2. **SQL Operations:**
   - **SELECT:** Used to query data from one or more tables.
   - **INSERT:** Adds new records into a table.
   - **UPDATE:** Modifies existing records in a table.
   - **DELETE:** Removes records from a table.
   - **JOIN:** Combines data from two or more tables based on a related column between them.
   - **WHERE:** Filters data based on specific conditions.
   - **GROUP BY:** Groups rows that have the same values into aggregated data.
   - **ORDER BY:** Sorts the result set based on one or more columns.

### 3. **Database Management Systems (DBMS):**
   - **Examples:** MySQL, PostgreSQL, Oracle, SQL Server, SQLite.
   - **Functions:** These systems manage the creation, retrieval, updating, and deletion of data in a database.

### 4. **Normalization:**
   - **Process:** Organizing a database structure to reduce redundancy and improve data integrity.
   - **Benefits:** Minimizes data duplication, enhances query performance, and simplifies maintenance.

### 5. **Transactions:**
   - **Definition:** A sequence of one or more SQL operations treated as a single unit of work.
   - **ACID Properties:** Transactions ensure Atomicity, Consistency, Isolation, and Durability of database operations.

SQL is a powerful tool for managing and querying databases, and it is widely used by developers, data analysts, and database administrators to interact with relational databases effectively.