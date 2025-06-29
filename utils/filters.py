import pandas as pd
import re

class TextPreProcess:
    """Class for Pre-Processing Amazon reviews"""

    def __init__(self, amazon_reviews:pd.DataFrame, appos:dict)-> None:

        self.amazon_reviews = amazon_reviews
        self.appos = appos

    def drop_missing(self) -> pd.DataFrame:

        self.amazon_reviews = self.amazon_reviews.dropna()
        return self

    def convert_lowercase(self) -> pd.DataFrame:

        self.amazon_reviews.loc['title'] = self.amazon_reviews['title'].apply(lambda s: s.lower())
        self.amazon_reviews.loc['text'] = self.amazon_reviews['text'].apply(lambda s: s.lower())                                    
        return self
    
    def remove_https(self) -> pd.DataFrame:

        self.amazon_reviews.loc['title'] =  self.amazon_reviews['title'].apply(lambda s: re.sub(r'https?:\/\/\S+', '', s))
        self.amazon_reviews.loc['text'] =  self.amazon_reviews['text'].apply(lambda s: re.sub(r'https?:\/\/\S+', '', s))
        return self
    
    def negation_handling(self) -> pd.DataFrame:

        def negation_helper(text, appos):

            text_lower = text.lower().split()
            without_appos = [appos[w]  if w in appos else w for w in text_lower]
            without_appos = " ".join(without_appos)
            return without_appos
        
        self.amazon_reviews.loc['title'] = self.amazon_reviews['title'].apply(lambda s: negation_helper(s, self.appos))
        self.amazon_reviews.loc['text'] = self.amazon_reviews['text'].apply(lambda s: negation_helper(s, self.appos))
        return self

    def apply_text_filtering(self):

        return self.drop_missing().convert_lowercase().remove_https().negation_handling().amazon_reviews