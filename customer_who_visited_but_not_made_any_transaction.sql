SELECT 
    customer_id, 
    COUNT(customer_id) AS count_no_trans 

FROM Visits
WHERE 
    visit_id NOT IN (
        SELECT visit_id FROM Visits v
        NATURAL JOIN Transactions
    )

GROUP BY 
    customer_id;
