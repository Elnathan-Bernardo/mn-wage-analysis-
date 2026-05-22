-- Q4: MN tech/MIS wages vs national benchmarks
SELECT
    OCC_TITLE,
    TOT_EMP AS mn_employment,
    TRY_CAST(A_MEDIAN AS FLOAT) AS mn_annual_median,
    TRY_CAST(H_MEAN AS FLOAT) AS mn_hourly_mean,
    CASE
        WHEN TRY_CAST(A_MEDIAN AS FLOAT) > 105600 THEN 'Above National Avg'
        WHEN TRY_CAST(A_MEDIAN AS FLOAT) < 105600 THEN 'Below National Avg'
        ELSE 'At Par'
    END AS vs_national
FROM oews_mn
WHERE OCC_CODE LIKE '15-%'
    AND O_GROUP = 'detailed'
    AND TRY_CAST(A_MEDIAN AS FLOAT) IS NOT NULL
ORDER BY TRY_CAST(A_MEDIAN AS FLOAT) DESC;