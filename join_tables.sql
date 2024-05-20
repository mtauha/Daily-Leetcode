SELECT
    firstname AS firstName,
    lastname AS lastName, 
    city, 
    state 
FROM Person
LEFT JOIN 
    Address 
ON 
    Person.personID = Address.personID;