import pandas as pd

# Load data
df = pd.read_csv("../data/raw/train.csv", parse_dates=["date"])

pattern = 50
print("="* pattern)
print("DATASET SUMMARY")
print("="* pattern)
# general
print(f"Rows             : {len(df)}")
print(f"Columns          : {df.shape[1]}")
print(f"Stores           : {df['store_nbr'].nunique()}")
print(f"Product families : {df['family'].nunique()}")
print(f"Start date       : {df['date'].min()}")
print(f"End date         : {df['date'].max()}")

# 2. DATA TYPES
print("\n" + "=" * pattern)
print("DATA TYPES")
print("=" * pattern)
print(df.dtypes)# datatypes of argument for column values

print("\n" + "=" * pattern)
print("sales")
print("=" * pattern)
print(df["sales"].describe()) # it give the count , mean , max of the "sales" value

print(f"\nZero sales rows : {(df['sales'] == 0).sum()}") # it will print # first it will conver the row with "0" to True=1 and then do the sum of it
# its doing sum of index?  No
print(f"Zero sales %    : "
    f"{100 * (df['sales'] == 0).mean():.2f}%") # the row which has 0 in sale will be consider true = in pnada term "1", and false greater than 0 sale considering "0".
print(f"Negative sales  : {(df['sales'] < 0).sum():,}")# same it will conver the row sale which is in negative to True, and other False which is 0 or + ve

# ============================================================
# 6. PROMOTION STATISTICS
# ============================================================

print("\n" + "=" * pattern)
print("PROMOTION STATISTICS")
print("=" * pattern)

print(df["onpromotion"].describe()) # again full count, max, min, and description
promotion_rows = (df["onpromotion"] > 0).sum()
print(f"\nRows with promotion : {promotion_rows:,}")

# 7. HIGHEST SELLING PRODUCT FAMILIES
print("\n" + "=" * pattern)
print("TOP 10 PRODUCT FAMILIES BY SALES")
print("=" * pattern)

# group , then sum total sales for each product family,
# then sort from highest total sales to lowest.
family_sales = (df.groupby("family")["sales"].sum().sort_values(ascending=False)) # the order will top sale to bottom (descending))
# .sum()
"""
example data :
family       sales
GROCERY      10
BEVERAGES    20
GROCERY      15
GROCERY       5

this sommand: df.groupby("family")["sales"].sum()
adds:
GROCERY      10 + 15 + 5 = 30
BEVERAGES    20 + 30     = 50
"""

print(family_sales.head(10))


# 9. NUMBER OF UNIQUE DATES
# ============================================================

print("\n" + "=" * pattern)
print("TIME-SERIES INFORMATION")
print("=" * pattern)
print(f"Unique dates: {df['date'].nunique():,}")

expected_days = (df["date"].max() - df["date"].min()).days + 1
print(f"Calendar days in range : {expected_days:,}")
print(f"Dates represented      : {df['date'].nunique():,}")


# ============================================================
# 10. EXPECTED STORE-FAMILY COMBINATIONS
# ============================================================

# store_family_pairs = (df[["store_nbr", "family"]].drop_duplicates())
"""
this store combination of unique store id + family. and if duplicate it will drop that duplicate.
Only calculating this combination without duplicate grouping
"""

# print(f"Store-family combinations: "
#     f"{len(store_family_pairs):,}")

expected_pairs = (df["store_nbr"].nunique() * df["family"].nunique())
print(f"Maximum possible combinations: {expected_pairs:,}")