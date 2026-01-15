import pandas as pd

claims = pd.read_csv("../data/sample_claims.csv")

summary = claims.groupby("plan_type")["procedure_cost"].sum().reset_index()

summary.to_excel("monthly_claims_summary.xlsx", index=False)

print("Automated report generated successfully.")
