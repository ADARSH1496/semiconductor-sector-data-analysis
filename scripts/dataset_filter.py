import pandas as pd

RAW_INPUT_PATH = r"C:\MASTERS\Data Analysis\ASSIGNMENTS\Final Project\repo\semiconductor-sector-data-analysis\data\raw\semi_conductor_se.csv"
df = pd.read_csv(RAW_INPUT_PATH)

print("Raw dataset shape (rows, columns):", df.shape)
print("Raw dataset total rows:", len(df))


# 2. Drop unwanted index column (if present)
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])


# 3. Parse date column
df["date"] = pd.to_datetime(df["date"])


# 4. Filter time range (2015–2025)
START_DATE = "2015-01-01"
END_DATE   = "2025-08-04"

df = df[(df["date"] >= START_DATE) & (df["date"] <= END_DATE)]

print("After date filter:", df.shape)
print("Rows:", len(df))

# 5. Select tickers

selected_tickers = [
    "NVDA", "AMD", "INTC", "AVGO", "TSM",
    "NXPI", "ASML", "AMAT", "LRCX", "QCOM",
    "MU", "TXN", "ADI", "ON", "MRVL",
    "KLAC", "MCHP", "STM", "IFX.DE"
]

df = df[df["stock_name"].isin(selected_tickers)]

print("After ticker filter:", df.shape)
print("Rows:", len(df))



# 6. Sort data (important for time series)
df = df.sort_values(["stock_name", "date"]).reset_index(drop=True)


# 7. Basic sanity checks
print("\nFinal dataset checks:")
print("Number of unique tickers:", df["stock_name"].nunique())
print("Date range:",
      df["date"].min().date(), "to", df["date"].max().date())
print("Final total rows:", len(df))


# 8. Save filtered dataset
PROCESSED_OUTPUT_PATH = r"C:\MASTERS\Data Analysis\ASSIGNMENTS\Final Project\repo\semiconductor-sector-data-analysis\data\processed\semiconductor_stocks_data_2015_2025.csv"
df.to_csv(PROCESSED_OUTPUT_PATH, index=False)

print(f"\nFiltered dataset saved as: {PROCESSED_OUTPUT_PATH}")
