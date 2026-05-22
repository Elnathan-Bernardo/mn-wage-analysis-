-- Q3: Most in-demand occupations with highest vacancies
SELECT TOP 20
    j.soctitle,
    j.vacancies,
    j.vacanrate,
    j.medianwage * 2080 AS posted_annual_wage,
    o.A_MEDIAN AS oews_annual_median,
    o.TOT_EMP AS current_employment
FROM jvs_mn j
LEFT JOIN oews_mn o ON j.occ_code = o.OCC_CODE
WHERE j.vacancies > 0
    AND j.soclevel >= 3
ORDER BY j.vacancies DESC;