import pandas as pd

claims = pd.read_csv("../data/sample_claims.csv")

total_claims = claims["claim_id"].nunique()
total_cost = claims["procedure_cost"].sum()

print(f"Total Claims: {total_claims}")
print(f"Total Cost: {total_cost}")
