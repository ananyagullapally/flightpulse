SELECT
    airport,
    COUNT(*) AS total_routes
FROM (
    SELECT source_airport AS airport FROM {{ ref('stg_routes') }}
    UNION ALL
    SELECT destination_airport AS airport FROM {{ ref('stg_routes') }}
)
GROUP BY airport
ORDER BY total_routes DESC
