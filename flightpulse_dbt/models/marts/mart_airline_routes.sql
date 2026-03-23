SELECT
    airline,
    COUNT(*) AS total_routes
FROM {{ ref('stg_routes') }}
GROUP BY airline
ORDER BY total_routes DESC
