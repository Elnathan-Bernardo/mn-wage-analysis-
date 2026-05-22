-- Q2: Wage gap analysis by occupation group
SELECT
    OCC_TITLE,
    TOT_EMP,
    TRY_CAST(A_PCT10 AS FLOAT)  AS bottom_10pct,
    TRY_CAST(A_MEDIAN AS FLOAT) AS median_wage,
    TRY_CAST(A_PCT90 AS FLOAT)  AS top_10pct,
    TRY_CAST(A_PCT90 AS FLOAT) - TRY_CAST(A_PCT10 AS FLOAT) AS wage_spread
FROM oews_mn
WHERE O_GROUP = 'major'
    AND TRY_CAST(A_PCT10 AS FLOAT) IS NOT NULL
    AND TRY_CAST(A_PCT90 AS FLOAT) IS NOT NULL
ORDER BY wage_spread DESC;