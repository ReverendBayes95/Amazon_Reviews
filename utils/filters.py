import pandas as pd
import re
from typing import Self

class TextPreProcess:
    """Class for Pre-Processing Amazon reviews"""

    def __init__(self, amazon_reviews:pd.DataFrame, appos:dict)-> None:

        self.amazon_reviews = amazon_reviews.copy()
        self.appos = appos

    def remove_empty_reviews(self)-> Self:

        self.amazon_reviews.loc[:,'title'] = self.amazon_reviews['title'][self.amazon_reviews['title'].str.strip() != '']
        self.amazon_reviews.loc[:,'text'] = self.amazon_reviews['text'][self.amazon_reviews['text'].str.strip() != '']
        return self

    def drop_missing(self) -> Self:

        self.amazon_reviews = self.amazon_reviews.dropna()
        return self

    def convert_lowercase(self) -> Self:

        self.amazon_reviews.loc[:,'title'] = self.amazon_reviews['title'].str.lower()
        self.amazon_reviews.loc[:,'text'] = self.amazon_reviews['text'].str.lower()                                   
        return self
    
    def remove_https(self) -> Self:

        self.amazon_reviews.loc[:,'title'] =  self.amazon_reviews['title'].str.replace(r'https?:\/\/\S+', '', regex=True)
        self.amazon_reviews.loc[:,'text'] =  self.amazon_reviews['text'].str.replace(r'https?:\/\/\S+', '', regex=True)
        return self
    
    def negation_handling(self) -> Self:

        def negation_helper(text, appos):

            text_lower = text.lower().split()
            without_appos = [appos[w]  if w in appos else w for w in text_lower]
            without_appos = " ".join(without_appos)
            return without_appos
        
        self.amazon_reviews.loc[:,'title'] = self.amazon_reviews['title'].apply(lambda s: negation_helper(s, self.appos))
        self.amazon_reviews.loc[:,'text'] = self.amazon_reviews['text'].apply(lambda s: negation_helper(s, self.appos))
        return self

    def apply_text_filtering(self) -> pd.DataFrame:

        return self.drop_missing().remove_empty_reviews().convert_lowercase().remove_https().negation_handling().amazon_reviews