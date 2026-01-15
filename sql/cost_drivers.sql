SELECT
    p.specialty,
    SUM(c.procedure_cost) AS total_spend,
    COUNT(c.claim_id) AS claim_volume
FROM claims c
JOIN providers p ON c.provider_id = p.provider_id
GROUP BY p.specialty
ORDER BY total_spend DESC;
