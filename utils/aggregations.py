import pandas as pd

def create_single_review(df: pd.DataFrame) -> pd.DataFrame:

    df_temp = df.copy()
    df_temp["review"] = df_temp["title"] + "\n " + df_temp["text"]

    return df_temp[["polarity", "review"]]

def stratified_sample(df: pd.DataFrame, strat_column: str, n_samples: int):
    return df.groupby(strat_column).apply(
        lambda x: x.sample(min(len(x), n_samples))
    ).reset_index(drop=True)