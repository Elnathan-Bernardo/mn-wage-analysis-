-- Q1: Top 10 MN occupation groups by total employment
SELECT TOP 10
    OCC_TITLE,
    TOT_EMP,
    A_MEDIAN,
    H_MEAN
FROM oews_mn
WHERE O_GROUP = 'major'
ORDER BY TOT_EMP DESC;