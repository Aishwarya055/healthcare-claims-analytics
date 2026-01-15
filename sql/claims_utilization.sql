SELECT
    c.plan_type,
    c.claim_type,
    COUNT(c.claim_id) AS total_claims,
    SUM(c.procedure_cost) AS total_cost
FROM claims c
GROUP BY c.plan_type, c.claim_type
ORDER BY total_cost DESC;
