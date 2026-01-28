import pandas as pd

# df = pd.read_csv("/Users/ishika.3.saxena/serverless/churn_prediction/data/Teleco-Customer-churn.csv")
df = pd.read_csv("../data/Teleco-Customer-churn.csv")


# preview first 5 rows
print(df.head())

print("dataset info")
print(df.info(),"\n")

# check for missing values
print("missing values in each coloumn")
print(df.isnull().sum(),"\n")

print("descriptive statistics")
print(df.describe())

# target varibale distribution
# Step 6: Check target variable distribution
if 'Churn' in df.columns:
    print("\n===== Target Variable Distribution (Churn) =====")
    print(df['Churn'].value_counts())
else:
    print("\nChurn column not found!")

categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
print("\n Unique values in categorical coloumn")
for col in categorical_cols:
    print(f"{col}:{df[col].unique()}")


numeric_cols=df.select_dtypes(include=['int64','float64']).columns
print("\n===== Skewnessof numeric fetaures =====")
print(df[numeric_cols].skew())