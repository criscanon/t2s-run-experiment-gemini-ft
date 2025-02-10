prompts = {

# FT1: NLQ
"ft_prompt_1":
"""{nlq}""",

# FT2: Dialect + Completed Schema + NLQ
"ft_prompt_2":
"""You are a {dialect} expert, your task is to create an optimal, syntactically, and semantically correct {dialect} query based on the provided database schema to answer the input question.

Consider the following database schema:
{schema}

Input question:
{nlq}

Provide only the SQL query to execute without any comments, and ensure it ends with a semicolon.""",

# FT3: Dialect + Completed Schema + Five Examples NLQ-SQL + NLQ (Nativo).
"ft_prompt_3":
"""You are a {dialect} expert, your task is to create an optimal, syntactically, and semantically correct {dialect} query based on the provided database schema and three example pairs of NLQ (input question) - SQL, to answer the input question.

### Database Schema

{schema}

### Example NLQ-SQL Pairs

NLQ: Tell me the name of the movies of the actor CHRISTIAN AKROYD ordered by category.
SQL:
SELECT f.film_id, f.title, a.first_name, a.last_name, c.name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE a.first_name LIKE 'CHRISTIAN' AND a.last_name LIKE 'AKROYD'
ORDER BY c.name;

NLQ: List the total sales that Mike had in the month of June 2005. Round the value to 4 decimal places.
SQL:
SELECT s.staff_id, s.first_name, s.last_name, ROUND(SUM(p.amount), 4) AS total_sales
FROM payment p
JOIN staff s ON p.staff_id = s.staff_id
WHERE s.first_name LIKE 'Mike'
AND p.payment_date BETWEEN '2005-06-01 00:00:00' AND '2005-06-30 23:59:59'
GROUP BY s.staff_id, s.first_name, s.last_name;

NLQ: Which customers have rented more than 35 movies at store 2?
SQL:
SELECT c.customer_id, c.first_name, c.last_name, COUNT(*) AS rental_count, c.store_id
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
WHERE c.store_id = 2
GROUP BY c.customer_id
HAVING COUNT(*) > 35;

### Input Question

{nlq}

Provide only the SQL query to execute without any comments, and ensure it ends with a semicolon."""
}