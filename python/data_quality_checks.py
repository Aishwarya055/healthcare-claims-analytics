import pandas as pd

claims = pd.read_csv("../data/sample_claims.csv")

# Check for missing values
missing_summary = claims.isnull().sum()

# Validate cost values
invalid_costs = claims[claims["procedure_cost"] <= 0]

print("Missing Values Summary:")
print(missing_summary)

print("\nInvalid Cost Records:")
print(invalid_costs)
