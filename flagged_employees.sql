-- Identify non-compliant employees
SELECT 
    EmployeeID, 
    ComplianceScore 
FROM compliance_data
WHERE ComplianceScore < 80;