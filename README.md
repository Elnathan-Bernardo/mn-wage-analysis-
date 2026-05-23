# Minnesota Wage & Employment Analysis (2024)
 * An end-to-end data analytics project using real Minnesota government data to answer four business questions about the labor market.

## Tools Used
 * Python — for data cleaning
 * SQL Server — database and analysis queries
 * Power BI — interactive dashboards (5 pages)

## Business Questions
1. Which MN occupations employ the most workers and pay the highest wages?
2. Where are the biggest wage gaps across MN occupation groups?
3. Which jobs are most in-demand but hardest to fill?
4. How do MN tech wages compare to national benchmarks?
5. How do wages vary across MN metro regions?

## Data Sources
 * BLS OEWS May 2024 — occupation wages by state
 * MN DEED Job Vacancy Survey 2024 — open positions by occupation
 * BLS QCEW 2024 — employment and wages by metro area

## Key Findings
- Computer & Math leads MN with 97K workers at $102K median wage
- Legal occupations have the widest wage inequality (4.4x gap)
- Healthcare has 24,000+ unfilled skilled positions statewide
- Minneapolis-St. Paul leads MN regions at $78.7K average annual pay

## Dashboard Screenshots

## Page 1 — Employment & Wage Overview
 * [Page 1](page1.png)

## Page 2 — Wage Gap Analysis
 * [Page 2](page2.png)

## Page 3 — Job Vacancy Gap
 * [Page 3](page3.png)

## Page 5 — Regional Map
 * [Page 5](page5.png)

## How to Run
1. Download raw data files from BLS and MN DEED
  - [BLS OEWS May 2024 State Data](https://www.bls.gov/oes/tables.htm) → Under May 2024 → click State (XLSX)
  - [MN DEED Job Vacancy Survey](https://mn.gov/deed/data/data-tools/job-vacancy/) → Set Statewide + All Industries + Export
  - [BLS QCEW 2024 Annual by Area](https://www.bls.gov/cew/downloadable-data-files.htm) → Annual Averages → 2024 → Area
2. Create a folder called `Raw Data` in the project directory and place downloaded files there
3. Run `cleaned dataset.py` to generate clean CSVs
4. Open SQL Server Management Studio → create a database called `mn_wage_analysis`
5. Update SERVER_NAME in `cleaned dataset.py` to your own SQL Server instance and re-run to load data into the database
6. Run the SQL query files (`q1_industry_wages.sql`, `q2_wage_gaps.sql`, `q3_vacancy_gap.sql`, `q4_tech_vs_national.sql`) in SQL Server Management Studio
7. Open `MN_Wage_Analysis.pbix` in Power BI Desktop and update the data connection to your own SQL Server instance
