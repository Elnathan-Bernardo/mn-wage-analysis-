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

## How to Run
1. Download raw data files from BLS and MN DEED
2. Place in `Raw Data/` folder
3. Run `cleaned dataset.py` to generate clean CSVs
4. Load the cleaned CSVs into SQL Server and run queries in `/sql` folder
5. Open `MN_Wage_Analysis.pbix` in Power BI Desktop
