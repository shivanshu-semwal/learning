# SQL Syntax

The SQL language is subdivided into several language elements, including:

- Clauses
    - which are constituent components of statements and queries. _In some cases, these are optional._
- Expressions
    - which can produce either scalar values, or tables consisting of columns and rows of data
- Predicates
    - which specify conditions that can be evaluated to SQL three-valued logic (3VL) (true/false/unknown) 
    or Boolean truth values and are used to limit
    the effects of statements and queries, or to change program flow.
- Queries
    - which retrieve the data based on specific criteria. This is an important element of SQL.
- Statements
    - which may have a persistent effect on schemata and data, or may control transactions, program flow, connections, sessions, or diagnostics.
SQL statements also include the semicolon (";") statement terminator.
Though not required on every platform, it is defined as a standard part of the SQL grammar.

Insignificant whitespace is generally ignored in SQL statements and queries, making it easier to format SQL code for readability.

## SQL - Clauses, Keywords, functions, data types

- [difference between clause and keyword](https://stackoverflow.com/questions/31151264/what-is-the-difference-between-a-keyword-and-a-clause-in-sql)

- `CLAUSE` - we join different clauses to make a sql query
    - `SELECT name FROM table`, this is a clause
    - `SELECT` `FROM` are keywords
- `KEYWORDS` - words which have special meaning in SQL
    - `WHERE`, `SELECT`, `FROM`, `DISTINCT`
    - Some keywords can only be used with some clauses, like `DISTINCT` can only be used with `SELECT`
- `FUNCTIONS()` are which take a parameter - inside (), there can be no parameter too
    - `COUNT()` is a function

## Syntax Elements

- **statements** - which may have a persistent effect on schemata and data, or may control transactions, program flow, connections, sessions, or diagnostics.
- **queries** - which retrieve the data based on specific criteria.
- **clauses** - which are constituent components of statements and queries.
- **predicates** - which specify conditions that can be evaluated to SQL three-valued logic or Boolean truth values and are used to limit the effects of statements and queries, or to change program flow.
- **expressions** - which can produce either scalar values, or tables consisting of columns and rows of data
- **keywords** - words that are defined in sql language, can be reserver or non reserved
- **identifiers** - name of database objects, like tables, columns and schemas.
- **insignificant** whitespace - is generally ignored in SQL statements and queries, making it easier to format SQL code for readability.
- **comments** - to add comments to code

## Further Link

- <https://en.wikipedia.org/wiki/SQL_syntax>
- <https://standards.iso.org/iso-iec/9075/-2/ed-6/en/ISO_IEC_9075-2(E)_Foundation.bnf.xml>
- <http://forcedotcom.github.io/phoenix/index.html>
- <https://archive.org/details/federalinformati127nati/page/16/mode/2up>
