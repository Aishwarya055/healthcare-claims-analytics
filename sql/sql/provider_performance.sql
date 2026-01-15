SELECT
    p.provider_name,
    COUNT(c.claim_id) AS claims_processed,
    AVG(c.procedure_cost) AS avg_claim_cost
FROM claims c
JOIN providers p ON c.provider_id = p.provider_id
GROUP BY p.provider_name;
