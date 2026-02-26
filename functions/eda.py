import pandas as pd
def eda(df: pd.DataFrame)->None:
    """
    Evaluate basic statistics of a dataframe
    Args:
        df (pd.DataFrame): dataframe to evaluate
    Returns:
        None: prints basic statistics of the dataframe  
        
    """
    print(f"{'='*5}DF Shape: {df.shape} {'='*5}")
    num_cols = []
    cat_cols = []
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            num_cols.append(col)
        else:
            cat_cols.append(col)    
    print(f"{'*'*3}Numeric Cols{'*'*3}")
    for col in num_cols:
        n_min = df[col].min()
        n_max = df[col].max()
        num_na = df[col].isna().sum()
        print(col)
        print(f"\tNum_NA:{num_na}")
        print(f"\t% NA: {(num_na/len(df))*100}%")
        print(f"\tMin: {n_min}")
        print(f"\tMax: {n_max}")
        print(f"\tRange: {n_max - n_min}")
        print(f"\tQ1:{df[col].quantile(0.25)}")
        print(f"\tQ3:{df[col].quantile(0.75)}")
        print(f"\t SD:{df[col].std()}")
    print("\n")
    print(f"{'*'*3}Categorical Cols{'*'*3}")
    for col in cat_cols:
        d = df[col]
        num_null = d.isna().sum()
        print(f"{col}")
        print(f"\tNum NA: {num_null}")
        print(f"\t% NA: {(num_null/len(df))*100}%")
        print(f"\t Num Uniques: {d.nunique()}")
        if d.nunique()<7:
            print(f"Unique Values:{d.unique()}")

    