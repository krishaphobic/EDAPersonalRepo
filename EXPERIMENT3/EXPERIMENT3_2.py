import numpy as np
import pandas as pd

from sklearn.experimental import enable_iterative_imputer  
from sklearn.impute import IterativeImputer, SimpleImputer

df = pd.DataFrame({
    "Age": [25, np.nan, 30, 45, 22],
    "Salary": [50000, 60000, np.nan, 80000, 45000],
    "Category": ["A", "B", "A", np.nan, "B"],
})


mean_imputer = SimpleImputer(strategy="mean")
df["Age_Mean"] = mean_imputer.fit_transform(df[["Age"]]).ravel()

median_imputer = SimpleImputer(strategy="median")
df["Salary_Median"] = median_imputer.fit_transform(df[["Salary"]]).ravel()

mode_imputer = SimpleImputer(strategy="most_frequent")
df["Category_Mode"] = mode_imputer.fit_transform(df[["Category"]]).ravel()

const_imputer = SimpleImputer(strategy="constant", fill_value="Missing")
df["Category_Const"] = const_imputer.fit_transform(df[["Category"]]).ravel()


num_cols = ["Age", "Salary"]
mice_imputer = IterativeImputer(max_iter=10, random_state=42)


mice_array = mice_imputer.fit_transform(df[num_cols])
df[["Age_MICE", "Salary_MICE"]] = mice_array


print(df.to_string())
