# read the train csv and get infor about quantities.

import pandas as pd

df = pd.read_csv(
    "../data/raw/train.csv",
    parse_dates=["date"]
)# datetime64[us] , remeber for time series datafram load it as "parse_date" type
print("\n========== DATASET INFO ==========")
print(df["date"].dtype)
print("Shape:", df.shape)# 3000888, 6
print("\nColumns:") # print columns name
print(df.columns.tolist()) # It prints the names of all columns.
print("\nFirst 5 rows:")
print(df.head()) # this function has default n=5, this head give first five rows of the DataFrame.

# df.tail(), returns the last 5 rows.
print("\nDate range:")
print(df["date"].min(), "->", df["date"].max()) # how it is finding date , it consider whole sequence?

print("\nStores:", df["store_nbr"].nunique()) # how many unique store 
print("Product families:", df["family"].nunique()) # no of unique family 
# while unique -> actual unique values



# ============================================================
# 2. CHECK DATA TYPES
# ============================================================

print("\n========== DATA TYPES ==========")

print(df.dtypes)


# ============================================================
# 3. CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum()) # find missing value row and sum it 


# ============================================================
# 4. CHECK DUPLICATES
# ============================================================

print("\n========== DUPLICATES ==========")

print("Duplicate rows:", df.duplicated().sum()) # look for duplicate rows


# ============================================================
# 5. SALES STATISTICS
# ============================================================

print("\n========== SALES STATISTICS ==========")

print(df["sales"].describe())


# ============================================================
# 6. PROMOTION STATISTICS
# ============================================================

print("\n========== PROMOTIONS ==========")

print(df["onpromotion"].describe())


# ============================================================
# 7. LIST PRODUCT FAMILIES
# ============================================================

print("\n========== PRODUCT FAMILIES ==========")

for family in sorted(df["family"].unique()):
    print(family)


# ============================================================
# 8. NUMBER OF RECORDS PER STORE
# ============================================================

print("\n========== RECORDS PER STORE ==========")

print(
    df["store_nbr"]
    .value_counts()
    .sort_index()
)


# ============================================================
# 9. TOTAL SALES PER STORE
# ============================================================

print("\n========== TOTAL SALES PER STORE ==========")

store_sales = (
    df.groupby("store_nbr")["sales"]
      .sum()
      .sort_values(ascending=False)
)

print(store_sales)


# ============================================================
# 10. TOTAL SALES PER PRODUCT FAMILY
# ============================================================

print("\n========== TOTAL SALES PER FAMILY ==========")

family_sales = (
    df.groupby("family")["sales"]
      .sum()
      .sort_values(ascending=False)
)

print(family_sales)