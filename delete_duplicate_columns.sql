DELETE t1
  FROM Person AS t1
    INNER JOIN Person AS t2
WHERE t1.id > t2.id
  AND t1.email = t2.email;