import numpy as np
import pandas as pd

# dataframe
data = np.arange(15, 30).reshape(5, 3)
dfx = pd.DataFrame(data, index=['apple', 'banana', 'kiwi', 'grapes', 'mango'], 
                   columns=['store1', 'store2', 'store3'])
dfx['store4'] = np.nan
dfx.loc['watermelon'] = np.arange(15, 19)
dfx.loc['oranges'] = np.nan
dfx['store5'] = np.nan
dfx.loc['apple', 'store4'] = 20.0


# finding missing values
print("--- 1. dfx.isnull() ---")
print(dfx.isnull())

print("\n--- 2. dfx.notnull() ---")
print(dfx.notnull())

print("\n--- 3. Missing values per store ---")
print(dfx.isnull().sum())

print("\n--- 4. Total missing values in DataFrame ---")
print(dfx.isnull().sum().sum())

print("\n--- 5. Count of reported (non-NaN) values ---")
print(dfx.count())


# dropping missing values
print("\n--- Filtering store4 manually ---")
print(dfx.store4[dfx.store4.notnull()])

print("\n--- Dropping NaNs from store4 Series ---")
print(dfx.store4.dropna())

print("\n--- dfx.dropna() (Drops any row with a single NaN) ---")
print(dfx.dropna())

print("\n--- dfx.dropna(how='all') (Only drops rows that are entirely NaN) ---")
print(dfx.dropna(how='all'))

print("\n--- dfx.dropna(how='all', axis=1) (Only drops columns that are entirely NaN) ---")
print(dfx.dropna(how='all', axis=1))

print("\n--- dfx.dropna(thresh=5, axis=1) (Keeps columns with at least 5 non-NaNs) ---")
print(dfx.dropna(thresh=5, axis=1))


# mathematical operations
print("\n--- NumPy vs Pandas Mean Handling ---")
ar1 = np.array([100, 200, np.nan, 300])
ser1 = pd.Series(ar1)
# Note: np.mean() returns nan if NaN is present, ser.mean() ignores it by default
print(f"NumPy Mean: {np.nanmean(ar1)} (using nanmean) or {ar1.mean()} (standard)") 
print(f"Pandas Series Mean: {ser1.mean()}")

ser2 = dfx.store4
print("\n--- store4 Operations ---")
print(f"Sum: {ser2.sum()}")
print(f"Mean: {ser2.mean()}")
print("Cumulative Sum:")
print(ser2.cumsum())


# filling missing values
print("\n--- Filling all NaNs with 0 ---")
filledDf = dfx.fillna(0)
print(filledDf)

print("\n--- Mean comparison: Original vs Filled ---")
print("Original dfx.mean():")
print(dfx.mean(numeric_only=True))
print("Filled dfx.mean():")
print(filledDf.mean())


print("\n--- Forward Fill (.ffill()) ---")
print(dfx.store4.ffill())

print("\n--- Backward Fill (.bfill()) ---")
print(dfx.store4.bfill())
