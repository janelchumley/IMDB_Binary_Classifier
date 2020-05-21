import pandas as pd
from sklearn.preprocessing import LabelEncoder

"""Computes the ratio of nulls for the columns in a given dataframe"""
def compute_missing_data(df):
    df_na = (df.isnull().sum() / len(df)) * 100
    df_na = df_na.drop(df_na[df_na == 0].index).sort_values(ascending=False)
    missing_data = pd.DataFrame({'Missing Ratio' :df_na})
    return missing_data

"""Converts large dollar tick values on plots into millions"""
def millions(x, pos):
    return '${:,.1f}M'.format(x*1e-6)

"""Performs imputation on numeric and categorical features"""
def imputate(df, cols, data_type):
    for col in cols:
        if data_type == "numeric":
            df[col] = df[col].fillna((df[col].mean()))
        elif data_type == "object":
            df[col] = df[col].fillna("unknown")
    return df

"""Generates the binary classifier's target variable"""
def is_good_movie(df, x):
    if x>df["movie_score"].median():
        return 1
    else:
        return 0

"""Places continuous values into bins based on quantiles"""
def create_categories(df, x, col):
    if x<df[col].quantile(.25):
        return "very low"
    elif x>df[col].quantile(.25) and x<df[col].quantile(.50):
        return "low"
    elif x>df[col].quantile(.50) and x<df[col].quantile(.75):
        return "high"
    elif x>df[col].quantile(.75):
        return "very high"
    else:
        return "unknown"

"""Drops any columns based on rarity"""
def drop_rare_val_cols(df):
    dropped = []
    threshold = df.shape[0]/5
    for col in df.columns:
        if df[col].nunique() > round(threshold):
            dropped.append(col)
            df = df.drop([col], axis=1)
    return (df, dropped)

"""Performs label encoding on categorical features"""
def label_encoder(df):
    le = LabelEncoder()
    non_numeric_columns = df.dtypes[(df.dtypes == "object")].index
    for c in non_numeric_columns:
        le.fit(list(df[c].values))
        df[c] = le.transform(list(df[c].values))
    return df

"""Removes the the  \xa0 and whitespace characters from a string"""
def encode_and_strip_whitespace(s):
    s = s.replace(u'\xa0', u' ')
    s = s.strip()
    return s
