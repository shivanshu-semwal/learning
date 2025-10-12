# Structured query language

## What is SQL?

- SQL is a domain specific language used in programming and designed
  for managing data held in a RDBMS or for stream processing in a
  relational data stream management.
- useful for handling structured data

## Interoperability and standardization

> SQL implementations are incompatible between vendors and do not necessarily completely follow standards.
> In particular, date and time syntax, string concatenation, NULLs, and comparison case sensitivity vary from vendor to vendor.

SQL was adopted as a standard by the ANSI in 1986 as SQL-86 and the ISO in 1987.

<https://en.wikipedia.org/wiki/SQL#Interoperability_and_standardization>

## Theory behind SQL

- relational algebra and tuple relational calculus are used here

## Types of statements in SQL

SQL consists of many types of statements, which may be informally classed as sublanguages:

- DDL
    - data definition language
    - creating and modifying database objects such as table, and users
    - `CREATE`, `ALERT`, `DROP`, `TRUNCATE`
- DCL
    - data control language
    - control the access of the data stored in the database
    - `GRANT`, `REVOKE`
- DML
    - data manipulation language
    - adding, inserting, modifying (updating), conditional selection
    - `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `FROM`, `WHERE`
- DQL
    - data query language
    - perform queries on data within schema objects\
    - `SELECT`
- TCL (*not everyone agrees this to be sublanguage)
    - transaction control language

## Further Links

- <https://en.wikibooks.org/wiki/SQL_Dialects_Reference>