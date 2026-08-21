import pandas as pd
import numpy as np
import os


# 1. LOAD THE DATASET

df = pd.read_csv("Sample_dataset.csv")

print("=" * 60)
print("ORIGINAL DATASET")
print("=" * 60)
print(df)

print("\nDataset shape:", df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])



# 2. DATA QUALITY ANALYSIS

print("\n" + "=" * 60)
print("DATA QUALITY ANALYSIS")
print("=" * 60)

# Missing values
missing_values = df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100

missing_report = pd.DataFrame({
    "Missing Values": missing_values,
    "Missing Percentage (%)": missing_percentage
})

print("\nMissing Value Report:")
print(missing_report)

# Duplicate rows
duplicate_count = df.duplicated().sum()

print("\nNumber of exact duplicate rows:", duplicate_count)

# Duplicate IDs
duplicate_ids = df["ID"].duplicated().sum()

print("Number of duplicate IDs:", duplicate_ids)



# 3. DATA CLEANING

clean_df = df.copy()

# Convert Age to numeric.
# Invalid values such as "thirty-eight" become NaN.
clean_df["Age"] = pd.to_numeric(
    clean_df["Age"],
    errors="coerce"
)

# Remove commas from Net worth and convert to numeric.
clean_df["Net worth"] = (
    clean_df["Net worth"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

clean_df["Net worth"] = pd.to_numeric(
    clean_df["Net worth"],
    errors="coerce"
)

# Convert Salary to numeric.
# Text such as "sixty five thousand" becomes NaN.
clean_df["Salary"] = pd.to_numeric(
    clean_df["Salary"],
    errors="coerce"
)

# Standardise country names.
# AU and AUS represent Australia.
clean_df["Country"] = clean_df["Country"].replace({
    "AU": "AUS"
})

# Convert Join Date to datetime.
# Invalid dates become NaT.
clean_df["Join Date"] = pd.to_datetime(
    clean_df["Join Date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

print("\nCleaned Dataset:")
print(clean_df)



# 4. DESCRIPTIVE STATISTICS

print("\n" + "=" * 60)
print("DESCRIPTIVE ANALYTICS")
print("=" * 60)

numeric_columns = ["Age", "Net worth", "Salary"]

for column in numeric_columns:

    print(f"\n--- {column} ---")

    print("Count :", clean_df[column].count())
    print("Mean  :", clean_df[column].mean())
    print("Median:", clean_df[column].median())
    print("Min   :", clean_df[column].min())
    print("Max   :", clean_df[column].max())
    print("Range :", clean_df[column].max() -
                    clean_df[column].min())
    print("Std Dev:", clean_df[column].std())



# 5. COUNTRY ANALYSIS

print("\n" + "=" * 60)
print("COUNTRY ANALYSIS")
print("=" * 60)

country_counts = clean_df["Country"].value_counts()

print("\nNumber of records by country:")
print(country_counts)

country_percentage = (
    clean_df["Country"].value_counts(normalize=True) * 100
)

print("\nPercentage by country:")
print(country_percentage)


# 6. SALARY ANALYSIS BY COUNTRY

print("\n" + "=" * 60)
print("SALARY ANALYSIS BY COUNTRY")
print("=" * 60)

salary_by_country = clean_df.groupby("Country")["Salary"].agg([
    "count",
    "mean",
    "median",
    "min",
    "max"
])

print(salary_by_country)


# 7. NET WORTH ANALYSIS BY COUNTRY

print("\n" + "=" * 60)
print("NET WORTH ANALYSIS BY COUNTRY")
print("=" * 60)

networth_by_country = clean_df.groupby("Country")["Net worth"].agg([
    "count",
    "mean",
    "median",
    "min",
    "max"
])

print(networth_by_country)



# 8. CORRELATION ANALYSIS

print("\n" + "=" * 60)
print("CORRELATION ANALYSIS")
print("=" * 60)

correlation = clean_df[
    ["Age", "Net worth", "Salary"]
].corr()

print(correlation)


# 9. KEY ANALYTICAL RESULTS

print("\n" + "=" * 60)
print("KEY ANALYTICAL RESULTS")
print("=" * 60)

print("Average Age:",
      round(clean_df["Age"].mean(), 2))

print("Median Age:",
      round(clean_df["Age"].median(), 2))

print("Average Salary:",
      round(clean_df["Salary"].mean(), 2))

print("Median Salary:",
      round(clean_df["Salary"].median(), 2))

print("Highest Salary:",
      clean_df["Salary"].max())

print("Lowest Salary:",
      clean_df["Salary"].min())

print("Average Net Worth:",
      round(clean_df["Net worth"].mean(), 2))

print("Highest Net Worth:",
      clean_df["Net worth"].max())

print("Lowest Net Worth:",
      clean_df["Net worth"].min())



# 10. SAVE ANALYSIS RESULTS TO CSV

results = {
    "Metric": [
        "Number of Rows",
        "Number of Columns",
        "Duplicate Rows",
        "Duplicate IDs",
        "Average Age",
        "Median Age",
        "Minimum Age",
        "Maximum Age",
        "Average Salary",
        "Median Salary",
        "Minimum Salary",
        "Maximum Salary",
        "Average Net Worth",
        "Median Net Worth",
        "Minimum Net Worth",
        "Maximum Net Worth"
    ],

    "Value": [
        len(clean_df),
        len(clean_df.columns),
        clean_df.duplicated().sum(),
        clean_df["ID"].duplicated().sum(),
        clean_df["Age"].mean(),
        clean_df["Age"].median(),
        clean_df["Age"].min(),
        clean_df["Age"].max(),
        clean_df["Salary"].mean(),
        clean_df["Salary"].median(),
        clean_df["Salary"].min(),
        clean_df["Salary"].max(),
        clean_df["Net worth"].mean(),
        clean_df["Net worth"].median(),
        clean_df["Net worth"].min(),
        clean_df["Net worth"].max()
    ]
}

results_df = pd.DataFrame(results)

output_file = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "analysis_results.csv"
)

results_df.to_csv(output_file, index=False)

print(f"Analysis results saved to: {output_file}")