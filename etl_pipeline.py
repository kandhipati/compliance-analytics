# etl_pipeline.py
import pandas as pd

# Load sample compliance data
df = pd.read_csv('compliance_data.csv')

# Data cleaning: Remove rows with missing scores
df_clean = df.dropna(subset=['ComplianceScore'])

# Transformation: Flag non-compliant employees
df_clean['IsNonCompliant'] = df_clean['ComplianceScore'] < 80

# Save the cleaned and transformed data
df_clean.to_csv('compliance_data_clean.csv', index=False)

print("ETL process completed. Clean data saved to 'compliance_data_clean.csv'.")
