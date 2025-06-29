import pandas as pd

def create_single_review(df: pd.DataFrame) -> pd.DataFrame:

    df_temp = df.copy()
    df_temp["review"] = df_temp["title"] + "\n " + df_temp["text"]

    return df_temp[["polarity", "review"]]

#def calculate_accuracy