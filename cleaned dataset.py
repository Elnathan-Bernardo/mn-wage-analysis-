# Minnesota Wage Analysis - Data Cleaning
# Sources: BLS OEWS May 2024, MN DEED JVS 2024, BLS QCEW 2024
# Run this first before loading into SQL or Power BI

import pandas as pd
import numpy as np
import glob
from sqlalchemy import create_engine

# connect to sql server - update server name to yours
SERVER_NAME = "YOUR_SERVER_NAME\\SQLEXPRESS"
engine = create_engine(
    f"mssql+pyodbc://{SERVER_NAME}/mn_wage_analysis"
    "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

# load oews and filter to minnesota only
oews = pd.read_excel("Raw Data/state_M2024_dl.xlsx", sheet_name="state_M2024_dl")
oews_mn = oews[oews["PRIM_STATE"] == "MN"].copy()
oews_mn = oews_mn[oews_mn["O_GROUP"].isin(["detailed", "major"])]

# bls uses # for suppressed values so replace with NaN
wage_cols = ["H_MEAN", "A_MEAN", "H_MEDIAN", "A_MEDIAN"]
for col in wage_cols:
    oews_mn[col] = pd.to_numeric(oews_mn[col].replace("#", np.nan), errors="coerce")

oews_mn.to_csv("Raw Data/oews_mn_clean.csv", index=False)
oews_mn.to_sql("oews_mn", engine, if_exists="replace", index=False)
print("oews done -", len(oews_mn), "rows")

# load job vacancy survey
jvs = pd.read_csv("Raw Data/JVSOccResults.csv")
jvs["areaname"] = jvs["areaname"].str.strip()
jvs = jvs.drop(columns=[c for c in jvs.columns if "Unnamed" in c])

# normalize soc codes to match oews format (110000 -> 11-0000)
def normalize_soc(code):
    code = str(code).zfill(6)
    return f"{code[:2]}-{code[2:]}"

jvs["occ_code"] = jvs["occcode"].apply(normalize_soc)
jvs.to_csv("Raw Data/jvs_mn_clean.csv", index=False)
jvs.to_sql("jvs_mn", engine, if_exists="replace", index=False)
print("jvs done -", len(jvs), "rows")

# load all mn qcew files and combine
qcew_path = r"2024_annual_by_area\2024.annual.by_area"
mn_files = glob.glob(qcew_path + r"\*MN*.csv")
qcew_raw = pd.concat([pd.read_csv(f, dtype=str) for f in mn_files], ignore_index=True)

# keep only metro and county level totals
qcew_clean = qcew_raw[qcew_raw['agglvl_title'].isin([
    'County, Total Covered',
    'MSA, Total Covered',
    'MicroSA, Total Covered'
])].copy()

qcew_clean = qcew_clean[[
    'area_title', 'agglvl_title', 'industry_title',
    'annual_avg_emplvl', 'total_annual_wages',
    'annual_avg_wkly_wage', 'avg_annual_pay',
    'oty_annual_avg_emplvl_pct_chg', 'oty_avg_annual_pay_pct_chg'
]].copy()

qcew_clean.columns = [
    'area', 'area_type', 'industry',
    'avg_employment', 'total_annual_wages',
    'avg_weekly_wage', 'avg_annual_pay',
    'employment_pct_change', 'wage_pct_change'
]

for col in ['avg_employment', 'total_annual_wages', 'avg_weekly_wage',
            'avg_annual_pay', 'employment_pct_change', 'wage_pct_change']:
    qcew_clean[col] = pd.to_numeric(qcew_clean[col], errors='coerce')

# clean up area names
qcew_clean['area'] = (qcew_clean['area']
    .str.replace(', MN', '')
    .str.replace(' MSA', '')
    .str.replace(' MicroSA', '')
    .str.strip()
)

qcew_clean.to_csv("Raw Data/qcew_mn_clean.csv", index=False)
qcew_clean.to_sql("qcew_mn", engine, if_exists="replace", index=False)
print("qcew done -", len(qcew_clean), "rows")