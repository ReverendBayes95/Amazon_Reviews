from transformers import pipeline
import pandas as pd
import torch

def hf_classification_pipeline(df: pd.DataFrame, model: str = None) -> pd.DataFrame:

    if model is None:
        classifier = pipeline("text-classification")
    else:
        classifier = pipeline("text-classification", model=model)

    predictions = classifier(list(df['review'].astype(str)), truncation = True)

    return predictions
