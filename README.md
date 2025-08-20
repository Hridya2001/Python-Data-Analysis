# Exploratory Data Analysis (EDA) using Python


## Overview
This project demonstrates skills applied in a **technical assessment for a data analytics role**.  
It focuses on analyzing and tagging a dataset of customer complaints and repair information to derive actionable insights.

Key objectives:
- Clean and preprocess raw data.
- Tag fields such as `Root Cause`, `Symptom Condition`, `Symptom Component`, `Fix Condition`, and `Fix Component`.
- Identify critical columns and patterns for stakeholders.
- Generate visualizations to communicate insights effectively.

---

## Dataset
The dataset contains detailed information on customer complaints and repairs, including:

- **Vehicle & Transaction Info:** `VIN`, `TRANSACTION_ID`, `REPAIR_DATE`, `VEH_TEST_GRP`, `COUNTRY_SALE_ISO`, `ORD_SELLING_SRC_CD`  
- **Customer Complaints:** `CUSTOMER_VERBATIM`, `CORRECTION_VERBATIM`, `COMPLAINT_CD_CSI`, `COMPLAINT_CD`  
- **Parts & Labor:** `CAUSAL_PART_NM`, `GLOBAL_LABOR_CODE_DESCRIPTION`, `TRANSACTION_CATEGORY`, `REPORTING_COST`, `TOTALCOST`, `LBRCOST`  
- **Vehicle Specs:** `PLATFORM`, `BODY_STYLE`, `ENGINE`, `TRANSMISSION`, `ENGINE_DESC`, `TRANSMISSION_DESC`, `ENGINE_SOURCE_PLANT`, `TRANSMISSION_SOURCE_PLANT`  
- **Dealership Info:** `LAST_KNOWN_DLR_NAME`, `LAST_KNOWN_DLR_CITY`, `REPAIRING_DEALER_CODE`, `DEALER_NAME`, `REPAIR_DLR_CITY`, `STATE`, `DEALER_REGION`, `REPAIR_DLR_POSTAL_CD`  
- **Repair Metadata:** `REPAIR_AGE`, `KM`, `MEDIA_FLAG`, `VIN_MODL_DESGTR`, `LINE_SERIES`, `LAST_KNOWN_DELVRY_TYPE_CD`, `NON_CAUSAL_PART_QTY`, `SALES_REGION_CODE`  

> **Note:** Sensitive information has been anonymized for privacy.

---

## Approach
1. **Data Cleaning**
   - Removed duplicates and null values.
   - Standardized inconsistent entries for parts, labor codes, and repair notes.

2. **Data Tagging**
   - Applied structured logic to tag root causes, symptoms, and fixes.
   - Ensured consistency across multiple components and conditions.

3. **Analysis & Visualization**
   - Selected top 5 critical columns for stakeholder insights.
   - Created visualizations (bar plots, distribution charts) to highlight key patterns.
   - Derived actionable insights to support data-driven decision making.

---

## Key Insights
- Recurring complaints help prioritize preventive actions.
- Symptom and fix patterns indicate areas for process improvement.
- Data-driven analysis can guide repair teams to reduce repeat issues.
- Certain parts and modules frequently cause customer-reported problems.

---

## Tools & Technologies
- Python 3.x
- Pandas, NumPy
- Matplotlib, Seaborn
- Jupyter Notebook

---


## Conclusion
This repository serves as a **hands-on example for aspiring Python data analysts** to understand how to:
- Load and clean real-world datasets.
- Perform exploratory data analysis (EDA) to extract meaningful insights.
- Identify key features that matter to stakeholders.
- Create effective visualizations to communicate findings.  

By studying this repo, learners can gain practical experience and ideas for structuring their own data analysis projects in Python.
Happy learning....
