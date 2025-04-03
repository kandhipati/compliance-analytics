# anomaly_detection.py
import pandas as pd

# Load the cleaned compliance data
df = pd.read_csv('compliance_data_clean.csv')

# Define a simple rule: flag scores below a dynamic threshold (e.g., mean - 1 standard deviation)
threshold = df['ComplianceScore'].mean() - df['ComplianceScore'].std()
df['Anomaly'] = df['ComplianceScore'] < threshold

# Output anomalies
anomalies = df[df['Anomaly'] == True]
anomalies.to_csv('anomalies_detected.csv', index=False)

print(f"Anomaly detection completed. {len(anomalies)} anomalies detected and saved to 'anomalies_detected.csv'.")
