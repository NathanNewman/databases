### Conceptual Exercise

Answer the following questions below:

1. What is PostgreSQL?
It is a relational database management system.
2. What is the difference between SQL and PostgreSQL?
SQL stands for structured query language. It's a human readable language used for communicating with data bases PostgreSQL is a type of SQL.

3. In `psql`, how do you connect to a database?
You type psql and then add a space and type the name of the database.

4. What is the difference between `HAVING` and `WHERE`?
Having is used when the condition requires and aggregate function.

5. What is the difference between an `INNER` and `OUTER` join?
Inner joins connect everything in common. Outer joins connect everything not in common.

6. What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
The left outer lists everything in the left column and then joins some information from the right, where as
the right joins lists everything from the right and then adds some information from the left.

7. What is an ORM? What do they do?
It stands for Object Relational Mapping and is a library for a programming language that allows database communication. SQL-Alchemy is an example of an ORM for Python.

8. What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
AJAX is client side and used in JavasScript, where as the python requests library is server side.

9. What is CSRF? What is the purpose of the CSRF token?
Cross site request forgery is an attack that causes users to make requests on a web-application that they do not intend to. A CSRF token is a type of authentication key used to prevent such attacks.

10. What is the purpose of `form.hidden_tag()`?
It is used in WTForms to hide certain inputs that the user is not suppose to see. The most common use is to hide the CSRF token.
