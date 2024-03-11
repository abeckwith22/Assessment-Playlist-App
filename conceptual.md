### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

PostgreSQL is a ORM relational database management system and is know for it's close relationship with the SQL standard.

- What is the difference between SQL and PostgreSQL?

The difference between SQL and PostgreSQL is that SQL is more of a guideline to how an ORM library should act. PostgreSQL while following closely to the standards that are written out by SQL is not the same as SQL. 

- In `psql`, how do you connect to a database?

In `psql` you would connect to a database using `\c example_db` command.

- What is the difference between `HAVING` and `WHERE`?

`HAVING` is used to check the conditions of your query after aggregation takes place whereas `WHERE` is what happens before aggregation.

- What is the difference between an `INNER` and `OUTER` join?

The difference between an `INNER` and `OUTER` is `INNER` join which is the default joining method will find data that matches and discard any other information in the query in terms of a venn diagram it will display queries which match both tables and won't display any null values if there are any. `OUTER` join will find information from both tables resulting in data that can contail null values as long as it can relate to another table.

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
`LEFT OUTER` will find null values on the left side of a table, whereas `RIGHT OUTER` will find null values on the right side of table.

- What is an ORM? What do they do?

ORM or Object-Relational Mapping is a technique that allows the user to query and manipulate data from a database.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?

We won't get cross-site request errors by using server side with `requests` unlike if we we're to use client-side requests using HTTP requests with AJAX.

- What is CSRF? What is the purpose of the CSRF token?

CSRF or Cross Site Request Forgery is a method of submitting a post request from an alternative source (website, curl request, etc.) that can possibly contain more information than the actual form allows. The CSRF token is used in most website forms to verify if the form came from the same website or not, thereby stopping people putting in alternative information.

- What is the purpose of `form.hidden_tag()`?

The purpose of the `form.hidden_tag()` is to ensure that the CSRF token placed into the HTML without being shown to the user, so that the form can be verified by the token.