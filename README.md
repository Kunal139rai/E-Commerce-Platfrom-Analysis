# E-Commerce-Platfrom-Analysis
Finding Key insights from an E-commerce platform using SQL ,Python and PowerBI

### Problem 1: Data Modelling (related to Problem 2)

Imagine you are designing a database for an e-commerce platform. Key business requirements are as follows:

1. Multiple kinds of products related to clothing, groceries, electronics are available on the platform
2. Each product may (not necessarily) have variants such as red T-shirt, green T-shirt. Products or some of their variants may be discontinued or restored as per requirement.
3. Pricing is dynamic and may be revised from time to time as per business requirements (each variant may have a different pricing)
4. Customer details required for completing the order need to be saved. Customers may change their details such as address from time to time.
5. Make assumptions about other business requirements (as necessary) but state them clearly. For e.g. you can assume that its not a multi-seller platform, i.e. all products are sold by the platform itself.

**Design a data model**

1. An entity-relationship diagram (ERD) with all proposed entities and types of relationships between them.
2. Generated and inserted sample data in the above model. Include the process and code of generating random data.The data should have:
    1. At least 2 years of order history
    2. At least 10 products; at least 2 products with variants.
    3. At least 10 customers
  
  ### Problem 2: SQL (related to Problem 1)

With the above data, writes an SQL queries for the following:

1. Retrieve the top 5 customers who have made the highest average order amounts in the last 6 months. The average order amount should will be calculated for each customer, and the result should be sorted in descending order.
2. Retrieved the list of customer whose order value is lower this year as compared to previous year
3. Create a table showing cumulative purchase by a particular customer. Show the breakup of cumulative purchases by product category
4. Retrieve the list of top 5 selling products. Further bifurcate the sales by product variants
